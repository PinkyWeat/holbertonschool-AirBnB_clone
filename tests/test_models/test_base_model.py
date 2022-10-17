#!/usr/bin/python3
"""python interpreter"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import datetime


class Base_Model_Tests(unittest.TestCase):
    """test attrubute """

    def test_BaseModel_save(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        storage = FileStorage()
        storage.all().clear()
        my_dict = my_model.to_dict()
        sve = BaseModel()
        try:
            os.remove("file.json")
        except Exception:
            pass
        sve.save()
        strmodel = f"[{my_model.__class__.__name__}] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(my_model.__class__.__name__, "BaseModel")
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)
        self.assertTrue(isinstance(my_model.created_at, datetime))
        self.assertTrue(isinstance(my_model.updated_at, datetime))
        self.assertEqual(my_dict["id"], my_model.id)
        self.assertEqual(strmodel, my_model.__str__())
        self.assertTrue(os.path.exists("file.json"))

if __name__ == '__main__':
    unittest.main()
