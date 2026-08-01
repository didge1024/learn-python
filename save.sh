#!/usr/bin/env bash
#
# save.sh — save your work and send it to GitHub for your mentor to read.
#
# Run this whenever you finish for the day:   ./save.sh
#
# It shows you what you changed, asks you to say YES, lets you leave a note or a
# question for your mentor, and then saves everything to GitHub. Nothing is sent
# anywhere unless YOU approve it here.
#
set -euo pipefail

bold=$'\033[1m'; green=$'\033[32m'; yellow=$'\033[33m'; blue=$'\033[34m'; dim=$'\033[2m'; reset=$'\033[0m'

# Work from the repo folder no matter where it's run from.
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Hmm, this folder isn't set up with git yet. Ask your mentor for help." >&2
  exit 1
fi

# Is there anything new to save?
if [[ -z "$(git status --porcelain)" ]]; then
  printf "\n${green}Nothing new to save yet${reset} — do some coding, then run ${bold}./save.sh${reset} again. 🙂\n\n"
  exit 0
fi

printf "\n${bold}${blue}Here's what you worked on:${reset}\n\n"
git -c color.status=always status --short
printf "\n${dim}"
git --no-pager diff --stat --color=always 2>/dev/null || true
printf "${reset}\n"

# --- Noah approves (or not) ------------------------------------------------
read -r -p "${bold}Save these and send them to your mentor on GitHub? [y/N] ${reset}" answer
case "${answer:-}" in
  [yY]|[yY][eE][sS]) ;;
  *)
    printf "\n${yellow}Okay — nothing was saved.${reset} Run ${bold}./save.sh${reset} again whenever you're ready.\n\n"
    exit 0
    ;;
esac

# --- A one-line summary of what you did ------------------------------------
read -r -p "In a few words, what did you do? (or just press Return) " summary
[[ -z "${summary:-}" ]] && summary="Practice session $(date '+%Y-%m-%d %H:%M')"

# --- Any comments or concerns for your mentor ------------------------------
# These get written into notes-for-mentor.md and committed too, so your mentor
# can read exactly what confused you or what you want help with.
read -r -p "Any questions or things that confused you? (for your mentor, or Return to skip) " concern
if [[ -n "${concern:-}" ]]; then
  {
    echo ""
    echo "## $(date '+%Y-%m-%d %H:%M') — $summary"
    echo ""
    echo "$concern"
  } >> notes-for-mentor.md
  printf "  ${green}✓${reset} Added your note to notes-for-mentor.md\n"
fi

# --- Save and send ---------------------------------------------------------
git add -A
git commit -q -m "$summary"

printf "\n${blue}Sending to GitHub…${reset}\n"
if GIT_TERMINAL_PROMPT=0 git push -q 2>/dev/null; then
  printf "\n${bold}${green}🎉 Saved and sent!${reset} Your mentor can now read your code and comments.\n\n"
else
  printf "\n${yellow}Saved on your computer${reset}, but couldn't upload to GitHub just now.\n"
  printf "Check your internet and try ${bold}./save.sh${reset} again, or ask your mentor to help connect GitHub.\n\n"
fi
