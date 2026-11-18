from mini_biblioteca.emprestimos import Emprestimo
from mini_biblioteca.livros import Livro
from mini_biblioteca.usuarios import Usuario

def test_instanciar_livro():
    livro = Livro("Crime e castigo", "Fiodor Dostoiévisk", "L001")
    assert livro.titulo == "Crime e castigo"
    assert livro.autor == "Fiodor Dostoiévisk"
    assert livro.codigo == "L001"
    assert livro.disponivel is True