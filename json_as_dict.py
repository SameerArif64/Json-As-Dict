import json
import os

class JsonAsDict:
    def __init__(self, file_path, lock=True):
        self.file_path = file_path
        self.lock = lock
        self._data = self._load_data()
    
    def _load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        return {}
    
    def _save_data(self):
        if not self.lock:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(self._data, file, indent=4)
    
    def __getitem__(self, key):
        return self._data.get(key)
    
    def __setitem__(self, key, value):
        self._data[key] = value
        self._save_data()
    
    def __delitem__(self, key):
        if key in self._data:
            del self._data[key]
            self._save_data()
    
    def __iter__(self):
        return iter(self._data)
    
    def __len__(self):
        return len(self._data)
    
    def __contains__(self, key):
        return key in self._data
    
    def clear(self):
        self._data.clear()
        self._save_data()
    
    def keys(self):
        return self._data.keys()
    
    def values(self):
        return self._data.values()
    
    def items(self):
        return self._data.items()
    
    def get(self, key, default=None):
        return self._data.get(key, default)
    
