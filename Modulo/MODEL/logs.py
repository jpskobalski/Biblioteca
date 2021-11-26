import datetime, os

program_location = os.path.dirname(os.path.abspath(__file__))
logs = os.path.join(program_location, 'log.txt')

def logregister(funcion):
    def registrar(*args):
        logfile = open(logs, 'a+')
        hora = str(datetime.datetime.now())
        dato = funcion(*args)
        if dato == None:
            return registrar
        else:
            if dato == 'alta':
                logfile.write('Se han subido un titulo a la base - %s \n' %(hora))
            if dato == 'baja':
                logfile.write('Se han eliminado un ID de la base  - %s \n' %(hora))
            if dato == 'modi':
                logfile.write('Se han modificado un ID en la base - %s \n' %(hora))
        logfile.close()
    return registrar

@logregister
def crear_log(abmc):
    if abmc == 'alta':
        return 'alta'
    if abmc == 'baja':
        return 'baja'
    if abmc == 'modi':
        return 'modi'
    else:
        return None