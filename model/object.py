from dataclasses import dataclass

@dataclass
class Object:
    object_id: int
    object_name: str

    def __str__(self):
        return f"{self._object_id} {self._object_name}"

    def __hash__(self):
        return hash(self.object_id)