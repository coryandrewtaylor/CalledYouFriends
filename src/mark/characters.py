from ..books import MARK
from ..models import Character


ANDREW = Character(name="Andrew", book=MARK)

ANGELS = Character(name="Angels", book=MARK, is_collective=True)

GALILAEANS = Character(name="Galilaeans", book=MARK, is_collective=True)

GOD = Character(name="God", book=MARK)

HOLY_SPIRIT = Character(name="Holy Spirit", book=MARK)

JAMES_BAR_ZEBEDEE = Character(name="James, son of Zebedee", book=MARK)

JESUS = Character(name="Jesus", book=MARK)

JOHN_BAR_ZEBEDEE = Character(name="John, son of Zebedee", book=MARK)

JOHN_THE_BAPTIST = Character(name="John the Baptist", book=MARK)

JOHN_THE_BAPTISTS_CAPTORS = Character(
    "John the Baptist's captors", book=MARK, is_collective=True
)

JUDEANS = Character(name="Judeans", book=MARK, is_collective=True)

POSSESSED_MAN_CAPERNAUM_SYNAGOGUE = Character(
    name="Possessed man in Capernaum synagogue", book=MARK
)

UNCLEAN_SPIRIT_CAPERNAUM_SYNAGOGUE = Character(
    name="Unclean spirit in Capernaum synagogue", book=MARK
)

RESIDENTS_OF_JERUSALEM = Character(
    name="Residents of Jerusalem", book=MARK, is_collective=True
)

SCRIBES = Character(name="Scribes", book=MARK, is_collective=True)

SATAN = Character(name="Satan", book=MARK)

SIMON = Character(name="Simon", book=MARK)

SYNAGOGUE_ATTENDEES_IN_CAPERNAUM = Character(
    name="Synagogue attendees in Capernaum", book=MARK, is_collective=True
)

ZEBEDEE = Character(name="Zebedee", book=MARK)

ZEBEDEES_HIRED_MEN = Character(
    name="Zebedee's hired men", book=MARK, is_collective=True
)
