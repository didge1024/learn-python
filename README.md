# learn-python

A learning repo for using **Claude** (via Claude Code) as a hands-on tutor for Python —
and, over time, for building and running real software on modern systems: local
environments, containers, and orchestrated platforms like Kubernetes.

The goal isn't just "learn Python syntax." It's to grow from writing a first script
to shipping software that runs the way modern systems actually run it.

## How to use this with Claude

Claude Code is a pair-programmer that lives in your terminal. Use it to:

- **Explain** concepts at your level — ask "why", not just "how".
- **Generate exercises** and then check your solutions.
- **Debug with you** — paste an error and reason through it together.
- **Review your code** and suggest cleaner, more idiomatic approaches.
- **Scaffold projects** — from a single file to a containerized service.

Good prompts to start with:

- "Explain Python list comprehensions with three exercises, then quiz me."
- "Review `exercises/hello.py` and suggest idiomatic improvements."
- "Help me containerize the project in `projects/` and explain each Dockerfile line."
- "Walk me through deploying this container to a local Kubernetes cluster."

## Learning path

The repo is organized so understanding compounds — each stage builds on the last.

### 1. Python fundamentals
- Variables, types, control flow
- Data structures: lists, dicts, sets, tuples
- Functions, modules, and packages
- Files, errors, and the standard library

### 2. Writing real programs
- Virtual environments and dependency management (`venv`, `pip`, `pyproject.toml`)
- Testing with `pytest`
- Linting and formatting (`ruff`, `mypy`)
- Structuring a project people can actually run

### 3. Running software in modern systems
- **The command line & the OS** — processes, environment variables, paths
- **Containers** — packaging an app in a `Dockerfile`, building and running images,
  understanding images vs. containers, ports, and volumes
- **Orchestration** — why we need it, and running workloads on **Kubernetes**:
  pods, deployments, services, and config
- **Automation** — CI/CD basics so changes ship safely and repeatably

## Structure

- `exercises/` — bite-sized practice problems
- `projects/` — small end-to-end programs that grow into deployable services

## Getting started

```bash
python3 --version        # 3.10+ recommended
python3 exercises/hello.py
```

Then open Claude Code in this repo and ask it what to tackle next.

## Roadmap

- [ ] Syntax basics: variables, types, control flow
- [ ] Data structures: lists, dicts, sets, tuples
- [ ] Functions and modules
- [ ] Files and error handling
- [ ] A first small project with tests
- [ ] Containerize a project with Docker
- [ ] Run it on a local Kubernetes cluster
- [ ] Add CI/CD to ship changes automatically
