from app.app import Usuario

def test_actualizar_peso():
    usuario = Usuario("Test", 80.0)
    usuario.actualizar_peso(75.0)
    assert usuario.get_peso() == 75.0