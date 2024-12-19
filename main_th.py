import sqlite3
baza = "quiz.sqlite"
conn = None
cursor = None


def open():
    global conn, cursor
    conn = sqlite3.connect(baza)

    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()


def clear_db():
    open()
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    query = '''DROP TABLE IF EXISTS question'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    close()

def create():
    open()
    do('''CREATE TABLE IF NOT EXISTS quiz (id INTEGER 
       PRIMARY KEY,
       name VARCHAR 
       )
              
       ''')
    
    do('''CREATE TABLE IF NOT EXISTS question (question VARCHAR,
       answer VARCHAR,
       wrong1 VARCHAR,
       wrong2 VARCHAR,
       wrong3 VARCHAR,

       
       )
      
       ''')
    
    do('''CREATE TABLE IF NOT EXISTS quiz_content (id INTEGER PRIMARY KEY,
       quiz_id INTEGER,
       question_id INTEGER,
       FOREIGN KEY (quiz_id) REFERENCES quiz(id)
       FOREIGN KEY (question_id) REFERENCES question(id)

       )
              
       ''')
    close()



def add_question():
    questions=[
        ('Скільки буде 2+2?', '4','5','6','110')
        ('Скільки буде 7+2?', '9','5','6','110')
        ('Скільки буде 2+88?', '90','44','67','110')
        ('Скільки буде 2+90?', '92','5','63','110')
        ('Скільки буде 3+22?', '25','56','16','2110')
        ('Скільки буде 24+2?', '26','35','56','6110')


    ]
    open()
    cursor.executemany('''INSERT INTO question(question,answer,wrong1,wrong2,wrong3)
                       VALUES(?,?,?,?,?)
                       
                       
                       
                       ''',questions)
    conn.commit()
    close()


    def add_quiz():
        quizez = [('Тест IQ',)
                  ('Гра на мільйон',)
                  ('Ти геній?',)]
        open()
        cursor.executemany('''INSERT INTO quiz (name) 
        VALUES (?)''',quizez)
        conn.commit()
        close()

    def add_quiz_links():
        
        open()
        
        cursor.execute('''PRAGMA foreign_keys=on''')
        query = ('''
        INSERT INFO quiz_content (quiz_id, question_id) 
        VALUES (?, ?)
     (quiz_id, question_id))''')
        answer= input("Додати зв'язок?(y/n)")
        while answer !="n":
            quiz_id = int(input("Введіть ID вікторини"))
            question_id = int(input("Введіть ID питання"))
            cursor.execute(query,[quiz_id,question_id])
            conn.commit()
            answer= input("Додати зв'язок?(y/n)")

        close()

    def show(table):
        query = 'SELECT * FROM'+table
        open()
        cursor.execute(query)
        print(cursor.fetchall())
        close()
        
    def show_tables():
        show("question")
        show("quiz")
        show("quiz_content")

    def return_question(question_id=0,quiz_id=1):
        open()
        query = '''
        SELECT quiz_content.id, question.question, question.answer,
        question.wron1,question.wrong2,question.wrong3
        FROM question, quiz_content
        WHERE quiz_content.question == question.id
        AND quiz_content> ? AND quiz_content.quiz_id==?
        ORDER BY quiz_content.id

'''

    cursor.execute(query,[question_id,quiz_id])
    result = cursor.fetchone()
    close()
    return result

    def main():
        clear_db()
        create()
        add_question()
        add_quiz()
        add_links()
        show_tables()
        print(return_questio(3,1))


    if __name__=="__main__":
        main()

        





            


        


       