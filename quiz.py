class Quiz:
    """퀴즈 한 문제를 나타내는 클래스"""

    def __init__(self, question, choices, answer):
        # self는 "지금 만들어지는 이 퀴즈 자신"이라는 뜻이에요
        self.question = question   # 문제 (글자)
        self.choices = choices     # 선택지 4개 (리스트)
        self.answer = answer       # 정답 번호 (1~4)

    def display(self, number):
        """문제와 선택지를 화면에 보여줘요"""
        print("-" * 40)
        print(f"[문제 {number}]")
        print(self.question)
        print()
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")
        print()

    def check(self, user_answer):
        """사용자가 고른 번호가 정답이면 True, 아니면 False"""
        return user_answer == self.answer

    def to_dict(self):
        """파일(JSON)에 저장하기 좋은 모양(딕셔너리)으로 바꿔요"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data):
        """파일에서 읽은 딕셔너리를 Quiz로 되돌려요. 이상하면 ValueError를 내요"""
        question = data["question"]
        choices = data["choices"]
        answer = data["answer"]

        if not isinstance(question, str) or question.strip() == "":
            raise ValueError("문제가 비어 있거나 글자가 아닙니다.")
        if not isinstance(choices, list) or len(choices) != 4:
            raise ValueError("선택지는 4개여야 합니다.")
        for choice in choices:
            if not isinstance(choice, str) or choice.strip() == "":
                raise ValueError("선택지가 비어 있거나 글자가 아닙니다.")
        if type(answer) is not int or answer < 1 or answer > 4:
            raise ValueError("정답은 1~4 사이의 숫자여야 합니다.")

        return cls(question, choices, answer)