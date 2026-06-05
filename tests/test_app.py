import unittest
from unittest.mock import patch

from app import main

class TestApp(unittest.TestCase):
    def test_main_prints_message(self):
        with patch("builtins.print") as mock_print:
            main()

        mock_print.assert_called_once_with("immersionmu initialized")

if __name__ == "__main__":
    unittest.main()
