import unittest
from unittest.mock import patch, MagicMock
import os
import json
from models.engine.file_storage import (
    FileStorage,
)  # Update with the actual module name
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.file_content = '{\
        "BaseModel.test_id": {"__class__": "BaseModel", "id": "test_id"}\
        }'
        self.file_path = "file.json"

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        # Test that all() returns the __objects dictionary
        all = self.storage.all()
        self.assertEqual(all, {})

    def test_create_instance(self):
        # Test create_instance method with valid class name
        obj_data = {"__class__": "BaseModel", "id": "123"}
        obj = self.storage.create_instance("BaseModel", obj_data)
        self.assertEqual(obj.__class__.__name__, "BaseModel")
        self.assertEqual(obj.id, "123")

        # Test create_instance method with invalid class name
        with self.assertRaises(ValueError):
            self.storage.create_instance("InvalidClass", obj_data)

    def test_new(self):
        # Test new method to add object to __objects dictionary
        class MockObj:
            def __init__(self):
                self.__class__.__name__ = "MockObj"
                self.id = "mock_id"

        mock_obj = MockObj()
        self.storage.new(mock_obj)
        self.assertIn("MockObj.mock_id", self.storage._FileStorage__objects)

    @patch("builtins.open", create=True)
    def test_save(self, mock_open):
        # Test save method
        mock_file = mock_open.return_value
        mock_file.write.return_value = None
        isinstance = BaseModel({"__class__": "TestObj", "id": "test_id"})
        self.storage._FileStorage__objects = {"TestObj.test_id": isinstance}
        self.assertTrue(self.storage.save())

    # @patch('builtins.open', create=True)
    # def test_reload(self, mock_open):
    #     # Create a mock file content
    #     instance_data = {
    #         "BaseModel.test_id": {"__class__": "BaseModel", "id": "test_id"}
    #     }
    #     mock_file_content = json.dumps(instance_data)
    #     try:
    #         with open(self.file_path, "w", encoding="utf-8") as file:
    #             print("WRITE")
    #             file.write(mock_file_content)
    #     except Exception as e:
    #         print("Error writing to file:", e)
    #     # Call reload method
    #     self.assertTrue(self.storage.reload())

    #     # Assertions
    #     self.assertIn(
    # "BaseModel.test_id", self.storage._FileStorage__objects)


if __name__ == "__main__":
    unittest.main()
