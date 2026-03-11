import json
import os
from conduit.commands.path import CONFIG_DIR

MAX_HISTORY = 10
MEMORY_FILE = os.path.join(CONFIG_DIR, "memory.json")

class MemoryManager:

    def __init__(self):
        self.history = []
        self.load()

    def add(self, role, message):
        self.history.append({"role": role, "content": message})

        if len(self.history) > MAX_HISTORY:
            self.history = self.history[-MAX_HISTORY:]

        self.save()

    def get(self):
        return self.history

    def clear(self):
        self.history = []
        self.save()

    def save(self):
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(self.history, f, indent=2)

    def load(self):
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                self.history = json.load(f)
