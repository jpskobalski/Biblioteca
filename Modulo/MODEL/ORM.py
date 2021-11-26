from peewee import *
import os, datetime

program_location = os.path.dirname(os.path.abspath(__file__))
db = SqliteDatabase(os.path.join(program_location,'nivel_avanzado.db'))

class Noticia(Model):
    titulo = CharField(unique = True)
    descripcion = TextField()
    fecha = DateField(default=datetime.datetime.today().strftime('%Y-%m-%d'))
    estado_de_publicacion = BooleanField(default=True)
    class Meta:
        database = db
    def __str__(self):
        return 'El titulo ingresado es: ' + str(self.titulo)

db.connect()
db.create_tables([Noticia])