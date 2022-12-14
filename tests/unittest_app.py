import json
import unittest
import requests

class TestStringMethods(unittest.TestCase):
    def test_get(self):
        response=requests.get("http://localhost:5000")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json()["result"]["content"],"good morning")

    def test_get_users(self):
        res = requests.get("http://localhost:5000/users/all")
        assert res.status_code == 200
        res_users = res.json()["result"]["users"]
        assert len(res_users) == 4
        assert res_users[0]["name"] == "Aria"

    def tests_get_users_with_team(self):
        res = requests.get("http://localhost:5000/users?team=LWB")
        assert res.status_code == 200

        res_users = res.json()["result"]["users"]
        assert len(res_users) == 3
        assert res_users[1]["name"] == "Tim"

    def test_get_user_id(self):
        res = requests.get("http://localhost:5000/users/1")
        assert res.status_code == 200

        res_user = res.json()["result"]["user"]
        assert res_user["name"] == "Aria"
        assert res_user["age"] == 19

    def test_insert_user(self):
        info={"name":"Esty","age":20,"team":"LWB"}
        res=requests.post("http://localhost:5000/users",json=info)
        assert res.status_code==201

    def test_update(self):
        info={"age":25}
        res=requests.put("http://localhost:5000/users/2",json=info)
        assert res.status_code==200
        resUser=res.json()["result"]["Updated user"]
        assert resUser["age"]==25

    def test_delete(self):
        res=requests.delete("http://localhost:5000/users/1")
        assert res.status_code==200

    def test_mirror(self):
        res = requests.get("http://localhost:5000/mirror/Tim")
        assert res.status_code == 200
        assert res.json()["result"]["name"] == "Tim"


if __name__ == '__main__':
    unittest.main()