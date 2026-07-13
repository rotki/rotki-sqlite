import sys
import sysconfig
import unittest

import rsqlite


class RsqliteTestCase(unittest.TestCase):
    def test_in_memory_database(self) -> None:
        with rsqlite.connect(":memory:") as connection:
            result = connection.execute("SELECT 42").fetchone()

        self.assertEqual(result, (42,))

    def test_import_does_not_enable_gil(self) -> None:
        if sysconfig.get_config_var("Py_GIL_DISABLED"):
            self.assertFalse(sys._is_gil_enabled())


if __name__ == "__main__":
    unittest.main()
