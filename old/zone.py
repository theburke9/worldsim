class Zone:
    def __init__(self, label: str, x1: int, y1: int, x2: int, y2: int):
        self.label = label
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def contains(self, x: int, y: int):
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2

    def __str__(self):
        return f"Zone(label: {self.label}, x1: {self.x1}, x2: {self.x2}, y1: {self.y1}, y2: {self.y2})"


if __name__ == "__main__":
    zone = Zone(0, 5, 0, 5, "house")
    print(zone)