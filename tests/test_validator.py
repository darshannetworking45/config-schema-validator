import unittest
from src.validator import NetworkSchemaValidator

class TestSchemaValidator(unittest.TestCase):
    def test_valid_data(self):
        data = {
            "hostname": "sw-access-01",
            "management_ip": "192.0.2.10",
            "role": "access",
            "site": "NYC",
            "vlans": [10, 20, 30]
        }
        errors = NetworkSchemaValidator.validate_device_vars(data)
        self.assertEqual(len(errors), 0)

    def test_invalid_data(self):
        data = {
            "hostname": "sw-access-01",
            "management_ip": "bad_ip_address",
            "vlans": [10, 5000]
        }
        errors = NetworkSchemaValidator.validate_device_vars(data)
        self.assertGreaterEqual(len(errors), 3)

if __name__ == "__main__":
    unittest.main()
