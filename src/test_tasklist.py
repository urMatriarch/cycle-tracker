import unittest

from tasklist import TaskList
from task import Task

class TestTaskList(unittest.TestCase):
    def test_tasklist_basic(self):
        matches = TaskList()
        self.assertEqual(0, matches.length)
        self.assertEqual([], matches.tasks)

    def test_add_and_remove_task(self):
        matches = TaskList()
        test_case = Task("Polish Boots")
        matches.add_task(test_case)
        self.assertEqual(1, matches.length)
        self.assertEqual("Polish Boots", matches.tasks[0].name)
        matches.remove_task(test_case)
        self.assertEqual(0, matches.length)
        self.assertEqual([], matches.tasks)

    def test_remove_task_fail(self):
        matches = TaskList()
        test_case = Task("Polish Boots")
        with (self.assertRaises(Exception)):
            matches.remove_task(test_case)
        matches.add_task(test_case)
        with (self.assertRaises(Exception)):
            matches.remove_task("This is not a Task!")

    def test_add_non_task_fail(self):
        matches = TaskList()
        test_case = "This is a not a Task!"
        with (self.assertRaises(Exception)):
            matches.add_task(test_case)

if __name__ == "__main__":
    unittest.main()