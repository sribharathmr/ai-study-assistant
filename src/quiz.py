quiz_active = False
last_question = ""

def start_quiz(question):
    global quiz_active, last_question
    quiz_active = True
    last_question = question

def stop_quiz():
    global quiz_active
    quiz_active = False

def is_quiz_active():
    return quiz_active

def get_last_question():
    return last_question

