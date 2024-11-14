from aluno import Aluno

sistema = Aluno()

def main():
  while True:
        print("\nEscolha uma opção:")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            name = input('Digite o nome do aluno: ')
            age = input('Digite a idade do aluno: ')
            course = input('Digite o curso do aluno: ')
            sistema.register_student(name=name, age=age, course=course)

        elif opcao == '2':
            sistema.list_students()

        elif opcao == '3':
            student_id = int(input("Digite o ID do aluno que deseja atualizar: "))
            name = input("Novo nome (ou Enter para manter o atual): ")
            age = input("Nova idade (ou Enter para manter o atual): ")
            course = input("Novo curso (ou Enter para manter o atual): ")

            sistema.update_student(student_id, name=name if name else None, age=age if age else None, course=course if course else None)

        elif opcao == '4':
            student_id = int(input("Digite o ID do aluno que deseja excluir: "))
            sistema.delete_student(student_id)

        elif opcao == '5':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()