from models.Alunos import Aluno
from data.Database import SimpleDB
from services.Aluno import AlunoService

def main():
    # Criação do banco de dados simples
    db = SimpleDB()

    # Instancia o serviço de alunos
    aluno_service = AlunoService(db)

    # Cadastrar 3 alunos
    aluno_service.cadastra_aluno(nome="João Silva", email="joao.silva@email.com", curso="GES")
    aluno_service.cadastra_aluno(nome="Maria Oliveira", email="maria.oliveira@email.com", curso="GET")
    aluno_service.cadastra_aluno(nome="Pedro Costa", email="pedro.costa@email.com", curso="GEB")

    # Listar os alunos cadastrados
    print("Alunos cadastrados inicialmente:")
    aluno_service.lista_alunos()

    # Atualizar um aluno
    aluno_service.atualiza_aluno(matricula="GES1", novo_nome="João Silva Júnior", novo_email="joao.silva.jr@email.com")

    # Remover um aluno
    aluno_service.remove_aluno(matricula="GES1")

    # Listar novamente os alunos para verificar remoção
    print("\nAlunos após remoção:")
    aluno_service.lista_alunos()

if __name__ == "__main__":
    main()
