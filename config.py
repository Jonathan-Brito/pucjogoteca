SECRET_KEY = 'aluno'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(

        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = '420024Jojo.,',
        servidor = 'localhost',
        database = 'pucjogoteca'
    )
