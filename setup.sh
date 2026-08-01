#!/usr/bin/env bash
#
# setup.sh — one-time setup for the learn-python environment on a Mac.
#
# Installs (only what's missing):
#   • Xcode Command Line Tools  (gives you git + compilers)
#   • Homebrew                  (the Mac package manager)
#   • a modern Python 3         (via brew)
#   • git                       (via brew, configured for you)
#   • Colima + Docker tools     (run containers without Docker Desktop)
#
# Safe to run more than once — it skips anything already installed.
#
# Run it from the learn-python folder:   ./setup.sh
#
set -euo pipefail

# --- pretty output helpers -------------------------------------------------
bold=$'\033[1m'; green=$'\033[32m'; yellow=$'\033[33m'; blue=$'\033[34m'; reset=$'\033[0m'
step() { printf "\n${bold}${blue}==>${reset} ${bold}%s${reset}\n" "$1"; }
ok()   { printf "  ${green}✓${reset} %s\n" "$1"; }
info() { printf "  ${yellow}•${reset} %s\n" "$1"; }

printf "\n${bold}🐍 learn-python — Mac setup${reset}\n"
printf "This gets your Mac ready to code and run software in containers.\n"

# --- 0. macOS check --------------------------------------------------------
if [[ "$(uname)" != "Darwin" ]]; then
  echo "This script is for macOS. On another system, ask Claude for setup steps." >&2
  exit 1
fi

# --- 1. Xcode Command Line Tools (provides git and build tools) ------------
step "Checking Xcode Command Line Tools"
if xcode-select -p >/dev/null 2>&1; then
  ok "Command Line Tools already installed"
else
  info "Opening the installer — click ${bold}Install${reset} and wait for it to finish."
  xcode-select --install || true
  echo
  read -r -p "  Press Return here once the Command Line Tools have finished installing… " _
fi

# --- 2. Homebrew -----------------------------------------------------------
step "Checking Homebrew (the Mac package manager)"
if ! command -v brew >/dev/null 2>&1; then
  info "Installing Homebrew — you may be asked for your Mac password."
  NONINTERACTIVE=1 /bin/bash -c \
    "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
  ok "Homebrew already installed"
fi

# Make sure brew is on PATH for this script AND future terminals.
if [[ -x /opt/homebrew/bin/brew ]]; then
  BREW_PREFIX=/opt/homebrew            # Apple Silicon (M1/M2/M3…)
elif [[ -x /usr/local/bin/brew ]]; then
  BREW_PREFIX=/usr/local               # Intel Macs
else
  echo "Homebrew installed but 'brew' wasn't found where expected." >&2
  exit 1
fi
eval "$("$BREW_PREFIX/bin/brew" shellenv)"

# Add brew to the login shell so `brew` works in new terminals too.
SHELL_PROFILE="$HOME/.zprofile"   # macOS default shell is zsh
if ! grep -q 'brew shellenv' "$SHELL_PROFILE" 2>/dev/null; then
  printf '\neval "$(%s/bin/brew shellenv)"\n' "$BREW_PREFIX" >> "$SHELL_PROFILE"
  ok "Added Homebrew to your shell profile ($SHELL_PROFILE)"
fi
ok "Homebrew ready ($("$BREW_PREFIX/bin/brew" --version | head -1))"

# --- 3. Core tools: python + git ------------------------------------------
step "Installing modern Python and git"
brew_install() {
  local pkg="$1"
  if brew list --formula "$pkg" >/dev/null 2>&1; then
    ok "$pkg already installed"
  else
    info "Installing $pkg…"
    brew install "$pkg"
    ok "$pkg installed"
  fi
}
brew_install git
brew_install python

ok "Python: $(python3 --version 2>&1)"
ok "git:    $(git --version 2>&1)"

# --- 4. Configure git so commits have a name on them -----------------------
step "Setting up git"
if [[ -z "$(git config --global user.name || true)" ]]; then
  read -r -p "  What name should show on your code commits? " git_name
  git config --global user.name "${git_name:-Python Learner}"
  ok "git name set to '$(git config --global user.name)'"
else
  ok "git name already set ('$(git config --global user.name)')"
fi
if [[ -z "$(git config --global user.email || true)" ]]; then
  read -r -p "  What email should show on your commits? " git_email
  git config --global user.email "${git_email:-learner@learn-python.local}"
  ok "git email set to '$(git config --global user.email)'"
else
  ok "git email already set ('$(git config --global user.email)')"
fi
git config --global init.defaultBranch main >/dev/null 2>&1 || true

# --- 5. Containers: Colima + Docker tools ----------------------------------
# Colima runs a lightweight Linux VM so `docker` works without Docker Desktop.
step "Installing container tools (Colima + Docker)"
brew_install colima
brew_install docker            # the `docker` command-line client
brew_install docker-compose    # multi-container projects

step "Starting Colima (your container engine)"
if colima status >/dev/null 2>&1; then
  ok "Colima is already running"
else
  info "Starting Colima — first launch downloads a small Linux image, please wait…"
  colima start
  ok "Colima started"
fi

# Prove docker actually works end-to-end.
if docker ps >/dev/null 2>&1; then
  ok "Docker is working ($(docker --version 2>&1))"
else
  info "Docker command installed but couldn't reach the engine yet."
  info "Try opening a NEW terminal and running: colima start"
fi

# --- Done ------------------------------------------------------------------
printf "\n${bold}${green}🎉 All set!${reset}\n"
cat <<'NEXT'

  Next steps:
    1. Close this Terminal and open a fresh one (so everything loads).
    2. Come back to this folder:   cd ~/Desktop/learn-python
    3. Run your first program:     python3 exercises/hello.py
    4. Find where to start:        cd assessment && python3 grade.py
    5. Start your tutor:           claude

  Have fun — you've got this! 🚀
NEXT
