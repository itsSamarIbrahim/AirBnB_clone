#!/usr/bin/python3
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.name}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            class_name = obj.__class__.__name__
            obj_id = obj.id
            serialized_objects[obj_id] = obj.to_dict()
        with open(self.__file_path, 'w') as File:
            json.dump(serialized_objects, File)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as File:
                loaded_objects = json.load(File)
                for obj_id, obj_dict in loaded_objects.items():
                    class_name = obj_dict['__class__']
                    cls = globals()[class_name]
                    obj = cls(**obj_dict)
                    key = f"{class_name}.{obj_id}"
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
