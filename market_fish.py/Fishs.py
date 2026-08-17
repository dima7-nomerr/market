from dataclasses import dataclass

@dataclass(slots=True)
class Fish:
    mazvanie_prodykta: str
    vid: str
    prigotovlenie: str
    data_isgotovleni: str
    ves: str
    tsena: int
    razmer: str
    id: int | None = None

