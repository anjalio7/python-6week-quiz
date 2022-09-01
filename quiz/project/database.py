
from operator import truediv
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="quiz"    
)

cursor = con.cursor()

def adminLogin(data):
    try:
        cursor.execute('SELECT * FROM admin WHERE username = %s and password = %s', data)
        return cursor.fetchall()
    except:
        return False

def allSubject():
    try:
        cursor.execute('SELECT * FROM subject')
        return cursor.fetchall()
    except:
        return False

def addSubject(data):
    try:
        cursor.execute('INSERT INTO subject (name) VALUES (%s)', data)
        con.commit()
        return True
    except:
        return False

def getSubjects():
    try:
        cursor.execute('SELECT * FROM subject')
        return cursor.fetchall()
    except:
        return False

def deleteSubject(id):
    try:
        cursor.execute('DELETE FROM subject WHERE id = %s', id)
        con.commit()
        return True
    except:
        return False

def singleSubject(id):
    try:
        cursor.execute('SELECT * FROM subject WHERE id = %s', id)
        return cursor.fetchone()
    except:
        return False

def editSubject(data):
    try:
        cursor.execute('UPDATE subject SET name = %s WHERE id = %s', data)
        con.commit()
        return True
    except:
        return False

def addTopic(data):
    try:
        cursor.execute('INSERT INTO topic (subjectId, name) VALUES (%s, %s)', data)
        con.commit()
        return True
    except:
        return False

def allTopics():
    try:
        cursor.execute('SELECT topic.id, subject.name, topic.name FROM topic LEFT JOIN subject ON topic.subjectId = subject.id')
        return cursor.fetchall()
    except:
        return False

def deleteTopic(id):
    try:
        cursor.execute('DELETE FROM topic WHERE id = %s', id)
        con.commit()
        return True
    except:
        return False

def singleTopic(id):
    try:
        cursor.execute('SELECT subject.id, subject.name, topic.name FROM topic LEFT JOIN subject ON topic.subjectId = subject.id WHERE topic.id = %s', id)
        return cursor.fetchone()
    except:
        return False

def editTopic(data):
    try:
        cursor.execute('UPDATE topic SET subjectId = %s, name = %s WHERE id = %s', data)
        con.commit()
        return True
    except:
        return False


def getTopic(subId):
    try:
        cursor.execute('SELECT id, name FROM topic WHERE subjectId = %s', (subId, ))
        return cursor.fetchall()
    except:
        return False

def addQues(data):
    print(data)
    try:
        cursor.execute('INSERT INTO questions (topicId, question, options, answer) VALUES (%s, %s, %s, %s)', data)
        con.commit()
        return True
    except:
        return False


def getQues():
    try:
        cursor.execute('SELECT questions.id, topic.name, questions.question, questions.options, questions.answer FROM questions LEFT JOIN topic ON questions.topicId = topic.id')
        return cursor.fetchall()
    except:
        return False

def deleteQues(id):
    try:
        cursor.execute('DELETE FROM questions WHERE id = %s', id)
        con.commit()
        return True
    except:
        return False

def singleQues(id):
    try:
        cursor.execute('SELECT topic.id, topic.name, questions.question, questions.options, questions.answer FROM questions LEFT JOIN topic ON questions.topicId = topic.id WHERE questions.id = %s', id)
        return cursor.fetchone()
    except:
        return False

def editQues(data):
    try:
        cursor.execute('UPDATE questions SET topicId = %s, question = %s, options = %s, answer = %s WHERE id = %s', data)
        con.commit()
        return True
    except:
        return False



def getTopics(subId):
    try:
        cursor.execute('SELECT * FROM topic WHERE subjectId = %s', (subId, ))
        return cursor.fetchall()
    except:
        return False 


def getScores(topicId):
    try:
        cursor.execute('SELECT *  FROM scores WHERE topicId = %s', (topicId, ))
        return cursor.fetchall()
    except:
        return False