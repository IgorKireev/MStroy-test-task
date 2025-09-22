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
