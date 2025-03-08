from data.Database import SimpleDB
from services.Aluno import AlunoService

def main():
    db = SimpleDB()
    aluno_service = AlunoService(db)

    while True:
        print("\nMenu:")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Verificar aluno")
        print("4. Atualizar aluno")
        print("5. Remover aluno")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            aluno_service.cadastra_aluno()
        elif opcao == "2":
            aluno_service.lista_alunos()
        elif opcao == "3":
            aluno_service.verifica_aluno()
        elif opcao == "4":
            aluno_service.atualiza_aluno()
        elif opcao == "5":
            aluno_service.remove_aluno()
        elif opcao == "6":
            db.save_to_csv('data/bd.csv')
            print("Salvando e Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
