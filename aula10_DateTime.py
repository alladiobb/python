from datetime import date, time


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
    print(horario)

if __name__ == '__main__':
    trabalhandoComDate()