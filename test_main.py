# test_main.py
import unittest
from main import hello_github_action

class TestHelloGitHubAction(unittest.TestCase):
    def test_hello_github_action(self):
        result = hello_github_action()
        self.assertEqual(result, "Hello GitHub Actions")

if __name__ == '__main__':
    unittest.main()
