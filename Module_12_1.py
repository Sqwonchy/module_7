import  unittest
import les_run

class TestRunner(unittest.TestCase):
    def test_walk(self):
        runner = les_run.Runner("Bob")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance,50)
    def test_run(self):
        runner = les_run.Runner("Jho")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance,100)
    def test_challenge(self):
        runner_1 = les_run.Runner("Dima")
        runner_2 = les_run.Runner("Alex")
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1,runner_2)






if __name__ == "__main__":
    unittest.main()