from .characters import *
from ..books import MARK
from ..models import Scene

I = Scene(
    book=MARK,
    reference="1:4-11",
    location="Jordan River",
    characters=(
        JOHN_THE_BAPTIST,
        JUDEANS,
        RESIDENTS_OF_JERUSALEM,
        JESUS,
        HOLY_SPIRIT,
        GOD,
    ),
)

II = Scene(
    book=MARK,
    reference="1:12-13",
    location="The wilderness",
    characters=(JESUS, HOLY_SPIRIT, SATAN, ANGELS),
)

III = Scene(
    book=MARK,
    reference="1:15",
    characters=(JOHN_THE_BAPTIST, JOHN_THE_BAPTISTS_CAPTORS),
)

IV = Scene(
    book=MARK,
    reference="1:14-15",
    location="Galiilee",
    characters=(JESUS, GALILAEANS),
)

V = Scene(
    book=MARK,
    reference="1:16-18",
    location="Sea of Galilee",
    characters=(JESUS, SIMON, ANDREW),
)

VI = Scene(
    book=MARK,
    reference="1:19-20",
    location="Sea of Galilee",
    characters=(
        JESUS,
        SIMON,
        ANDREW,
        JAMES_BAR_ZEBEDEE,
        JOHN_BAR_ZEBEDEE,
        ZEBEDEE,
        ZEBEDEES_HIRED_MEN,
    ),
)

VII = Scene(
    book=MARK,
    reference="1:21-28",
    location="Capernaum",
    characters=(
        JESUS,
        SIMON,
        ANDREW,
        JAMES_BAR_ZEBEDEE,
        JOHN_BAR_ZEBEDEE,
        SYNAGOGUE_ATTENDEES_IN_CAPERNAUM,
        POSSESSED_MAN_CAPERNAUM_SYNAGOGUE,
        UNCLEAN_SPIRIT_CAPERNAUM_SYNAGOGUE,
        SCRIBES,
    ),
)
