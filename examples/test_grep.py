import unittest
import os

from files import grep


class TestGrep(unittest.TestCase):
    filepath = "file.txt"

    @classmethod
    def setUpClass(cls):
        lines = ["bye", "hello world", "goodbye", "Jane, hello"]
        with open(cls.filepath, "w") as f:
            for line in lines:
                f.write(f"{line}\n")

    def test_lines_match(self):
        returned_lines = grep("hello", self.filepath)

        self.assertIsInstance(returned_lines, list)
        self.assertEqual(["hello world\n",  "Jane, hello\n"], returned_lines)

    def test_lines_do_not_match(self):
        returned_lines = grep("hi", self.filepath)

        self.assertIsInstance(returned_lines, list)
        self.assertEqual(0, len(returned_lines))

    def test_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            grep("hi", "nonexistent.txt")

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.filepath)
