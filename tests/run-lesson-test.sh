#!/bin/bash
# Test a lesson's steps in the real WSL Ubuntu image, in a throwaway
# podman container (Windows-side steps like `wsl --install` can't be).
# Usage: run-lesson-test.sh [LESSON.qmd]   (DEBUG=1 for detail)
# Image: Canonical's WSL rootfs, what `wsl --install` gives (26.04.1 as
# of 2026-10-28), imported once as wsl-ubuntu:26.04.1.
set -euo pipefail
# Always lowest CPU priority (x280 froze briefly during a run, 2026-10-28).
# ionice is useless here: the NVMe uses the `none` scheduler.
[ "$(nice)" -ge 19 ] || exec nice -n 19 "$0" "$@"
here=$(CDPATH= cd "$(dirname "$0")" && pwd)  # CDPATH makes cd echo the dir
lesson=${1:-$here/../posts/lesson1-setup-gauss.qmd}
img=wsl-ubuntu:26.04.1
url=https://releases.ubuntu.com/resolute/ubuntu-26.04.1-wsl-amd64.wsl
pm() { podman --storage-driver vfs "$@"; }  # x280 is btrfs: no rootless overlay

if ! pm image exists $img; then
  dl=$(mktemp -d); echo "fetching $url" >&2
  curl -sSfL -o "$dl/img.wsl" "$url"
  curl -sSfL "$(dirname $url)/SHA256SUMS" | grep "$(basename $url)" \
    | sed "s|$(basename $url)|$dl/img.wsl|" | sha256sum -c >&2
  pm import "$dl/img.wsl" $img >&2; rm -rf "$dl"
fi

work=$(mktemp -d); chmod 755 "$work"  # the container user must read it
trap 'rm -rf "$work"' EXIT
cp "$here"/lesson-root.sh "$here"/lesson-user.sh "$work"/
uv run -q --with loguru python3 -I "$here/extract_blocks.py" "$lesson" "$work/blocks"
echo "testing $lesson in $img" >&2
# --network host: no tun device needed (x280 runs a kernel whose modules
# were upgraded away until reboot, 2026-10-28); fine for a throwaway test.
time pm run --rm --network host --cpus 2 --memory 3g -e DEBUG="${DEBUG:-}" -v "$work":/lesson:ro "$img" bash /lesson/lesson-root.sh
