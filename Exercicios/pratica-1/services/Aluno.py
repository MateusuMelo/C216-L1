from models.Alunos import Aluno
from data.Database import SimpleDB


class AlunoService:
    def __init__(self, db: SimpleDB):
        self.db = db

    def cadastra_aluno(self, nome: str, email: str, curso: str):
        aluno = Aluno(nome, email, curso)
        self.db.insert_one(aluno.get_series())

    def lista_alunos(self):
        print('\nAlunos cadastrados:', self.db.read_all())

    def verifica_aluno(self, matricula: str):
        aluno = self.db.read_by_mat(matricula)
        print(f'Aluno {aluno}')

    def atualiza_aluno(self, matricula: str, novo_nome: str = '', novo_email: str = '', novo_curso: str = ''):
        update_data = {}
        if novo_nome:
            update_data['nome'] = novo_nome
        if novo_email:
            update_data['email'] = novo_email
        if novo_curso:
            update_data['curso'] = novo_curso

        if update_data:
            self.db.update(f'matricula == {matricula}', update_data)
            print('Aluno atualizado com sucesso!')
        else:
            print('Nenhuma alteração feita.')

    def remove_aluno(self, matricula: str):
        self.db.delete(matricula)
        print('Aluno removido com sucesso!')
