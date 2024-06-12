import json
def python_to_json(data):
    return json.dumps(data)

data = {
    "name": "Alice",
    "age": 25,
    "city": "London"
}

json_data = python_to_json(data)
print("JSON representation of the data:")
print(json_data)



def filter_json_by_city(input_file, city):
    with open(input_file, "r") as json_file:
        data = json.load(json_file)
    filtered_data = [item for item in data if item.get("city") == city]
    return filtered_data

input_file = "data.json"
city = "New York"
filtered_data = filter_json_by_city(input_file, city)
print(f"Filtered data based on city '{city}':")
print(filtered_data)


def get_person_name_with_min_age(input_file):
    with open(input_file, "r") as json_file:
        data = json.load(json_file)
    min_age_person = min(data, key=lambda x: x["age"])
    return min_age_person["name"]

input_file = "data.json"
person_name_with_min_age = get_person_name_with_min_age(input_file)
print("Name of the person with the least age:")
print(person_name_with_min_age)

import json

def find_emmas_age(input_file):
    with open(input_file, "r") as json_file:
        data = json.load(json_file)
    for person in data:
        if person["name"] == "Emma":
            return person["age"]
    return None

input_file = "data.json"
emmas_age = find_emmas_age(input_file)
if emmas_age is not None:
    print("Emma's age is:", emmas_age)
else:
    print("Emma's age is not found in the data.")

import json

def find_daniel_hobby(input_file):
    with open(input_file, "r") as json_file:
        data = json.load(json_file)
    for person in data:
        if person["name"] == "Daniel":
            return person.get("hobby", "Hobby not found")
    return "Hobby not found"

input_file = "data.json"
austins_hobby = find_daniel_hobby(input_file)
print("Daniel hobby is:", austins_hobby)

def find_evas_experience(input_file):
    with open(input_file, "r") as json_file:
        data = json.load(json_file)
    for person in data:
        if person["name"] == "Eva":
            return person.get("experience", "Experience not found")
    return "Experience not found"

input_file = "data.json"
evas_experience = find_evas_experience(input_file)
print("Eva's experience is:", evas_experience)


import json

def count_people_with_reading_hobby(input_file):
    with open(input_file, "r") as json_file:
        data = json.load(json_file)
    count = sum(1 for person in data if "hobby" in person and person["hobby"] == "Reading")
    return count

input_file = "data.json"
reading_hobby_count = count_people_with_reading_hobby(input_file)
print("Number of people with 'Reading' hobby:", reading_hobby_count)


def test_count_people_with_reading_hobby(self):
    test_utils_instance = TestUtils()

    input_file = "data.json"
    expected_count = 3  # Assuming there are 3 people with 'Reading' as a hobby in the provided data

    actual_count = count_people_with_reading_hobby(input_file)

    test_utils_instance.yakshaAssert("TestCountPeopleWithReadingHobby", expected_count == actual_count, "functional")

    if expected_count == actual_count:
        print(f"Number of people with 'Reading' hobby: {actual_count}")
        print("TestCountPeopleWithReadingHobby = Passed")
    else:
        print(f"Expected count: {expected_count}, but got: {actual_count}")
        print("TestCountPeopleWithReadingHobby = Failed")

import json

def find_people_from_san_diego(input_file):
    with open(input_file, "r") as json_file:
        data = json.load(json_file)
    people_from_san_diego = [person["name"] for person in data if person.get("city", "") == "San Diego"]
    return people_from_san_diego

input_file = "data.json"
people_from_san_diego = find_people_from_san_diego(input_file)
if people_from_san_diego:
    print("People from San Diego:", ", ".join(people_from_san_diego))
else:
    print("No one is from San Diego in the data.")
