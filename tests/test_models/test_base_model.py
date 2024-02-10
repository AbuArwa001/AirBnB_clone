import unittest
from models.base_model import BaseModel
from datetime import datetime
import json
import os


class TestBaseModel(unittest.TestCase):
    test_json_file = "file.json"

    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        if os.path.exists(self.test_json_file):
            os.remove(self.test_json_file)

    def test_instance_attributes(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_method(self):
        expected_str = "[{}] ({}) {}".format(
            self.base_model.__class__.__name__,
            self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        base_model_dict = self.base_model.to_dict()

        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['id'], self.base_model.id)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')

        created_at_str = base_model_dict['created_at']
        updated_at_str = base_model_dict['updated_at']

        created_at = datetime.strptime(created_at_str, "%Y-%m-%dT%H:%M:%S.%f")
        updated_at = datetime.strptime(updated_at_str, "%Y-%m-%dT%H:%M:%S.%f")

        self.assertEqual(created_at, self.base_model.created_at)
        self.assertEqual(updated_at, self.base_model.updated_at)

    def test_to_dict_method_with_custom_class_name(self):
        # Create a derived class and test its serialization
        class CustomModel(BaseModel):
            pass

        custom_model = CustomModel()
        custom_model_dict = custom_model.to_dict()

        self.assertEqual(custom_model_dict['__class__'], 'CustomModel')

    def test_json_file_saving(self):
        # Truncate the file to make it empty
        with open(self.test_json_file, 'w') as f:
            f.truncate()

        # Save object to a JSON file
        self.base_model.save()

        # Check if file exists
        self.assertTrue(os.path.exists(self.test_json_file))

        # Load JSON file and check if data matches
        with open(self.test_json_file, 'r') as f:
            data = json.load(f)
            for key in data.keys():
                klass, id = key.split('.')
                if id == self.base_model.id:
                    self.assertEqual(id, self.base_model.id)
                    self.assertEqual(
                        datetime.fromisoformat(data[key]['created_at']),
                        self.base_model.created_at)
                    self.assertEqual(
                        datetime.fromisoformat(data[key]['updated_at']),
                        self.base_model.updated_at)
                    self.assertEqual(data[key]['__class__'], 'BaseModel')
                    break


if __name__ == '__main__':
    unittest.main()
