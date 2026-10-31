#!/bin/bash
# Container entry, as root: do what WSL's first launch does
# (make the user with a password, in the sudo group), then hand over.
set -euo pipefail
U=anna PW=lesson-test-pw
useradd -m -s /bin/bash -G sudo "$U"
echo "$U:$PW" | chpasswd
echo "made user $U (groups: $(id -nG $U))" >&2
exec runuser -u "$U" -- env DEBUG="${DEBUG:-}" bash /lesson/lesson-user.sh "$PW"
