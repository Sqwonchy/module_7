import unittest
from runner_and_tournament import Runner, Tournament
from unittest import skipIf


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        is_frozen = True

    def setUp(self):
        self.usain = Runner("Усейн", 10)
        self.andrei = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(value)

    @skipIf(lambda: TournamentTest.is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_1(self):
        number = 1
        tour = Tournament(90, self.usain, self.nik)
        finisher = tour.start()
        self.all_results = {place: runner.name for place, runner in finisher.items()}
        self.assertEqual(self.all_results[max(self.all_results)], "Ник")
        TournamentTest.all_results[number] = self.all_results

    @skipIf(lambda: TournamentTest.is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_2(self):
        number = 2
        tour = Tournament(90, self.andrei, self.nik)
        finisher = tour.start()
        self.all_results = {place: runner.name for place, runner in finisher.items()}
        self.assertEqual(self.all_results[max(self.all_results)], "Ник")
        TournamentTest.all_results[number] = self.all_results

    @skipIf(lambda: TournamentTest.is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_3(self):
        number = 3
        tour = Tournament(90, self.usain, self.andrei, self.nik)
        finisher = tour.start()
        self.all_results = {place: runner.name for place, runner in finisher.items()}
        self.assertEqual(self.all_results[max(self.all_results)], "Ник")
        TournamentTest.all_results[number] = self.all_results
