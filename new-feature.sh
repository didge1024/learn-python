#!/usr/bin/env bash
#
# new-feature.sh — start a new idea safely on its own branch.
#
# When you want to build something NEW (not a lesson), do it on a "branch" — a
# separate copy of your work — so the main lessons stay safe. Your mentor can
# look at your idea on its own without it getting mixed up with everything else.
#
# Usage:   ./new-feature.sh my cool idea
#     or:  ./new-feature.sh          (it will ask you for a name)
#
set -euo pipefail

bold=$'\033[1m'; green=$'\033[32m'; blue=$'\033[34m'; reset=$'\033[0m'

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "This folder isn't set up with git yet. Ask your mentor for help." >&2
  exit 1
fi

# Get a name for the idea (from the arguments, or by asking).
name="$*"
if [[ -z "$name" ]]; then
  read -r -p "What do you want to call your new idea? " name
fi

# Turn "My Cool Idea!" into a tidy branch name like "feature/my-cool-idea".
slug="$(printf '%s' "$name" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd 'a-z0-9-')"
[[ -z "$slug" ]] && slug="idea"
branch="feature/$slug"

# Make sure new work starts from an up-to-date main.
git checkout -q main 2>/dev/null || true
git pull --ff-only --quiet 2>/dev/null || true

if git switch -c "$branch" 2>/dev/null || git checkout -b "$branch" 2>/dev/null; then
  printf "\n${bold}${green}🌱 You're now on a new branch: %s${reset}\n" "$branch"
else
  # Branch already exists — just hop onto it.
  git switch "$branch" 2>/dev/null || git checkout "$branch"
  printf "\n${bold}${green}↩️  Switched back to your branch: %s${reset}\n" "$branch"
fi

cat <<NEXT

  Now build your idea here — the main lessons are untouched.
  When you're ready to save it, run:  ${bold}./save.sh${reset}

  Done experimenting? Go back to your lessons with:  ${bold}git checkout main${reset}

NEXT
