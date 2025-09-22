class TreeStore:
    def __init__(self, list_items: list):
        self.list_items = list_items
        self.items_by_id = {}
        self.children_by_parent = {}
        self.build_index()

    def build_index(self):
        for item in self.list_items:
            self.items_by_id[item["id"]] = item
            self.children_by_parent.setdefault(item["parent"], []).append(item)

    def getAll(self):
        return self.list_items



