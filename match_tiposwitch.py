mes_nacimiento = 'abril'

match mes_nacimiento:
    case 'enero' | 'febrero' | 'marzo':
        print("Naciste en verano")
    case 'abril' | 'mayo' | 'junio':
        print("Naciste en otono")
    case 'julio' | 'agosto' | 'septiembre':
        print("Naciste en invierno")
    case 'octubre' | 'noviembre' | 'diciembre':
        print("Naciste en primavera")
    case _:
        print("Mes no válido")


dia = 3

match dia:
    case 1:
        print("Hoy es Lunes")
    case 2:
        print("Hoy es Martes")
    case 3:
        print("Hoy es Miércoles")
    case _:
        print("No coincide con ninguna de las anteriores")