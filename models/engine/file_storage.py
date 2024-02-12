#!/usr/bin/python3
import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            loaded_objects = {}
            if os.path.exists(self.__file_path):
                with open(self.__file_path, "r", encoding="UTF-8") as f:
                    loaded_objects = json.loads(f.read())
                """ convert dict to obj and insert them in __objects """
                for key, obj_dict in loaded_objects.items():
                    class_name = obj_dict.get('__class__')
                    if class_name in globals():
                        cls = globals()[class_name]
                        instance = cls(**obj_dict)
                        self.__objects[key] = instance
        except FileNotFoundError:
            pass
