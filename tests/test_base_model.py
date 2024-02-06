# tests/test_base_model.py
import unittest
from models.base_model import BaseModel
from datetime import datetime
import json
import os


class TestBaseModel(unittest.TestCase):

    def test_instance_attributes(self):
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertTrue(hasattr(base_model, 'updated_at'))

    def test_id_is_string(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)

    def test_created_at_is_datetime(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_str_method(self):
        base_model = BaseModel()
        expected_str = "[{}] ({}) {}".format(
            base_model.__class__.__name__, base_model.id, base_model.__dict__)
        self.assertEqual(str(base_model), expected_str)

    def test_save_method(self):
        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(old_updated_at, base_model.updated_at)

    def test_to_dict_method(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()

        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['id'], base_model.id)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')

        created_at_str = base_model_dict['created_at']
        updated_at_str = base_model_dict['updated_at']

        created_at = datetime.strptime(created_at_str, "%Y-%m-%dT%H:%M:%S.%f")
        updated_at = datetime.strptime(updated_at_str, "%Y-%m-%dT%H:%M:%S.%f")

        self.assertEqual(created_at, base_model.created_at)
        self.assertEqual(updated_at, base_model.updated_at)

    def test_to_dict_method_with_custom_class_name(self):
        # Create a derived class and test its serialization
        class CustomModel(BaseModel):
            pass

        custom_model = CustomModel()
        custom_model_dict = custom_model.to_dict()

        self.assertEqual(custom_model_dict['__class__'], 'CustomModel')


if __name__ == '__main__':
    unittest.main()
