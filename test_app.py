import pytest
# pytest automatically injects fixtures
# that are defined in conftest.py
# in this case, client is injected
def test_index(client):
    print(client,'client')
    res = client.get("/")
    assert res.status_code == 200
    assert res.json["result"]["content"] == "hello world!"


def test_mirror(client):
    res = client.get("/mirror/Tim")
    assert res.status_code == 200
    assert res.json["result"]["name"] == "Tim"


def test_get_users(client):
    res = client.get("/users/all")
    assert res.status_code == 200

    res_users = res.json["result"]["users"]
    assert len(res_users) == 4
    assert res_users[0]["name"] == "Aria"


def tests_get_users_with_team(client):
    res = client.get("/users?team=LWB")
    assert res.status_code == 200

    res_users = res.json["result"]["users"]
    assert len(res_users) == 2
    assert res_users[1]["name"] == "Tim"


def test_get_user_id(client):
    res = client.get("/users/1")
    assert res.status_code == 200

    res_user = res.json["result"]["user"]
    assert res_user["name"] == "Aria"
    assert res_user["age"] == 19

def test_insert_user(client):
    info={"name":"Esty","age":20,"team":"LWB"}
    res=client.post("http://localhost:5000/users",json=info)
    assert res.status_code==201

def test_update(client):
    info={"age":25}
    res=client.put("http://localhost:5000/users/2",json=info)
    assert res.status_code==200
    resUser=res.json["result"]["Updated user"]
    assert resUser["age"]==25

def test_delete(client):
    res=client.delete("http://localhost:5000/users/1")
    assert res.status_code==200

