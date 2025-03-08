from models.Alunos import Aluno
from data.Database import SimpleDB


class AlunoService:
    def __init__(self, db: SimpleDB):
        self.db = db

    def cadastra_aluno(self):
        nome = input('Digite o nome do aluno: ')
        email = input('Digite o email do aluno: ')
        curso = input('Digite o curso do aluno: ')
        aluno = Aluno(nome, email, curso)
        self.db.insert_one(aluno.get_series())

    def lista_alunos(self):
        print('\nAlunos cadastrados:', self.db.read_all())

    def verifica_aluno(self):
        matricula = input('Digite a matrícula do aluno: ')
        aluno = self.db.read_by_mat(matricula)
        print(f'Aluno {aluno}')

    def atualiza_aluno(self):
        matricula = input('Digite a matrícula do aluno que deseja atualizar: ')
        novo_nome = input('Novo nome (deixe em branco para manter o atual): ')
        novo_email = input('Novo email (deixe em branco para manter o atual): ')
        novo_curso = input('Novo curso (deixe em branco para manter o atual): ')

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

    def remove_aluno(self):
        matricula = input('Digite a matrícula do aluno que deseja remover: ')
        self.db.delete(f'matricula == {matricula}')
        print('Aluno removido com sucesso!')
