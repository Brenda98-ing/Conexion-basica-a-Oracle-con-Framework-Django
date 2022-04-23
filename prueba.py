# oracle library
import cx_Oracle



DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
    }
}

class Transacction:


    db_config = DATABASES['default']
    dns = cx_Oracle.makedsn(db_config['HOST'], 1521, service_name=db_config['NAME'])

    connection = cx_Oracle.connect(user=db_config['USER'], password=db_config['PASSWORD'],
                       dsn=dns, encoding="UTF-8")


    def consulta(self):
        try:
            # crea cursor de la conexion
            cur = self.connection.cursor()

            # establecemos query
            query = f"""
                SELECT * FROM TP_ACCOUNT
            """
        

            for row in cur.execute(query):
                print(row)

        except cx_Oracle.Error as error:
            print(error)

        print("Ejecutado")



Transacction().consulta()
