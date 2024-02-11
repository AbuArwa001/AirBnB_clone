import unittest
from unittest.mock import patch, mock_open
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json

"""
Module to test the Amenity class functionality.
"""


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        Set up a FileStorage instance for testing.
        """
        self.file_storage = FileStorage()

    def tearDown(self):
        """
        Clean up after each test by resetting FileStorage instance.
        """
        self.file_storage = None

    def test_save_writes_correct_data_to_file(self):
        """
        Test that save method writes correct data to the file.
        """
        # Create a BaseModel instance
        model = BaseModel()
        model.id = "1"
        # Mock the creation time
        model.created_at = datetime(2024, 2, 9, 6, 0, 0)
        # Mock the update time
        model.updated_at = datetime(2024, 2, 9, 6, 0, 0)
        model.created_at = model.created_at.isoformat()
        model.updated_at = model.updated_at.isoformat()
        self.file_storage.new(model)

        # Mock the 'open' function and write data to the file
        with patch("builtins.open", mock_open()) as mock_file:
            file_saved = self.file_storage.save()

            # Assert that the file was opened with the correct arguments
            mock_file.assert_called_once_with(
                self.file_storage._FileStorage__file_path,
                "w",
                encoding="utf-8",
            )

            # Construct expected dictionary
            expected_data = {
                f"{model.__class__.__name__}.{model.id}": {
                    "__class__": model.__class__.__name__,
                    "id": model.id,
                    "created_at": model.created_at,
                    "updated_at": model.updated_at,
                }
            }

            # Deserialize actual data from the written file
            actual_data = json.loads(mock_file().write.call_args[0][0])

            # Compare dictionaries
            self.assertDictEqual(expected_data, actual_data)
            self.assertTrue(file_saved)

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='{"BaseModel.1": {"__class__": "BaseModel", "id": "1"}}',
    )
    def test_all_returns_correct_instance_from_file_storage(self, mock_open):
        """
        Test that all method returns correct instances from file storage.
        """
        # Call the test_save method to save a BaseModel instance
        self.test_save_writes_correct_data_to_file()

        # Reload the data from the file storage
        self.file_storage.reload()

        # Get all instances from the file storage
        instances = self.file_storage.all()

        # Check if there is exactly one instance and it is of type BaseModel
        self.assertEqual(len(instances), 1)
        self.assertIsInstance(instances["BaseModel.1"], BaseModel)

    def test_reload(self):
        """
        Test that reload method reloads data from file storage.
        """
        # Save some data to the file storage
        model = BaseModel()
        model.id = "1"  # Set a known ID
        self.file_storage.new(model)
        self.file_storage.save()

        # Reload the data from the file storage
        reloaded_data = self.file_storage.reload()

        # Assert that reloaded_data is not None
        self.assertIsNotNone(reloaded_data)


if __name__ == "__main__":
    unittest.main()
