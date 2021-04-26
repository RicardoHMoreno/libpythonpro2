import pytest

from libpythonproRhm.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador=Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['foo@bar.com.br', 'renzo@python.pro.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'ricardohm007@gmail.com',
        'Cursos pythom pro',
        'Primeira turma aberta!'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'renzo']
)
def test_remetente_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'ricardohm007@gmail.com',
            'Cursos pythom pro',
            'Primeira turma aberta!'
        )
