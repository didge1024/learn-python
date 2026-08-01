# learn-python 🐍

**Hey! Welcome. This repo will teach you to code in Python — from your very first line
to building real software that runs on the same kind of systems the pros use.**

You don't need any experience. You *do* get a superpower most people learning to code
never had: **Claude**, an AI tutor that sits right in your terminal and helps you the
whole way. Ask it anything. Get stuck? Ask. Confused by an error? Paste it in and ask.

> 📋 **Prefer a friendly page with one-tap copy buttons for every command?**
> Open the **[Start Here guide](https://claude.ai/code/artifact/32c3d0b3-b578-4128-8706-3e618910936c)** — same steps as below, easier to follow along.

## Get started on your Mac

This is written for a **Mac**. Follow it top to bottom — each step is one copy-paste.

### Step 1 — Open the Terminal

Press **⌘ Command + Space**, type **`Terminal`**, and hit **Return**. A window with a
text prompt opens. This is where you'll type everything below. (Don't worry, it looks
scarier than it is.)

### Step 2 — Install Claude Code (your AI tutor)

Copy this line, paste it into the Terminal, and press **Return**:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Wait for it to finish. Then check it worked:

```bash
claude --version
```

If you see a version number (like `2.1.x (Claude Code)`), you're good. If it says
`command not found`, **close the Terminal window and open a new one**, then try again.

> 💡 Prefer clicking to typing? There's also a **Mac desktop app** —
> [download it here](https://claude.ai/download). Either works.

### Step 3 — Connect your Claude account

Start it up:

```bash
claude
```

The first time, it opens your web browser and asks you to **log in**. Sign in with your
Claude account and approve access — then come back to the Terminal. You're connected. 🔌

> ⚠️ **Heads up (for whoever's paying):** Claude Code needs a paid **Claude Pro or Max**
> plan — the free Claude account doesn't include it. Sign up at
> [claude.ai](https://claude.ai) first if you don't have one.

### Step 4 — Get this project onto your Mac

In the Terminal:

```bash
cd ~/Desktop
git clone https://github.com/didge1024/learn-python.git
cd learn-python
```

(If a box pops up asking to install "command line developer tools," click **Install**,
wait for it to finish, then run the `git clone` line again.)

### Step 5 — Run the setup script (installs everything else)

This one script installs the rest of your toolkit for you: **Homebrew**, a modern
**Python**, **git**, and the **Docker / Colima** container tools you'll grow into later.
It's safe to run more than once. From inside the `learn-python` folder:

```bash
./setup.sh
```

It may ask for your Mac password and your name/email for git — that's normal. When it
finishes, **close the Terminal and open a fresh one**, then `cd ~/Desktop/learn-python`
again so everything loads.

### Step 6 — Run your very first program 🎉

```bash
python3 exercises/hello.py
```

A friendly hello pops up. **You just ran code.**

### Step 7 — Find out where to start

Don't guess where to begin — let the built-in diagnostic point you to the right lesson:

```bash
cd assessment
python3 grade.py
```

### Step 8 — Start learning with Claude

From the `learn-python` folder, launch your tutor and just talk to it:

```bash
claude
```

Then type something like:

> "I'm brand new to programming. Explain what a variable is, then give me a tiny
> exercise to try."

That's it. You're learning. 🚀

## How to actually use Claude as your tutor

Claude is a patient teacher that never gets tired of your questions. Try prompts like:

- "Explain this like I'm 12: what is a `for` loop?"
- "Give me 3 easy exercises on lists, then check my answers."
- "I got this error — what does it mean and how do I fix it?" *(paste the error)*
- "Look at my code and tell me how to make it cleaner."
- "What should I learn next?"

**One rule:** try things yourself *first*, then ask Claude to help or check. The struggle
is where the learning sticks — Claude is there to unblock you, not to do it for you.

## Level up: code in a real editor (VS Code)

Once you're comfortable, you can trade the terminal for a proper editor where you **see
your code, run it, and chat with Claude all at once**. One command sets it up:

```bash
./setup-editor.sh
```

It installs **VS Code** plus the **Python** and **Claude Code** extensions, then opens the
project. You'll get a layout like this:

```
┌───────────────────────┬──────────────────┐
│  your code            │   ✱ Claude        │
│  exercises/hello.py   │   your AI tutor,  │
│  print("hi")          │   right here      │
├───────────────────────┤                  │
│  ▶ Terminal:  hi      │                  │
└───────────────────────┴──────────────────┘
```

- Open a file from the left sidebar, then press the **▶ Run** button (top-right) — the
  output shows up in the terminal right below your code.
- Click the **✱ Claude** icon and **sign in** to chat with your tutor while you code.
- Open a terminal anytime with **Cmd + `** (the key above Tab) to run `./test.sh`, `claude`, etc.

## What's in here

- **`assessment/`** — [a quick diagnostic](assessment/README.md) that tells you where to start. **Run this first.**
- **`curriculum/`** — [the best free courses on the internet](curriculum/README.md) (MIT, Harvard, Berkeley) with the great assignments picked out. The MIT problem sets have [ready-to-code starter files](curriculum/mit-6.0001/) — you fill in the blanks and check them with `./test.sh` (tests are red until you finish; turning them green is the point).
- **`exercises/`** — tiny practice programs to warm up on.
- **`projects/`** — bigger builds that grow into real, deployable apps.

## Where this goes (the exciting part)

You'll start by writing small programs. But the goal is bigger: learning to **build and
run real software the way modern systems actually run it.**

1. **Learn the language** — Python basics, then real programs with tests.
2. **Think like a programmer** — algorithms and problem-solving.
3. **Ship it** — package your app in a **container** (Docker) and run it on an
   **orchestrated cluster** (Kubernetes) — the tech that runs apps like YouTube and
   Netflix behind the scenes.

Every step has free courses and hands-on labs linked in the [curriculum](curriculum/README.md).
Take it one lesson at a time, ask Claude when you're stuck, and you'll get there.

**Now go run `python3 exercises/hello.py` and start. You've got this. 🚀**

---

## Saving your work & trying ideas

- **When you finish for the day, run `./save.sh`.** It shows what you changed, asks you
  to say **yes**, lets you leave a **question or concern for your mentor**, and sends it
  all to GitHub. (Your work also saves automatically when you close Claude.)
- **Want to build your own idea?** Run `./new-feature.sh my cool idea` first — it makes a
  safe **branch** to experiment on without touching your lessons. Back to lessons anytime
  with `git checkout main`.

## For the grown-up who set this up

A few things are wired in to make this a smooth mentor-and-learner loop:

- **`setup.sh`** — one script bootstraps the whole Mac toolchain (Homebrew, modern Python,
  git, and Colima + Docker for the containers track later). Idempotent and commented.
- **`setup-editor.sh` + `.vscode/`** — optional VS Code setup with the Python and Claude
  extensions, pre-configured to dock Claude beside the code and use the project's `.venv`.
- **`CLAUDE.md`** — standing instructions that make Claude tutor like a patient teacher:
  hints over answers, a steady nudge to **write comments**, and encouragement to **branch**
  for new ideas.
- **Auto-update + save-back (hooks, in `.claude/settings.json`):** a `SessionStart` hook
  pulls your latest lessons/notes; a `SessionEnd` hook commits and pushes the learner's
  practice so **you can read their code and comments, then adjust and improve**.
- **`save.sh`** — the learner's approved save: they confirm before anything is sent, and
  it captures their questions into **`notes-for-mentor.md`** so you hear what confused them.
- Hooks are active for anyone using Claude in this folder. To review or disable them, run
  `/hooks` inside Claude, or edit `.claude/settings.json`.
