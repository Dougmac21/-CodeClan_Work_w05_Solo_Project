from flask import Blueprint, Flask, redirect, render_template, request

from models.question import Question
import repositories.question_repository as question_repository

question_blueprint = Blueprint("questions", __name__)

#index
@questions_blueprint.route("/questions")
def questions():
    questions = question_repository.select_all()
    return render_template("questions/index.html", questions=questions)

#new
@questions_blueprint.route("/questions/new")
def new_question():
    return render_template("questions/new.html")

#create
@questions_blueprint.route("/questions", methods=["POST"])
def create_question():
    question = request.form["question"]
    new_question = Question(question, correct_answer, alt_ans_1, alt_ans_2, alt_ans_3, difficulty, topic)
    question_repository.save(new_question)
    return redirect("/questions")

#edit
@questions_blueprint.route("/questions/<id>/edit")
def edit_question(id):
    question = question_repository.select(id)
    return render_template('questions/edit.html', question=question)


#update
@question_blueprint.route("/questions/<id>", methods=["POST"])
def update_question(id):
    question = request.form["question"]
    question = Question(question, correct_answer, alt_ans_1, alt_ans_2, alt_ans_3, difficulty, topic, id)
    question_repository.update(question)
    return redirect("/questions")


#delete
@questions_blueprint.route("/questions/<id>/delete", methods=["POST"])
def delete_question(id):
    question_repository.delete(id)
    return redirect("/questions")
