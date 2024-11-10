import logging
import unittest
import rt_with_exceptions

logging.basicConfig(filename="runner_tests.log",
                    filemode="w",
                    level=logging.INFO,
                    encoding="utf-8",
                    format="%(asctime)s | %(levelname)s |%(message)s| %(name)s | %(module)s | %(filename)s"
                           " | line: %(lineno)d | %(funcName)s"
                    )



class RunnerTest(unittest.TestCase):
    def setUp(self):
        logging.info(f"запуск {self._testMethodName} ")
    def tearDown(self):
        logging.info(f"окончание {self._testMethodName} ")
    def test_walk(self):
        try:
            runner = rt_with_exceptions.Runner("Bob", speed=-5)
            for i in range(10):
                runner.walk()
            logging.info('"test_walk" выполнен успешно')
            self.assertEqual(runner.distance, 50)
        except ValueError as e :
            logging.error(f"Неверная скорость для Runner {e}")
            return

    def test_run(self):
        try:
            runner = rt_with_exceptions.Runner(56)
            for i in range(10):
                runner.run()
            logging.info('"test_run" выполнен успешно')
            self.assertEqual(runner.distance, 100)
        except TypeError as e:
            logging.error(f"Неверный тип данных для объекта Runner {e}")
            return


    def test_challenge(self):
        runner_1 = rt_with_exceptions.Runner("Dima")
        runner_2 = rt_with_exceptions.Runner("Alex")
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1, runner_2)




if __name__ == "__main__":
    unittest.main()
