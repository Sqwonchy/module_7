import unittest
import module_12_2
import module_12_1

def chek_frozen(test_metod):
    def wrapper(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        return test_metod(self)
    return wrapper

test_suite = unittest.TestSuite()

test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))

run_test = unittest.TextTestRunner(verbosity=2)
run_test.run(test_suite)