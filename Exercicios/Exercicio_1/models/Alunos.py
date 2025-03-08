import pandas as pd


class Aluno:
    sequencial = 0

    def __init__(self, nome: str, email: str, curso: str):
        self.nome = nome
        self.email = email
        self.curso = curso
        Aluno.sequencial += 1
        self.matricula = f'{curso}{Aluno.sequencial}'

    def get_series(self) -> pd.Series:
        row = {'nome': self.nome, 'email': self.email, 'curso': self.curso, 'matricula': self.matricula}
        return pd.Series(row)
