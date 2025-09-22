class TreeStore:
    def __init__(self, list_items: list) -> None:
        self.list_items = list_items
        self.items_by_id = {}
        self.children_by_parent = {}
        self.build_index()


    def build_index(self) -> None:
        for item in self.list_items:
            self.items_by_id[item["id"]] = item
            self.children_by_parent.setdefault(item["parent"], []).append(item)


    def getAll(self) -> list:
        return self.list_items


    def getItem(self, id: int) -> dict:
        return self.items_by_id.get(id)


    def getChildren(self, id: int) -> list:
        return self.children_by_parent.get(id, [])


    def getAllParents(self, id: int) -> list:
        result = []
        current_item = self.items_by_id.get(id)
        while current_item and current_item["parent"] != "root":
            parent_id = current_item["parent"]
            parent = self.items_by_id.get(parent_id)
            if not parent:
                break
            result.append(parent)
            current_item = parent
        return result


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]


ts = TreeStore(items)


print(ts.getAll())
print(ts.getItem(7))
print(ts.getChildren(4))
print(ts.getChildren(5))
print(ts.getAllParents(7))