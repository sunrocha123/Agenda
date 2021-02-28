class Agenda(object):

    agenda = []

    def armazenaPessoa(self, nome, idade, altura):
        auxiliar = {}

        if len(self.agenda) < 10:
            auxiliar['nome'] = nome
            auxiliar['idade'] = idade
            auxiliar['altura'] = altura
            self.agenda.append(auxiliar)
        else:
            return 0
        pass

    def removePessoa(self, nome):
        for pessoa in self.agenda:
            if pessoa['nome'] == nome:
                self.agenda.remove(pessoa)
                return 1
        return 0
        pass

    def buscaPessoa(self, nome):
        for i in range(len(self.agenda)):
            if self.agenda[i]['nome'] == nome:
                return f'O(a) {nome} está na posição {i + 1} da agenda.'
        return 0
        pass

    def imprimeAgenda(self):
        for i in range(len(self.agenda)):
            print(f"{self.agenda[i]['nome']},"
                  f"{self.agenda[i]['idade']},"
                  f"{self.agenda[i]['altura']}")
        pass

    def imprimePessoa(self, index):
        for i in range(len(self.agenda)):
            if i == (index - 1):
                print(f"{self.agenda[i]['nome']},"
                      f"{self.agenda[i]['idade']},"
                      f"{self.agenda[i]['altura']}\n")
                return 1
        return 0
        pass


if __name__ == '__main__':

    def menu():
        print(f'MENU\n'
              f'1. Armazenar pessoa\n'
              f'2. Remover pessoa\n'
              f'3. Buscar pessoa\n'
              f'4. Imprimir agenda\n'
              f'5. Imprimir pessoa\n'
              f'6. Sair\n')

    print(f'--------------------\n'
          f'AGENDA\n'
          f'--------------------\n'
          f'Bem-vindo a nossa ferramenta de Agenda :)\n')
    while True:
        menu()

        while True:
            escolha_opcao = int(input('Digite uma opção (1 - 6): '))
            if int(escolha_opcao) <= 0 or int(escolha_opcao) > 6:
                print('Opção inválida! Por gentileza, digite novamente.')
            else:
                print()
                break

        objeto_Agenda = Agenda()

        if escolha_opcao == 1:
            #Bloco para testar o limite de usuários na lista

            '''nomes = [['Judson',19,1.9],
                     ['Ana',38,1.56],
                     ['Joao',12,1.6],
                     ['Caroline',16,1.78],
                     ['Railde',78,1.67],
                     ['Izabel',77,1.65],
                     ['Joel',43,1.78],
                     ['Nilma',40,1.8],
                     ['Edmilson',43,1.83],
                     ['Neuma',45,1.56]]

            for i in range (len(nomes)):
                objeto_Agenda.armazenaPessoa(nomes[i][0],nomes[i][1],nomes[i][2])'''

            nome = input('Digite o nome: ').title().strip()
            idade = int(input('Digite a idade: '))
            altura = float(input('Digite a altura: '))
            cadastro = objeto_Agenda.armazenaPessoa(nome, idade, altura)
            if cadastro == 0:
                print('Limite de cadastro atingido. Não será possível cadastrar esse usuário :(')
            else:
                print('Dados armazenados com sucesso na agenda! :)\n')
            pass
        elif escolha_opcao == 2:
            nome = input('Digite o nome: ').title().strip()
            remocao = objeto_Agenda.removePessoa(nome)
            if remocao == 0:
                print('Usuário não localizado na agenda :(\nPor gentileza, cadastrá-lo na agenda, para posteriormente removê-lo.\n')
            else:
                print('Usuário removido da agenda com sucesso! :)\n')
            pass
        elif escolha_opcao == 3:
            nome = input('Digite o nome: ').title().strip()
            buscaPessoa = objeto_Agenda.buscaPessoa(nome)
            if buscaPessoa == 0:
                print('Usuário não localizado na agenda :(')
            else:
                print(f'{buscaPessoa}\n')
            pass
        elif escolha_opcao == 4:
            objeto_Agenda.imprimeAgenda()
            print('')
            pass
        elif escolha_opcao == 5:
            posicao = int(input('Digite a posição da pessoa na agenda: '))
            posicao_pessoa = objeto_Agenda.imprimePessoa(posicao)
            if posicao_pessoa == 0:
                print('Usuário não localizado na agenda :(')
            pass
        else:
            print('Obrigado por usar nossa ferramenta!!!! :)')
            break

        while True:
            validar_uso = input('Deseja realizar outra operação (S/N)? ').title().strip()
            if validar_uso != 'S' and validar_uso != 'Sim' and validar_uso != 'N' and validar_uso != 'Não' and validar_uso != 'Nao':
                print('Opção inválida! Por gentileza, digite novamente')
            else:
                break

        if validar_uso == 'N' or validar_uso == 'Não' or validar_uso == 'Nao':
            print('Obrigado por usar nossa ferramenta!!!! :)')
            break
        print()