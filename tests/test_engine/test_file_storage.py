import unittest
from unittest.mock import patch, mock_open
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "file.json"
        self.file_storage = FileStorage()

    @patch("builtins.open", new_callable=mock_open, read_data='{"BaseModel.1": {"__class__": "BaseModel", "id": "1"}}')
    def test_reload(self, mock_open):
        self.assertIsNotNone(self.file_storage.reload())
        mock_open.assert_called_once_with(self.file_path, 'r', encoding='utf-8')

    @patch("builtins.open", new_callable=mock_open)
    def test_reload_file_not_exist(self, mock_open):
        mock_open.side_effect = FileNotFoundError
        self.assertIsNone(self.file_storage.reload())

    def test_save(self):
        self.file_storage.new(BaseModel())
        with patch("builtins.open", mock_open()) as mock_file:
            self.assertTrue(self.file_storage.save())
            mock_file.assert_called_once_with(self.file_path, 'w', encoding='utf-8')
            mock_file().write.assert_called_once_with('{"BaseModel.1": {"id": "1"}}')

    @patch("builtins.open", new_callable=mock_open)
    def test_save_failure(self, mock_open):
        mock_open.side_effect = OSError
        self.assertFalse(self.file_storage.save())

    @patch("builtins.open", new_callable=mock_open, read_data='{"BaseModel.1": {"__class__": "BaseModel", "id": "1"}}')
    def test_all(self, mock_open):
        self.file_storage.reload()
        instances = self.file_storage.all()
        self.assertEqual(len(instances), 1)
        self.assertIsInstance(instances["BaseModel.1"], BaseModel)

    def test_create_instance(self):
        class_data = {"id": "1"}
        instance = self.file_storage.create_instance("BaseModel", class_data)
        self.assertIsInstance(instance, BaseModel)
        self.assertEqual(instance.id, "1")

    def test_create_instance_invalid_class(self):
        with self.assertRaises(ValueError):
            self.file_storage.create_instance("InvalidClass", {})


if __name__ == '__main__':
    unittest.main()
