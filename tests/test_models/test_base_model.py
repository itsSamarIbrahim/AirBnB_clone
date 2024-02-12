#!/usr/bin/python3
import unittest
from unittest.mock import MagicMock
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from uuid import uuid4

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.mock_storage = MagicMock()

    def test_initialization_without_arguments(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_initialization_with_storage(self):
        model = BaseModel(storage=self.mock_storage)
        self.mock_storage.new.assert_called_once()

    def test_initialization_with_arguments(self):
        created_at = datetime(2022, 1, 1)
        updated_at = datetime(2022, 2, 2)
        model = BaseModel(
            id="test_id",
            created_at=created_at,
            updated_at=updated_at,
            custom_attr="custom_value"
        )
        self.assertEqual(model.id, "test_id")
        self.assertEqual(model.created_at, created_at)
        self.assertEqual(model.updated_at, updated_at)
        self.assertEqual(model.custom_attr, "custom_value")

    def test_save(self):
        model = BaseModel(storage=self.mock_storage)
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, original_updated_at)
        self.mock_storage.save.assert_called_once()

    def test_to_dict(self):
        created_at = datetime(2022, 1, 1)
        updated_at = datetime(2022, 2, 2)
        model = BaseModel(
            id="test_id",
            created_at=created_at,
            updated_at=updated_at,
            custom_attr="custom_value"
        )
        expected_dict = {
            'id': 'test_id',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-02-02T00:00:00',
            'custom_attr': 'custom_value',
            '__class__': 'BaseModel'
        }
        self.assertEqual(model.to_dict(), expected_dict)

    def test_str(self):
        model = BaseModel(id="test_id")
        expected_string = "[BaseModel] (test_id) {'id': 'test_id', 'created_at': %r, 'updated_at': %r}" % (model.created_at, model.updated_at)
        self.assertEqual(str(model), expected_string)

if __name__ == '__main__':
    unittest.main()

