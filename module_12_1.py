import  unittest
import les_run

class RunnerTest(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.is_frozen = False

    # @classmethod
    # def setUpClass(cls):
    #     cls.is_frozen = False

    @unittest.skipUnless(self.is_frozen, "fdfdfd")
    def test_walk(self):
        runner = les_run.Runner("Bob")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance,50)
    # @unittest.skipIf(RunnerTest.is_frozen , "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = les_run.Runner("Jho")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance,100)
    # @unittest.skipIf(RunnerTest.is_frozen , "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner_1 = les_run.Runner("Dima")
        runner_2 = les_run.Runner("Alex")
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1,runner_2)






if __name__ == "__main__":
    unittest.main()