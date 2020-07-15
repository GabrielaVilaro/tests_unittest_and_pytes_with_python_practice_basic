import pytest

class TestClass():
    @pytest.fixture()
    def configuracion(self):
        url = 'https://www.google.com.ar/?hl=es-419'
        nombre = 'Google'
        estado = 'Activo'
        return url, nombre, estado

    @pytest.fixture()
    def cierre(self):
        print('Se terminó la ejecución')

    def test_1(self, configuracion, cierre):
        assert 'https://www.google.com.ar/?hl=es-419' in configuracion

    def test_2(self, configuracion, cierre):
        assert 'Google' in configuracion

    def test_3(self, configuracion, cierre):
        assert 'Activo' in configuracion