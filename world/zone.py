class Zone:
    """
    This class represents a zone on the map.
    For exemple: Home, Park, School, etc...

    A zone is represented by a name and coordinates ((x0, y0), (x1, y1)).
    """
    name: str
    start_zone: tuple[int, int]
    end_zone: tuple[int, int]

    def __init__(self, name: str, start_zone: tuple[int, int], end_zone: tuple[int, int]) -> None:
        assert(isinstance(name, str))
        assert(isinstance(start_zone, tuple))
        assert(isinstance(end_zone, tuple))
        assert(start_zone[0] >= 0 and start_zone[1] >= 0)
        assert(end_zone[0] >= 0 and end_zone[0] > start_zone[0])
        assert(end_zone[1] >= 0)
        
        self.name = name.strip().lower()
        self.start_zone = start_zone
        self.end_zone = end_zone

    def has(self, x: int, y: int) -> bool:
        if (x >= self.start_zone[0] and x <= self.end_zone[0]):
            if (y >= self.start_zone[1] and y <= self.end_zone[0]):
                return True
        
        return False