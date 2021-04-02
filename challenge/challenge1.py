from uuid import uuid4


class API1:
    def __init__(self):
        self._storage = {}

    def _get_ancestors(self, obj_id):
        """
        recursive function to find all ancestors and returns the list if its name
        :param obj_id: str
        :return: List[str]
        """
        ancestors = []
        if obj_id is None:
            return ancestors
        obj = self._storage.get(obj_id)
        ancestors.append(obj['name'])
        self._get_ancestors(obj['parent_id'])

    def get(self, obj_id: str):
        """Get an object."""
        obj = self._storage.get(obj_id)
        obj.pop('children_ids')  # remove key `children_ids`
        obj['ancestors'] = self._get_ancestors(obj.parent_id)  # get list of all ancestors
        return obj

    def create(self, data: dict):
        """Store one new object."""
        new_obj = {**data, "id": uuid4()}
        self._storage[new_obj["id"]] = new_obj
        return new_obj
