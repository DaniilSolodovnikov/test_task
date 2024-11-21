import unittest
from solution2 import get_animal_count_by_letter


class TestGetAnimalCountByLetter(unittest.TestCase):
    def test_animal_count_in_file(self):
        get_animal_count_by_letter()  # Выполните функцию, чтобы создать файл
        with open("beasts.csv", "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            expected_letters = ["А", "Б", "В"]
            for row in reader:
                letter = row[0]
                if letter in expected_letters:
                    self.assertNotEqual(int(row[1]), 0, f"Количество животных для буквы {letter} равно 0")


if __name__ == '__main__':
    unittest.main()