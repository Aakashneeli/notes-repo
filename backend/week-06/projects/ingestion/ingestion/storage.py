"""Learner integration: keys must be server-generated UUID hex + .txt.
Local filesystem root is private, controlled by the server, never by clients.
"""
class LocalStorage:
    def __init__(self, root):
        self.root = root
    def put(self, key, data):
        raise NotImplementedError("Validate key, create root, exclusive binary write, clean partial file")
    def read(self, key):
        raise NotImplementedError("Validate key before resolving under root")
    def delete(self, key):
        raise NotImplementedError("Validate key; remove if present, never unrelated paths")
