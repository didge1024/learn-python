# PS5 — RSS Feed Filter

**Source:** MIT 6.0001, Problem Set 5 · https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/assignments/

## Goal

Pull live news stories from RSS feeds and raise an alert when a story matches your
interests. This is the first "real-world data + OOP" assignment.

1. **`NewsStory` class** — holds guid, title, description, link, pubdate.
2. **Trigger classes** — `WordTrigger` (title/description/phrase), `TitleTrigger`,
   `DescriptionTrigger`, and composite triggers `AndTrigger`, `OrTrigger`, `NotTrigger`.
   Use inheritance and an abstract `evaluate(story)` method.
3. **`filter_stories`** — return only the stories that fire at least one trigger.

## Skills

Classes & inheritance, polymorphism, parsing feeds, composing boolean logic.

## How to work it

1. Read the official PDF. The original uses `feedparser`; add it to `requirements.txt`.
2. Build `NewsStory` and the trigger hierarchy (tests target these).
3. Wire up `filter_stories`, then (stretch) poll a live feed on a timer.
