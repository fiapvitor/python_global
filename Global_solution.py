# criamos varias listas onde será armazenado as variaveis necessarias para o funcionamento do sistema
consultas = []
motivoConsultas = []

tratamentos = []
dataTratamento = []
sessoesTratamento = []

medicamentoAlergico = []

numerocarteirinha1 = []
numerocarteirinha2 = []
numerocarteirinha3 = []

pacientesconsultas = []
pacientesTratamentos = []
pacientesMedicamentos = []
crm = 1123 # criamos um crm com um número para que demonstre o funcionamento da entrada do medico credenciado no nosso sistema.


print("OLÁ DOUTOR")
while True:
    x = input('Digite seu CRM: ') 
    x = int(x)

    if x != crm: # caso o crm seja diferente do informado, a validação de dados vai dar como invalida e pedir novamente o crm
        print('CRM não existente!!')
        continue
    else: 
        print("Bem vindo!")
        break
while True:  # caso seja valido o crm, entramos na estrutura de repetição e no nosso menu 
        print('=====>MENU<=====')
        print('1 - Adicionar consulta')
        print('2 - Adicionar tratamento')
        print('3 - Adicionar medicamento alérgico')
        print('4 - Mostrar resultados do dia')
        print('5 - sair')

        escolha = int(input('Escolha uma opção: '))

        if escolha == 1: # onde pegaremos as variaveis necessarias e as armazenaremos nas listas
            numerodaCarteirinha = int(input('Digite o númeroda carteirinha do paciente:'))
            if (numerodaCarteirinha <= 0):  # outra validação de dados é a do número da carteirinha, onde se o número for igual ou menor que zero ele não reconhece e retorna ao menu.
                print('número invalido!!')
                print('Retornando ao menu...')
                continue
            else:
                paciente = input('Digite o nome do paciente: ')
                consulta = input('Qual especialização da consulta: ')
                motivoConsulta = input('Qual o motivo da consulta: ')

                numerocarteirinha1.append(numerodaCarteirinha)
                pacientesconsultas.append(paciente)
                consultas.append(consulta)
                motivoConsultas.append(motivoConsulta)
                #variaveis sendo armazenadas nas listas correspondentes
                print('REGISTRO REALIZADO COM SUCESSO!')

        elif escolha == 2:
            numerodaCarteirinha = int(input('Digite o número da carteirinha do paciente:'))
            if (numerodaCarteirinha <= 0):
                print('número invalido!!')
                print('Retornando ao menu...')
                continue
            else:
                paciente = input('Digite o nome do paciente: ')
                tratamento = input('Digite qual tratamento o paciente realizara: ')
                sessoes = input('Digite a quantidade de sessões a serem realizadas: ')
                data = input('Digite a data de inicio do tratamento: ')

                numerocarteirinha2.append(numerodaCarteirinha)
                pacientesTratamentos.append(paciente)
                tratamentos.append(tratamento)
                sessoesTratamento.append(sessoes)
                dataTratamento.append(data)
                print('REGISTRO REALIZADO COM SUCESSO!')

        elif escolha == 3:
            numerodaCarteirinha = int(input('Digite o númeroda carteirinha do paciente:'))
            if (numerodaCarteirinha <= 0):
                print('número invalido!!')
                print('Retornando ao menu...')
                continue
            else: 
                paciente = input('Digite o nome do paciente: ')
                medicamento= input('Digite o medicamento que o paciente tem alergia: ')
                pacientesMedicamentos.append(paciente)
                numerocarteirinha3.append(numerodaCarteirinha)
                medicamentoAlergico.append(medicamento)
                print('REGISTRO REALIZADO COM SUCESSO!')

        elif escolha == 4:
            consulta_encontrada = False
            tratamento_encontrado = False
            alergia_encontrada = False

            print('Pessoas que passaram em consulta:')
            for i in range(len(numerocarteirinha1)): # na opção 4 entramos em um for para demonstrar em ordem as consultas/ tratamento / medicamentos alergicos que foram registrado hoje
                if numerocarteirinha1[i] > 0: # aqui entramos em um if que pega numerocarteirinha1 que foram registrado, no caso é o numero das consultas e se foi realizada
                    # ele monstra as informações
                    print(f'Número da carteirinha: {numerocarteirinha1[i]} | Nome: {pacientesconsultas[i]} |Consulta: {consultas[i]} | Motivo da consulta: {motivoConsultas[i]}')
                    consulta_encontrada = True

            print('Pessoas que realizaram tratamento:')
            for i in range(len(numerocarteirinha2)):
                if numerocarteirinha2[i] > 0:
                    print(f'Número da carteirinha: {numerocarteirinha2[i]} | Nome: {pacientesTratamentos[i]} | Tratamento: {tratamentos[i]} | Quantas sessões ao total: {sessoesTratamento[i]} | Data de inicio: {dataTratamento[i]}')
                    tratamento_encontrado = True

            print('Pessoas que têm alergia a algum medicamento:')
            for i in range(len(numerocarteirinha3)):
                if numerocarteirinha3[i] > 0:
                    print(f'Número da carteirinha: {numerocarteirinha3[i]} | Nome: {pacientesMedicamentos[i]} |Alergica: {medicamentoAlergico[i]}')
                    alergia_encontrada = True

            if not consulta_encontrada: # caso não seja encontrada ele monstra a mensagem que não foi realizado,, isso para as 3 informações.
                print('Nenhuma pessoa passou em consulta hoje.')

            if not tratamento_encontrado:
                print('Nenhuma pessoa realizou tratamento hoje.')

            if not alergia_encontrada:
                print('Nenhuma pessoa tem alergia a algum medicamento.')
        elif escolha == 5:  # enceramento do programa
            print('Encerrando programa...')
            break     







