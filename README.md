# learn-python 🐍

**Hey! Welcome. This repo will teach you to code in Python — from your very first line
to building real software that runs on the same kind of systems the pros use.**

You don't need any experience. You *do* get a superpower most people learning to code
never had: **Claude**, an AI tutor that sits right in your terminal and helps you the
whole way. Ask it anything. Get stuck? Ask. Confused by an error? Paste it in and ask.

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

### Step 4 — Check you have Python

Macs come with Python, but let's make sure. In the Terminal:

```bash
python3 --version
```

`Python 3.10` or higher? Perfect. If it's missing or older, just **ask Claude**: type
`claude`, then *"How do I install the latest Python on my Mac?"* and follow along.

### Step 5 — Get this project onto your Mac

In the Terminal:

```bash
cd ~/Desktop
git clone https://github.com/didge1024/learn-python.git
cd learn-python
```

(If `git` asks to install "command line developer tools," click **Install** and wait,
then run the `git clone` line again.)

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

## What's in here

- **`assessment/`** — [a quick diagnostic](assessment/README.md) that tells you where to start. **Run this first.**
- **`curriculum/`** — [the best free courses on the internet](curriculum/README.md) (MIT, Harvard, Berkeley) with the great assignments picked out. The MIT problem sets have [ready-to-code starter files](curriculum/mit-6.0001/) — you fill in the blanks and run the tests.
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
