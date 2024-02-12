import unittest
from unittest.mock import patch, mock_open
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        if os.path.exists(self.file_storage._FileStorage__file_path):
            os.remove(self.file_storage._FileStorage__file_path)

    # def test_save_writes_correct_data_to_file(self):
    #     if os.path.exists(self.file_storage._FileStorage__file_path):
    #         os.remove(self.file_storage._FileStorage__file_path)
    #         self.file_storage = None
    #     fil_str = FileStorage()
    #     fil_str._FileStorage__file_path = "new_file.json"
    #     self.model.created_at = datetime(2024, 2, 9, 6, 0, 0)
    #     self.model.updated_at = datetime(2024, 2, 9, 6, 0, 0)
    #     fil_str.new(self.model)
    #
    #     with patch("builtins.open", mock_open()) as mock_file:
    #         mock_file.reset_mock()
    #         file_saved = fil_str.save()
    #
    #         mock_file.assert_called_once_with(
    #             fil_str._FileStorage__file_path,
    #             "w",
    #             encoding="utf-8",
    #         )
    #
    #         expected_data = {
    #             f"{self.model.__class__.__name__}.{self.model.id}": {
    #                 "__class__": self.model.__class__.__name__,
    #                 "id": self.model.id,
    #                 "created_at": self.model.created_at.isoformat(),
    #                 "updated_at": self.model.updated_at.isoformat(),
    #             }
    #         }
    #
    #         actual_data = json.loads(mock_file().write.call_args[0][0])
    #         print(actual_data)
    #         self.assertDictEqual(expected_data, actual_data)
    #         self.assertTrue(file_saved)

    # @patch(
    #     "builtins.open",
    #     new_callable=mock_open,
    #     read_data='{"BaseModel.1": {"__class__": "BaseModel", "id": "1"}}',
    # )
    # def test_all_returns_correct_instance_from_file_storage(self, mock_open):
    #     instances = self.file_storage.all()
    #     B_Model = f"BaseModel.{self.model.id}"
    #     self.assertEqual(len(instances), 1)
    #     self.assertIsInstance(instances[B_Model], BaseModel)

    def test_reload(self):
        self.model.save()
        reloaded_data = self.file_storage.all()
        self.assertIsNotNone(reloaded_data)


if __name__ == "__main__":
    unittest.main()
