# Description: Quiz with multiple-choice questions. Randomly picks questions and gives score at the end.
# Topics Covered:
# Lists/dictionaries
# Loops & conditionals
# Functions
# File handling (store questions in a file)
# Random module
# OOP (optional: make Question class)

import random
import os

# ? questions.txt file to have:
# ? Question (line 1)
# ? Correct answer (line 2)
# ? Options, comma-separated (line 3)


class Question:
    def __init__(self, question, answer, options):
        self.question = question
        self.answer = answer
        self.options = options
    
    def is_correct(self, user_answer):
        return user_answer == self.answer
    
    def __str__(self):
        return f"Question: {self.question}\nOptions: {self.options}"


def load_questions(file_path):
    questions = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            question = lines[i].strip()
            answer = lines[i + 1].strip()
            options = lines[i + 2].strip().split(',')
            questions.append(Question(question, answer, options))
    return questions


def main():
    questions = load_questions('questions.txt')
    random.shuffle(questions)
    score = 0
    for question in questions:
        print(question)
        user_answer = input("Your answer: ").strip().lower()
        if question.is_correct(user_answer):
            score += 1
        print(f"Your final score is {score}/{len(questions)}")

if __name__ == "__main__":
    main()