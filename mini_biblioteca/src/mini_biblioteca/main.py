from mini_biblioteca.emprestimos import Emprestimo
from mini_biblioteca.livros import Livro
from mini_biblioteca.usuarios import Usuario

def main() -> None:
    usuario = Usuario("A", "U001")
    livro = Livro("Crime e castigo", "Fiodor Dostoévisk", "L001")

    emprestimo = Emprestimo(livro, usuario)
    print(f"Após empréstimo: disponivel={livro.disponivel}, ativo={emprestimo.ativo}")

    emprestimo.devolver()
    print(f"Após devolução:  disponivel={livro.disponivel}, ativo={emprestimo.ativo}")


if __name__ == "__main__":
    main()