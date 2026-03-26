import unittest
import datetime as dt

from task import Task

class TestTask(unittest.TestCase):
    def test_task_basic(self):
        duration = dt.timedelta(30)
        matches = Task("Polish Boots", duration)
        self.assertEqual("Polish Boots", matches.name)
        due_date = dt.date.today() + duration
        self.assertEqual(due_date, matches.due)

if __name__ == "__main__":
    unittest.main()