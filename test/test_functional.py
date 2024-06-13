import unittest
from python_conversion import *
from test.TestUtils import TestUtils

class PythonConversionTests(unittest.TestCase):

    def setUp(self):
        self.input_file = "data.json"
        self.test_utils_instance = TestUtils()

    def test_python_to_json(self):
        data = {"name": "Alice", "age": 25, "city": "London"}
        expected_output = '{"name": "Alice", "age": 25, "city": "London"}'
        actual_output = python_to_json(data)
        self.test_utils_instance.yakshaAssert("TestPythonToJson", expected_output == actual_output, "functional")
        if expected_output == actual_output:
            print("TestPythonToJson = Passed")
        else:
            print("TestPythonToJson = Failed")

    def test_filter_json_by_city(self):
        city = "New York"
        expected_filtered_data = [{'name': 'John', 'age': 30, 'city': 'New York', 'salary': 60000, 'experience': 5, 'networth': 150000,
              'hobby': 'Reading'}]

        filtered_data = filter_json_by_city(self.input_file, city)
        self.test_utils_instance.yakshaAssert("TestFilterJsonByCity", expected_filtered_data == filtered_data, "functional")
        if expected_filtered_data == filtered_data:
            print("TestFilterJsonByCity = Passed")
        else:
            print("TestFilterJsonByCity = Failed")

    def test_get_person_name_with_min_age(self):
        expected_person_name = "Jackson"
        person_name_with_min_age = get_person_name_with_min_age(self.input_file)
        self.test_utils_instance.yakshaAssert("TestGetPersonNameWithMinAge", expected_person_name == person_name_with_min_age, "functional")
        if expected_person_name == person_name_with_min_age:
            print("TestGetPersonNameWithMinAge = Passed")
        else:
            print("TestGetPersonNameWithMinAge = Failed")

    def test_find_emmas_age(self):
        expected_emmas_age = 35
        emmas_age = find_emmas_age(self.input_file)
        self.test_utils_instance.yakshaAssert("TestFindEmmasAge", expected_emmas_age == emmas_age, "functional")
        if expected_emmas_age == emmas_age:
            print("TestFindEmmasAge = Passed")
        else:
            print("TestFindEmmasAge = Failed")

    def test_find_daniel_hobby(self):
        expected_daniel_hobby = "Chess"
        daniel_hobby = find_daniel_hobby(self.input_file)
        self.test_utils_instance.yakshaAssert("TestFindDanielsHobby", expected_daniel_hobby == daniel_hobby, "functional")
        if expected_daniel_hobby == daniel_hobby:
            print("TestFindDanielsHobby = Passed")
            print("Daniel hobby is:", daniel_hobby)
        else:
            print("TestFindDanielsHobby = Failed")

    def test_find_evas_experience(self):
        expected_evas_experience = 5
        evas_experience = find_evas_experience(self.input_file)
        self.test_utils_instance.yakshaAssert("TestFindEvasExperience", expected_evas_experience == evas_experience, "functional")
        if expected_evas_experience == evas_experience:
            print("TestFindEvasExperience = Passed")
            print("Eva's experience is:", evas_experience)
        else:
            print("TestFindEvasExperience = Failed")
            print("Eva's experience is:", evas_experience)

    def test_find_people_from_san_diego(self):
        expected_people_from_san_diego = ["Charlotte"]
        people_from_san_diego = find_people_from_san_diego(self.input_file)
        self.test_utils_instance.yakshaAssert("TestFindPeopleFromSanDiego", expected_people_from_san_diego == people_from_san_diego, "functional")
        if expected_people_from_san_diego == people_from_san_diego:
            print("TestFindPeopleFromSanDiego = Passed")
            print("People from San Diego:", ", ".join(people_from_san_diego))
        else:
            print("TestFindPeopleFromSanDiego = Failed")
            print("No one is from San Diego in the data.")

    def test_count_people_with_reading_hobby(self):
        expected_count = 2
        actual_count = count_people_with_reading_hobby(self.input_file)
        self.test_utils_instance.yakshaAssert("TestCountPeopleWithReadingHobby", expected_count == actual_count, "functional")
        if expected_count == actual_count:
            print(f"Number of people with 'Reading' hobby: {actual_count}")
            print("TestCountPeopleWithReadingHobby = Passed")
        else:
            print(f"Expected count: {expected_count}, but got: {actual_count}")
            print("TestCountPeopleWithReadingHobby = Failed")

if __name__ == '__main__':
    unittest.main()
