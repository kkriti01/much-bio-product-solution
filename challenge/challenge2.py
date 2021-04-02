import os
import random
from uuid import uuid4

from challenge.challenge1 import API1


class API2(API1):
    def create(self, data: dict):
        """Store one new object.
        Just adding a check to avoid duplicate entry, so that if program restart
        can be idempotent in case of random crashes.
        """
        self._maybe_crash()
        new_obj = {**data, "id": uuid4()}
        if new_obj["id"] not in self._storage:
            # check if obj already exist or not to avoid duplicate entry
            self._storage[new_obj["id"]] = new_obj
        return new_obj

    @staticmethod
    def _maybe_crash():
        """Will this crash? No one knows. Very exciting."""
        if random.random() < 0.01:
            os._exit(0)
