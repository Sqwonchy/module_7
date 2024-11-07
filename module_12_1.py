import unittest
import les_run

def chek_frozen(test_metod):
    def wrapper(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        return test_metod(self)

    return wrapper



class RunnerTest(unittest.TestCase):
    is_frozen = False

    @chek_frozen
    def test_walk(self):
        if self.is_frozen:
            self.skipTest("Замароженно")
        runner = les_run.Runner("Bob")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @chek_frozen
    def test_run(self):
        runner = les_run.Runner("Jho")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @chek_frozen
    def test_challenge(self):
        runner_1 = les_run.Runner("Dima")
        runner_2 = les_run.Runner("Alex")
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1, runner_2)


if __name__ == "__main__":
    unittest.main()
