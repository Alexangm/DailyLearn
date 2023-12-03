from mysql.connector import connect, ClientFlag
class Database:
    db=None
    @staticmethod
    def ConnectDatabase():
        
        Database.db = connect(
            host="english.mysql.database.azure.com",
            user="alexgm",
            password="3ngl1sh4PP",
            database="db_english",
            client_flags=ClientFlag.SSL,
            ssl_ca="digicertglobalrootg2.crt.pem"
        )
        cursor =  Database.db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users(id_user INTEGER PRIMARY KEY AUTO_INCREMENT, email VARCHAR(255) NOT NULL, name text NOT NULL, password VARCHAR(255) NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS words(id_word INTEGER PRIMARY KEY AUTO_INCREMENT, word VARCHAR(255) NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS profile(id_user INTEGER, id_word INTEGER, fl_conhecia INTEGER, fl_favorita integer, fl_sabia integer DEFAULT 0)")
        cursor.execute("CREATE TABLE IF NOT EXISTS palavrasPortugues(id_word INTEGER PRIMARY KEY AUTO_INCREMENT, word VARCHAR(255) NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS palavrasQuiz(id_user INTEGER, id_word INTEGER, fl_acerto INTEGER)")
        Database.db.commit()
        print('conectou lindamente')
        print("Conectado com sucesso!")

    @staticmethod
    def droppalavrasQuiz():
        sql = "DROP TABLE palavrasQuiz"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        Database.db.commit()
        print("dropado com sucesso")
        return 1


    @staticmethod
    def updateWord(id_word, word):
        sql = "UPDATE words SET word = %s where id_word = %s"
        val = (f"{word}", f"{id_word}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()
        return 1
    
    @staticmethod
    def insertdata(email, name, password):
        sql = "INSERT INTO users (email, name, password) VALUES (%s, %s, %s)"
        val = (f"{email}", f"{name}", f"{password}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()


    @staticmethod
    def isValid(email):
        sql = "SELECT * FROM users WHERE email=(%s)"
        val = (f"{email}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        print("aqui o result", result)
        if(result):
            return False
        else:
            return True


    @staticmethod
    def isExist(email, password):
        sql = "SELECT * FROM users WHERE email=%s and password = %s"
        val = (f"{email}", f"{password}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if(result):
            return True
        else:
            return False
        

    @staticmethod
    def insertWord(word):
        sql = "INSERT INTO words (word) VALUES (%s)"
        val = (f"{word}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()


    def linkWordWithProfile(id_word, id_user, fav):
        sql = "SELECT * FROM profile WHERE id_user=%s and id_word = %s"
        val = (f"{id_user}", f"{id_word}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if(result):
            sql = "UPDATE profile SET fl_favorita = %s where id_word = %s and id_user = %s"
            val = (f"{fav}", f"{id_word}", f"{id_user}")
            cursor = Database.db.cursor()
            cursor.execute(sql, val)
            Database.db.commit()
            return 'result true'
        else:
            sql = "INSERT INTO profile (id_user, id_word, fl_conhecia, fl_favorita) VALUES (%s, %s, 0, %s)"
            cursor = Database.db.cursor()
            cursor.execute(sql, val)
            Database.db.commit()
            return 'result false'


    @staticmethod
    def insertQuiz(id_user, id_word, fl_acerto):
        sql = "SELECT * FROM palavrasQuiz WHERE id_user=%s and id_word = %s"
        val = (f"{id_user}", f"{id_word}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if(result):
            return 0
        else:
            sql = "INSERT INTO palavrasQuiz (id_user, id_word, fl_acerto) VALUES (%s, %s, %s)"
            val = (f"{id_user}", f"{id_word}", f"{fl_acerto}")
            print('DENTRO DO BD = ',sql, val)
            cursor = Database.db.cursor()
            cursor.execute(sql, val)
            Database.db.commit()
            return 1


    @staticmethod
    def insertPalavraPortugues(palavra):
        sql = "INSERT INTO palavrasPortugues (word) VALUES (%s)"
        val = (f"{palavra}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()


    @staticmethod
    def selectPalavraPortugues(id):
        sql = f"SELECT word FROM palavrasPortugues where id_word = %s"
        val = (f"{id}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        return cursor.fetchall()[0][0]


    # retorna a palavra pelo id
    @staticmethod
    def selectWord(id):
        sql = "SELECT word FROM words where id_word = %s"
        val = (f"{id}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        return cursor.fetchall()
    

    @staticmethod
    def selectWordById(id):
        sql = "SELECT word FROM words where id_word = %s"
        val = (f"{id}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        return cursor.fetchall()[0][0]

    @staticmethod
    def selectAllWords():
        sql = "SELECT * FROM words"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    
    @staticmethod
    def selectAllPortugueseWords():
        sql = "SELECT * FROM palavrasPortugues"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @staticmethod
    def changeUser(id_user, name, password):
        sql = "UPDATE users SET password = %s, name = %s where id_user = %s"
        val = (f"{password}", f"{name}", f"{id_user}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()
        return 'result true'
    

    @staticmethod
    def changePassword(id_user, password):
        sql = "UPDATE users SET password = %s where id_user = %"
        val = (f"{password}", f"{id_user}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()
        return 'result true'


    @staticmethod
    def changeName(id_user, name):
        sql = "UPDATE users SET name = %s where id_user = %s"
        val = (f"{name}", f"{id_user}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()
        return 'result true'


    @staticmethod
    def selectIdFromWord(word):
        sql = "SELECT id_word FROM words WHERE word=%s"
        val = (f"{word}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        return cursor.fetchall()[0][0]
    
    @staticmethod
    def selectNameById(id_user):
        sql = "SELECT name FROM users WHERE id_user=%s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        return cursor.fetchall()[0][0]

    #retorna id pelo email
    @staticmethod
    def selectIdFromEmail(email):
        sql = "SELECT id_user FROM users WHERE email=%s"
        val = (f"{email}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        return cursor.fetchall()[0][0]
    
    @staticmethod
    def selectNameFromEmail(email):
        sql = "SELECT name FROM users WHERE email=%s"
        val = (f"{email}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        return cursor.fetchall()[0][0]
    
    @staticmethod
    def selectPasswordFromId(id_user):
        sql = "SELECT password FROM users WHERE id_user=%s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        return cursor.fetchall()[0][0]

    
    @staticmethod
    def linkWordWithProfile(id_word, id_user, fav):
        sql = "SELECT * FROM profile WHERE id_user=%s and id_word = %s"
        val = (f"{id_user}", f"{id_word}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if(result):
            sql = "UPDATE profile SET fl_favorita = %s where id_word = %s and id_user = %s"
            val = (f"{fav}", f"{id_word}", f"{id_user}")
            cursor = Database.db.cursor()
            cursor.execute(sql, val)
            Database.db.commit()
            return 'result true'
        else:
            sql = "INSERT INTO profile (id_user, id_word, fl_conhecia, fl_favorita) VALUES (%s, %s, 0, %s)"
            val = (f"{id_user}", f"{id_word}", f"{fav}")
            cursor = Database.db.cursor()
            cursor.execute(sql, val)
            Database.db.commit()
            return 'result false'
        
    @staticmethod
    def linkWWP(id_word, id_user):
        sql = "SELECT * FROM profile WHERE id_user=%s and id_word = %s"
        val = (f"{id_user}", f"{id_word}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        print("até aqui vai")
        if(result):
            return print('conexao existente')
        else:
            sql = "INSERT INTO profile (id_user, id_word, fl_conhecia, fl_favorita) VALUES (%s, %s, 0, 0)"
            val = (f"{id_user}", f"{id_word}")
            cursor = Database.db.cursor()
            cursor.execute(sql, val)
            Database.db.commit()
            return print('conexao criada')


    @staticmethod
    def isFav(id_user, id_word):
        sql = "SELECT fl_favorita FROM profile WHERE (id_user=%s) AND (id_word = %s)"
        val = (f"{id_user}", f"{id_word}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if (result):
            Database.db.commit()
            return result[0][0]
        else:
            Database.db.commit()
            return -1

    @staticmethod
    def selectFavs(id_user):
        sql = "SELECT count(*) FROM profile where fl_favorita = '1' AND id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return result[0][0]
    

    @staticmethod
    def selectFavsWords(id_user):
        sql = "SELECT w.word FROM profile p inner join words w on p.id_word = w.id_word where fl_favorita = '1' AND id_user = %s order by 1"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        resultado = []
        if(result):
            for r in result:
                resultado.append(r[0].capitalize())
            return resultado
        else:
            return 0
        

    @staticmethod
    def selectKnew(id_user):
        sql = "SELECT count(*) FROM profile where fl_conhecia = '1' AND id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return result[0][0]
    

    @staticmethod
    def selectKnewWords(id_user):
        sql = "SELECT w.word FROM profile p inner join words w on p.id_word = w.id_word where fl_conhecia = '1' AND id_user = %s order by 1"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        resultado = []
        if(result):
            for r in result:
                resultado.append(r[0].capitalize())
            return resultado
        else:
            return 0
        
    @staticmethod
    def selectConheciAqui(id_user):
        sql = f"SELECT count(*) FROM profile where fl_conhecia = '0' AND id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return result[0][0]
    

    @staticmethod
    def selectConheciAquiWords(id_user):
        sql = "SELECT w.word FROM profile p inner join words w on p.id_word = w.id_word where fl_conhecia = '0' AND id_user = %s order by 1"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        resultado = []
        if(result):
            for r in result:
                resultado.append(r[0].capitalize())
            return resultado
        else:
            return 0
        
    @staticmethod
    def selectSabia(id_user):
        sql = "SELECT count(*) FROM profile where fl_sabia = '1' AND id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return result[0][0]
    

    @staticmethod
    def selectSabiaWords(id_user):
        sql = "SELECT w.word FROM profile p inner join words w on p.id_word = w.id_word where fl_sabia = '1' AND id_user = %s order by 1"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        resultado = []
        if(result):
            for r in result:
                resultado.append(r[0].capitalize())
            return resultado
        else:
            return 0

    @staticmethod
    def selectLearnHere(id_user):
        sql = "SELECT count(*) FROM profile where fl_sabia = 0 AND fl_conhecia = 0 AND id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return result[0][0]
    

    @staticmethod
    def selectLearnHereWords(id_user):
        sql = "SELECT w.word FROM profile p inner join words w on p.id_word = w.id_word where fl_sabia = 0 AND fl_conhecia = 0 AND id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        resultado = []
        if(result):
            for r in result:
                resultado.append(r[0].capitalize())
            return resultado
        else:
            return 0
        
    @staticmethod
    def selectQuizAcertos(id_user):
        sql = "SELECT count(*) FROM palavrasQuiz where fl_acerto = 1 AND id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return result[0][0]
    
    @staticmethod
    def selectQuizErros(id_user):
        sql = "SELECT count(*) FROM palavrasQuiz where fl_acerto = 0 AND id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return result[0][0]
    

    @staticmethod
    def selectQuizAcertoWords(id_user):
        sql = "SELECT w.word FROM palavrasQuiz p inner join words w on p.id_word = w.id_word where fl_acerto = 1 AND id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        resultado = []
        if(result):
            for r in result:
                resultado.append(r[0].capitalize())
            return resultado
        else:
            return 0


    @staticmethod
    def selectQuizErroWords(id_user):
        sql = "SELECT w.word FROM palavrasQuiz p inner join words w on p.id_word = w.id_word where fl_acerto = 0 AND id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        resultado = []
        if(result):
            for r in result:
                resultado.append(r[0].capitalize())
            return resultado
        else:
            return 0

        

    @staticmethod
    def updateProfile(id_word, id_user, conhecia, sabia):
        sql = "UPDATE profile SET fl_conhecia = %s, fl_sabia = %s where id_word = %s and id_user = %s"
        val = (f"{conhecia}", f"{sabia}", f"{id_word}", f"{id_user}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()
        return 1
    

    @staticmethod
    def deleteUser(id_user):
        sql = "DELETE FROM profile WHERE id_user = %s"
        val = (f"{id_user}",)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()
        sql = "DELETE FROM users WHERE id_user = %s"
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()
        return 1


    @staticmethod
    def selectWordKnoledge(id_user, id_word):
        sql = "SELECT fl_conhecia, fl_sabia FROM profile where id_user = %s AND id_word = %s"
        val = (f"{id_user}", f"{id_word}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result[0][0] and result[0][1]:
            return 1
        if result[0][0] and not result[0][1]:
            return 2
        if not result[0][0] and not result[0][1]:
            return 3
