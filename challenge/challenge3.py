from multiprocessing import Pool
from typing import List
from uuid import uuid4

from challenge.challenge2 import API2


class API3(API2):

    def update(self, data: dict):
        """Store one new object."""
        new_obj = {**data, "id": uuid4()}
        if new_obj["id"] not in self._storage:
            # check if obj already exist or not to avoid duplicate entry
            self._storage[new_obj["id"]] = new_obj
        return new_obj

    def bulk_create(self, data: List[dict]):
        """Store multiple objects.
        we are using multiprocessing.Pool to optimise the for loop
        Even we are not using multiprocessing.Pool

        >> for database engine not supporting multiprocessing, this might not be good solution,
        in such case getting rid of two loops and batch operation can help optimise the solution
        """
        self._maybe_crash()
        pool = Pool(processes=4)
        result = pool.map(self.update, data)
        return result
