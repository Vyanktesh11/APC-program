from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def evaluate_answer(self, answer):
        pass

class MCQQuestion(Question):
    def evaluate_answer(self, answer):
        return answer.strip().lower() == "b"

class TrueFalseQuestion(Question):
    def evaluate_answer(self, answer):
        return answer.strip().lower() == "true"

class DescriptiveQuestion(Question):
    def evaluate_answer(self, answer):
        return len(answer.strip()) >= 20

questions = [MCQQuestion(), TrueFalseQuestion(), DescriptiveQuestion()]
answers = ["B", "True", "This is a sufficiently long answer."]
for question, answer in zip(questions, answers):
    print(type(question).__name__, question.evaluate_answer(answer))
