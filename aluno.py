import pandas as pd
import os

class Aluno:

    def __init__(self, excel='alunos.xlsx'):
        self.excel = excel

        if os.path.exists(excel):
            self.df = pd.read_excel(self.excel)
        else:
            self.df = pd.DataFrame(columns=['ID', 'Nome', 'Idade', 'Curso'])


    def save(self):
        self.df.to_excel(self.excel, index=False)


    def register_student(self, name, age, course):
        new_id = len(self.df) + 1
        new_student = {'ID': new_id, 'Nome': name, 'Idade': age, 'Curso': course}

        self.df = pd.concat([self.df, pd.DataFrame([new_student])], ignore_index=True)
        self.save()
        print(f"Aluno '{name}' cadastrado com sucesso!")


    def list_students(self):
      if self.df.empty:
        print("Nenhum aluno foi cadastrado ainda")
      else:
        print("Lista de Alunos:")
        print(self.df)


    def update_student(self, student_id, name=None, age=None, course=None):

        if student_id in self.df['ID'].values:
            if name:
                self.df.loc[self.df['ID'] == student_id, 'Nome'] = name
            if age:
                self.df.loc[self.df['ID'] == student_id, 'Idade'] = age
            if course:
                self.df.loc[self.df['ID'] == student_id, 'Curso'] = course
            self.save()
            print(f"Aluno com ID {student_id} atualizado com sucesso!")
        else:
            print("Aluno não encontrado.")


    def delete_student(self, student_id):

        if student_id in self.df['ID'].values:
            self.df = self.df[self.df['ID'] != student_id]
            self.save()
            print(f"Aluno com ID {student_id} excluído com sucesso!")
        else:
            print("Aluno não encontrado.")