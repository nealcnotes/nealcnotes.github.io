#!/bin/bash
# Runs inside the container as the new user, playing the student:
# every bash/fish block of the lesson, in page order, from the folder
# she'd be in. Interactive lines become their non-interactive twins.
# Blocks are in /lesson/blocks (extract_blocks.py). DEBUG=1 for detail.
set -uo pipefail
B=/lesson/blocks
PW=$1
log() { [ -n "${DEBUG:-}" ] && echo "  [debug] $*" >&2; return 0; }
fails=()
cwd=$HOME

# Files she types in nvim, taken from the lesson's own python/lean blocks.
next_block() {  # next_block <blockfile> <lang> : first <lang> block after it
  ls $B/*."$2" | awk -v me="$1" '$0 > me' | head -1
}
seed() {  # seed <file> <current blockfile> : what she'd have typed into it
  case $1 in
    hello.txt)  echo hello ;;
    *.py)       cat "$(next_block "$2" python)" ;;  # the code shown right after
    *) echo "no seed for $1" >&2; return 1 ;;
  esac
}

# Translate one block's lines into what we can run unattended.
translate() {  # translate <blockfile>
  while IFS= read -r line; do
    case $line in
      "nvim "*) f=${line#nvim }; log "nvim $f -> seeded"
                # base64, because fish has no heredocs
                echo "echo $(seed "$f" "$1" | base64 -w0) | base64 -d > $f" ;;
      claude)   log "claude -> claude --version"; echo "claude --version" ;;
      python3)  py=$(next_block "$1" python)
                log "python3 REPL -> fed $py"; echo "python3 -q -i < $py" ;;
      *)        echo "$line" ;;
    esac
  done < "$1"
}

for f in $(ls $B | sort); do
  lang=${f##*.}
  [[ $lang == bash || $lang == fish ]] || { log "skip $f ($lang)"; continue; }
  code=$(translate $B/$f)
  echo "=== $f (in ${cwd/#$HOME/~})" >&2
  # Stop at the first failing line, like her reading an error.
  # Login shells: each block is like a fresh pane (Alt+Shift+D).
  if [[ $lang == bash ]]; then
    printf 'set -e\ncd %q\n%s\npwd > /tmp/cwd\n' "$cwd" "$code" > /tmp/blk
    run="bash -l /tmp/blk"
  else
    { printf 'cd %q\n' "$cwd"; sed 's/$/; or exit $status/' <<<"$code"
      echo 'pwd > /tmp/cwd'; } > /tmp/blk
    run="fish -l /tmp/blk"
  fi
  log "$(cat /tmp/blk)"
  if [[ $code == *sudo* ]] && ! sudo -n true 2>/dev/null; then
    # sudo-rs (Ubuntu 26.04) reads the password from a terminal only:
    # give it a pseudo-terminal and type her password into it.
    log "$f: sudo still wants a password, typing it via script(1)"
    out=$(printf '%s\n' "$PW" | script -qec "$run" /dev/null 2>&1); rc=$?
  else
    out=$($run 2>&1); rc=$?
  fi
  echo "$out" | tail -4 | sed 's/^/    /' >&2
  [[ -s /tmp/cwd ]] && cwd=$(cat /tmp/cwd)
  if (( rc != 0 )); then echo "    FAIL rc=$rc" >&2; fails+=("$f"); fi
done

# What the lesson promises, checked.
check() {  # check <description> <command> <expected substring>
  out=$(cd ~/course && fish -l -c "$2" 2>&1)
  if [[ $out == *"$3"* ]]; then echo "ok   $1" >&2
  else echo "FAIL $1: wanted '$3', got: $(echo "$out" | tail -3)" >&2; fails+=("$1"); fi
}
check "login shell is fish" "getent passwd $USER" "/usr/bin/fish"
check "sudo asks no password" "sudo -n true; and echo nopw" "nopw"
check "CLAUDE.md is in course/" "head -1 CLAUDE.md" "# Tutor mode"
check "hello.txt says hello" "cat hello.txt" "hello"
check "decide.py says 7 is odd" "python3 decide.py" "7 is odd"
check "parity.py says 7 odd" "python3 parity.py | head -1" "7 odd"
check "cp kept decide.py as it was" "python3 decide.py" "7 is odd"
check "loop.py ends at 5 25 odd" "python3 loop.py | tail -1" "5 25 odd"
check "gauss.py: last step, then the answer" "python3 gauss.py | tail -2 | string join ' '" "100 5050 5050"
check "range(1, n) stops at 99" \
  "sed 's/range(1, n + 1)/range(1, n)/' gauss.py > g99.py; python3 g99.py | tail -1" "4950"
check "missing indent is an IndentationError" \
  "sed 's/^ *total = total/total = total/' gauss.py > gbad.py; python3 gbad.py" "IndentationError"
check "claude is on fish's PATH" "command -v claude" ".local/bin/claude"
check "check.py: all 1000 agree" "python3 check.py" "all 1000 agree"
check "invariant.py ends at 5050" "python3 invariant.py | tail -1" "5050"
check "a wrong step trips the assert" \
  "sed 's/total + k$/total + k + 1/' invariant.py > ibad.py; python3 ibad.py" "AssertionError"
echo >&2
if (( ${#fails[@]} )); then echo "FAILED: ${fails[*]}" >&2; exit 1; fi
echo "ALL OK" >&2
