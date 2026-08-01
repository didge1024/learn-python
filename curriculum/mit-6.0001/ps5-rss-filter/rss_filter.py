"""PS5 — RSS feed filter. Build the NewsStory class and the trigger hierarchy."""
from abc import ABC, abstractmethod


class NewsStory:
    def __init__(self, guid: str, title: str, description: str, link: str, pubdate=None):
        raise NotImplementedError  # store fields and add getter methods per the PDF


class Trigger(ABC):
    @abstractmethod
    def evaluate(self, story: "NewsStory") -> bool:
        ...


class WordTrigger(Trigger):
    def __init__(self, word: str):
        raise NotImplementedError

    def is_word_in(self, text: str) -> bool:
        """True if self.word appears as a whole word in text (case-insensitive,
        ignoring surrounding punctuation)."""
        raise NotImplementedError


class TitleTrigger(WordTrigger):
    def evaluate(self, story: "NewsStory") -> bool:
        raise NotImplementedError


class AndTrigger(Trigger):
    def __init__(self, t1: Trigger, t2: Trigger):
        raise NotImplementedError

    def evaluate(self, story: "NewsStory") -> bool:
        raise NotImplementedError


def filter_stories(stories: list["NewsStory"], triggers: list[Trigger]) -> list["NewsStory"]:
    """Return the stories for which at least one trigger fires."""
    raise NotImplementedError
