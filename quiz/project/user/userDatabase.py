from operator import truediv
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="quiz"    
)

cursor = con.cursor()

def getSubjects():
    try:
        cursor.execute('SELECT * FROM subject')
        return cursor.fetchall()
    except:
        return False    

def getTopics(subId):
    try:
        cursor.execute('SELECT * FROM topic WHERE subjectId = %s', (subId, ))
        return cursor.fetchall()
    except:
        return False 

def getQuestions(topicId):
    try:
        cursor.execute('SELECT * FROM questions WHERE topicId = %s', (topicId, ))
        return cursor.fetchall()
    except:
        return False

def login(data):
    try:
        cursor.execute('SELECT * FROM users WHERE username = %s and password = %s', data)
        return cursor.fetchall()
    except:
        return False


def createScores(data):
    print(data)
    try:
        cursor.execute('INSERT INTO scores (userId, subjectId, topicId, scores, totalQues) VALUES (%s, %s, %s, %s, %s)', data)
        con.commit()
        return True
    except:
        return False

def fetchScore(userData):
    try:
        cursor.execute('SELECT scores.id, subject.name, topic.name, scores.scores, scores.totalQues FROM scores LEFT JOIN subject ON subject.id = scores.subjectId LEFT JOIN topic ON topic.id = scores.topicId WHERE userId = %s', (userData[0][0], ))
        return cursor.fetchall()
    except:
        return False