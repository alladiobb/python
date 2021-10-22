from datetime import date, time, datetime, timedelta


def trabalhandoComDate():

    dataAtual = date.today()
    print(dataAtual.strftime('%D'))
    print(dataAtual.strftime('%d/%m/%Y'))
    print(dataAtual.strftime('%A/%B/%Y'))

    data_atual_str = dataAtual.strftime('%D')

    print(dataAtual)
    print(data_atual_str)

def trabalhandoComTime():
    horario = time(hour=15, minute=18, second=30)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario)
    print(type(horario))
    print(horario_str)
    print(type(horario_str))

def trabalhandoComDateTime():
    dataAtual = datetime.now();
    print(dataAtual)
    print(type(dataAtual))
    dataAtualStr = (dataAtual.strftime('%d/%m/%Y %H:%M:%S'))
    print(dataAtualStr)
    print(type(dataAtual))

    print((dataAtual.day))
    print(str)

    tupla = ('Segunda','Terça','Quarta','Quinta','Sexta', 'Sábado','Domingo')
    array = ['Segunda','Terça','Quarta','Quinta','Sexta', 'Sábado','Domingo']
    chaves = {'Segunda','Terça','Quarta','Quinta','Sexta', 'Sábado','Domingo'}
    print(tupla[dataAtual.weekday()])
    print(dataAtual.weekday())

    # print(chaves(6))
    # print(array(6))

    #STRING para TIME
    dataString = '01/01/2020 12:20:19'
    dataConvertida = datetime.strptime(dataString, '%d/%m/%Y %H:%M:%S')
    print(dataConvertida)

    #CONTAS com DATAS
    print(dataConvertida)
    novaData = dataConvertida - timedelta(days=365, hours=10, minutes=10,
                                          seconds=9,milliseconds=15,microseconds=10,
                                          weeks=-1)
    print(novaData)
if __name__ == '__main__':
    # trabalhandoComDate()
    # trabalhandoComTime()
    trabalhandoComDateTime()