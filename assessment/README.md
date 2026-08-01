# Placement Diagnostic

**This is not a test you pass or fail — it's a compass.** Its only job is to find
**where in the [learning content](../curriculum/README.md) you should start**, so you
don't waste time on things you already know or get thrown in over your head.

Fill in the functions in `assessment.py`, run the diagnostic, and it points you to the
**first topic you haven't mastered yet** — that's your starting line.

It covers five levels of increasing depth:

| Level | Focus | Example task |
|-------|-------|--------------|
| 1 | Fundamentals | FizzBuzz, unit conversion |
| 2 | Data structures | word frequency, two-sum |
| 3 | Functions & recursion | Fibonacci, flatten nested lists |
| 4 | Algorithms | binary search, palindrome check |
| 5 | OOP | implement a `Stack` class |

## How to take it

```bash
cd assessment
python3 grade.py          # runs the grader, prints your score + placement
```

Or, for a detailed pass/fail per function, run this from the repo's main folder
(it sets up the test tool automatically the first time):

```bash
./test.sh assessment
```

Rules of engagement:

- **Do it honestly first.** Fill in `assessment.py` without help. The score is only
  useful if it reflects what *you* can do today.
- Then use Claude to review what you wrote and explain anything that stumped you.
- Retake it after each course stage to watch your level climb.

## How placement works

The diagnostic finds the **first level you can't fully clear** and routes you there —
everything below it, you've already shown you know. It prints a concrete starting point:

| First gap | Start here |
|-----------|-----------|
| Level 1 — Fundamentals | MIT 6.0001 **PS1** (credit-card debt) |
| Level 2 — Data structures | MIT 6.0001 **PS2–PS3** (Hangman, Word Game) |
| Level 3 — Functions & recursion | Berkeley **CS61A** (project *Hog*) |
| Level 4 — Algorithms | MIT **6.006** (Introduction to Algorithms) |
| Level 5 — OOP | MIT 6.0001 **PS5** (RSS filter) / CS61A *Ants* |
| No gaps — all cleared | **Docker → Kubernetes** systems track |

Then work that content with Claude as your tutor, and **re-run the diagnostic** to
confirm the gap closed and move up. It's meant to be taken many times.

## Beyond code: systems self-assessment

Containers and orchestration aren't auto-gradable here, so use this honest checklist —
you "pass" a line when you can do it *and explain it* to someone else:

- [ ] Create and use a Python virtual environment
- [ ] Write a `Dockerfile` and build an image
- [ ] Run a container, map a port, mount a volume
- [ ] Explain the difference between an image and a container
- [ ] Push an image to a registry
- [ ] Write a Kubernetes Deployment + Service manifest
- [ ] `kubectl apply` it to a local cluster and reach the app
- [ ] Explain what a pod is and why orchestration exists
