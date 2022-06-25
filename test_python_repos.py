from python_repos import r,repo_dicts
import unittest

class ResponseTestCase(unittest.TestCase):
    def test_response_code(self):
        response_code=r.status_code
        self.assertEqual(response_code,200)

    def test_repo_number(self):
        self.assertEqual(len(repo_dicts),30)

    if __name__=='__main__':
        unittest.main(argv=['first-arg-is-ignored'], exit=False)

