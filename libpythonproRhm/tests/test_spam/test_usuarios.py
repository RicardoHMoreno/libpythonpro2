from libpythonproRhm.spam.modelos import Usuario


def test_savar_usuario(sessao):
    usuario = Usuario(nome='Renzo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)

def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Renzo'), Usuario(nome='Luciano')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()



