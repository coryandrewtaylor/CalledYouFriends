from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Book:
    """
    Metadata about a text.

    Parameters
    ----------
    title : str
        The title of the text.
    author : Optional[str], optional
        The author of the text, by default None.
    """

    title: str
    author: Optional[str] = None


@dataclass(frozen=True)
class Character:
    """
    Metadata about a character in a book.

    Parameters
    ----------
    name : str
        The name of the character.
    book : Book
        The book in which the character appears.
    is_collective : bool, optional
        Whether the character is a collective entity, by default False.
    """

    name: str
    book: Book
    is_collective: bool = False


@dataclass(frozen=True)
class Scene:
    """
    Metadata about a scene in a book.

    A "scene," in this context, is a section of text that takes place
    in a single location during a single, contiguous period of time.

    Parameters
    ----------
    book : Book
        The book in which the scene appears.
    reference : str
        The reference to the scene, such as chapter and verse for biblical
        texts or section and paragraph for non-bilical works.
    characters : tuple[Character, ...]
        The characters that appear in the scene. It is assumed that,
        unless explicitly noted in the text, all characters mentioned in the scene are present during the entirety od the scene, and thus all cooccur together.
    location : Optional[str], optional
        The location of the scene, if given in the text, by default None.
    """

    book: Book
    reference: str
    characters: tuple[Character, ...]
    location: Optional[str] = None


@dataclass(frozen=True)
class SpeechAct:
    """
    An instance of a character speaking to another character.

    Parameters
    ----------
    book : Book
        The book in which the instance of dialogue appears.
    reference : str
        The reference to the instance of dialogue, such as chapter and verse for biblical texts or section and paragraph for non-bilical works.
    speaker : Character
        The character who speaks.
    hearer : Character
        The character to whom the speaker is speaking.
    is_direct : bool, optional
        Whether the speech act is direct, by default True. Direct speech acts are those which are recorded in the text as direct quotes. Indirect speech acts are those which are recorded in the text as paraphrases or summaries of what was said.
    is_antagonistic : bool
        Whether the sentiment of the speech act is negative, by default False. Antagonistic speech is equated with negative sentiment. Speech that is neutral or positive is not antagonistic. Sentiment is determined manually, rather than by a machine learning model.
    """

    book: Book
    reference: str
    speaker: Character
    hearer: Character
    is_direct: bool = True
    is_antagonistic: bool = False


@dataclass(frozen=True)
class Coappearance:
    """
    An instance of two characters appearing together in a scene.

    Parameters
    ----------
    scene: Scene
        The scene in which the instance of coapperance appears.
    character_1 : Character
        The first character.
    character_2 : Character
        The second character.
    is_direct : bool, optional
        Whether the coappearance is direct, by default True. Direct coappearances are those in which the two characters appear together, physically, in the same scene. Indirect coappearances are mentions of, or allusions to, an existing relationship between two characters who are not physically present in the same scene.
    """

    scene: Scene
    character_1: Character
    character_2: Character
    is_direct: bool = True
