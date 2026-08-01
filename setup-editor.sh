#!/usr/bin/env bash
#
# setup-editor.sh — set up VS Code as your coding editor, with Python + Claude.
#
# After this you'll have a real editor where you can see your code, run it in a
# terminal right next to it, and chat with Claude in a side panel — all at once.
#
# Installs (only what's missing):
#   • Visual Studio Code            (the editor)
#   • the Python extension          (run + check your code, colors, hints)
#   • the Claude Code extension     (your AI tutor, inside the editor)
#
# Run it from the learn-python folder, after ./setup.sh:   ./setup-editor.sh
#
set -euo pipefail

bold=$'\033[1m'; green=$'\033[32m'; yellow=$'\033[33m'; blue=$'\033[34m'; reset=$'\033[0m'
step() { printf "\n${bold}${blue}==>${reset} ${bold}%s${reset}\n" "$1"; }
ok()   { printf "  ${green}%s${reset} %s\n" "✓" "$1"; }
info() { printf "  ${yellow}%s${reset} %s\n" "•" "$1"; }

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

printf "\n${bold}🧑‍💻 Setting up your VS Code editor${reset}\n"

if [[ "$(uname)" != "Darwin" ]]; then
  echo "This script is for macOS. Ask Claude for steps on another system." >&2
  exit 1
fi

# --- 1. Install VS Code (via Homebrew) -------------------------------------
step "Installing Visual Studio Code"
if [[ -d "/Applications/Visual Studio Code.app" ]]; then
  ok "VS Code already installed"
elif command -v brew >/dev/null 2>&1; then
  info "Installing VS Code with Homebrew..."
  brew install --cask visual-studio-code
  ok "VS Code installed"
else
  echo "Homebrew isn't installed. Run ./setup.sh first, then try again." >&2
  exit 1
fi

# --- 2. Find the 'code' command --------------------------------------------
# Homebrew usually puts 'code' on your PATH; if not, use the copy inside the app.
CODE_BIN=""
if command -v code >/dev/null 2>&1; then
  CODE_BIN="code"
elif [[ -x "/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code" ]]; then
  CODE_BIN="/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code"
  # Make 'code' work in future terminals too.
  APP_BIN="/Applications/Visual Studio Code.app/Contents/Resources/app/bin"
  if ! grep -q "Visual Studio Code.app/Contents/Resources/app/bin" "$HOME/.zshrc" 2>/dev/null; then
    printf '\nexport PATH="%s:$PATH"\n' "$APP_BIN" >> "$HOME/.zshrc"
    ok "Added the 'code' command to your shell (open a new Terminal to use it)"
  fi
fi

if [[ -z "$CODE_BIN" ]]; then
  info "Installed VS Code, but couldn't find the 'code' command yet."
  info "Open VS Code once, press Cmd+Shift+P, run 'Shell Command: Install code command in PATH', then re-run this script."
  exit 0
fi

# --- 3. Install the extensions ---------------------------------------------
step "Installing editor extensions"
install_ext() {
  local ext="$1" label="$2"
  if "$CODE_BIN" --list-extensions 2>/dev/null | grep -qix "$ext"; then
    ok "${label} already installed"
  else
    info "Installing ${label}..."
    "$CODE_BIN" --install-extension "$ext" --force >/dev/null 2>&1 \
      && ok "${label} installed" \
      || info "Couldn't install ${label} automatically — you can add it from the Extensions panel."
  fi
}
install_ext "ms-python.python" "Python extension"
install_ext "anthropic.claude-code" "Claude Code extension"

# --- 4. Open the project ---------------------------------------------------
step "Opening your project in VS Code"
"$CODE_BIN" . >/dev/null 2>&1 || true

printf "\n${bold}${green}🎉 Your editor is ready!${reset}\n"
cat <<'NEXT'

  In VS Code:
    • Click a file in the left sidebar (try exercises/hello.py) to open it.
    • Press the ▶ Run button (top-right) to run it — output appears in the
      terminal panel right next to your code.
    • Click the ✱ Claude icon (top-right or right sidebar) and sign in to chat
      with your tutor while you work.

  Tip: open the terminal anytime with  Cmd + `  (the key above Tab).

  Happy coding! 🚀
NEXT
