import pytest

from mini_biblioteca.emprestimos import Emprestimo
from mini_biblioteca.livros import Livro
from mini_biblioteca.usuarios import Usuario

def test_livro_novo_comeca_disponivel():
    livro = Livro("Crime e castigo", "Fiodor Dostoiévisk", "L001")
    assert livro.disponivel is True
