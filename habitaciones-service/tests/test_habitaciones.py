from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["service"] == "habitaciones"

def test_crud_habitacion():
    # crear
    r = client.post("/habitaciones/", json={"numero": "101", "tipo":"doble", "precio_noche": 120000})
    assert r.status_code == 201
    data = r.json()
    assert data["numero"] == "101"
    hid = data["id"]

    # listar
    r2 = client.get("/habitaciones/")
    assert r2.status_code == 200
    assert any(h["numero"] == "101" for h in r2.json())

    # cambiar estado
    r3 = client.patch(f"/habitaciones/{hid}/estado", params={"estado":"ocupada"})
    assert r3.status_code == 200
    assert r3.json()["estado"] == "ocupada"

    # borrar
    r4 = client.delete(f"/habitaciones/{hid}")
    assert r4.status_code == 204
