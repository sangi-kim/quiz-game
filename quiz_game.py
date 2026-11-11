import json
import os

from default_quizzes import get_default_quizzes
from file_manager import backup_broken_file, read_state, write_state
from quiz import Quiz

# 이 파일이 있는 폴더(프로젝트 루트)의 state.json
STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "state.json")


class QuizGame:
    """게임 전체를 관리하는 클래스

    속성
      quizzes    : Quiz 객체들이 담긴 리스트
      best_score : 최고 기록 때 맞힌 개수
      best_total : 그 기록 때 전체 문제 수 (0이면 아직 안 푼 것)
    """

    # ---------- 1. 시작 / 파일 ----------
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.best_total = 0
        self.load()

    def use_default_data(self):
        """기본 퀴즈와 빈 점수로 시작해요"""
        self.quizzes = get_default_quizzes()
        self.best_score = 0
        self.best_total = 0

    def load(self):
        """state.json에서 퀴즈와 최고 점수를 불러와요"""
        try:
            data = read_state(STATE_FILE)
            quizzes = [Quiz.from_dict(item) for item in data["quizzes"]]
            best_score = data["best_score"]
            best_total = data["best_total"]

            if (
                type(best_score) is not int
                or type(best_total) is not int
                or best_score < 0
                or best_score > best_total
            ):
                raise ValueError("점수 값이 올바르지 않습니다.")

        except FileNotFoundError:
            # 첫 실행: 파일이 아직 없어요
            self.use_default_data()
            return

        except (json.JSONDecodeError, UnicodeDecodeError, KeyError, TypeError, ValueError):
            # 파일은 있는데 내용이 망가졌어요
            print("⚠️ 데이터 손상. 기본 데이터로 초기화합니다.")
            try:
                backup_broken_file(STATE_FILE)
                print("📁 손상된 파일은 state.json.bak 으로 보관했습니다.")
            except OSError:
                print("⚠️ 손상된 파일을 보관하지 못했습니다.")
            self.use_default_data()
            return

        except OSError:
            # 파일을 읽을 수 없어요 (권한 문제 등)
            print("⚠️ 파일 읽기 오류. 기본 데이터로 초기화합니다.")
            self.use_default_data()
            return

        # 여기까지 왔으면 모두 정상이에요
        self.quizzes = quizzes
        self.best_score = best_score
        self.best_total = best_total

        if best_total == 0:
            score_text = "최고점수 없음"
        else:
            score_text = f"최고점수 {self.calc_points(best_score, best_total)}점"
        print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(quizzes)}개, {score_text})")

    def save(self):
        """퀴즈와 최고 점수를 state.json에 저장해요"""
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
            "best_total": self.best_total,
        }
        try:
            write_state(STATE_FILE, data)
        except OSError:
            print("⚠️ 저장 실패. 데이터가 유지되지 않을 수 있습니다.")

    # ---------- 2. 입력 도우미 ----------
    def read_int(self, prompt, low, high):
        """low~high 사이의 숫자를 받을 때까지 계속 물어봐요"""
        while True:
            text = input(prompt).strip()   # 앞뒤 공백 제거

            if text == "":
                print("⚠️ 입력이 없습니다. 다시 입력해 주세요.")
                continue

            try:
                number = int(text)
            except ValueError:
                print("⚠️ 숫자를 입력하세요.")
                continue

            if number < low or number > high:
                print(f"⚠️ {low}-{high} 사이의 숫자를 입력하세요.")
                continue

            return number

    def read_text(self, prompt):
        """빈 글자가 아닌 글을 받을 때까지 계속 물어봐요"""
        while True:
            text = input(prompt).strip()   # 앞뒤 공백 제거

            if text == "":
                print("⚠️ 입력이 없습니다. 다시 입력해 주세요.")
                continue

            return text

    # ---------- 3. 계산 도우미 ----------
    def calc_points(self, correct, total):
        """맞힌 개수를 100점 만점 점수로 바꿔요"""
        return correct * 100 // total

    def update_best_score(self, correct, total):
        """이번 기록이 최고면 바꾸고 True, 아니면 False를 돌려줘요"""
        points = self.calc_points(correct, total)

        if self.best_total != 0:
            best_points = self.calc_points(self.best_score, self.best_total)
            if points <= best_points:
                return False

        self.best_score = correct
        self.best_total = total
        return True

    # ---------- 4. 화면 출력 ----------
    def show_menu(self):
        """메뉴를 화면에 보여줘요"""
        print()
        print("=" * 40)
        print("      🎯 나만의 Git 퀴즈 게임 🎯")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def show_quiz_list(self):
        """등록된 퀴즈의 문제를 번호와 함께 보여줘요"""
        if len(self.quizzes) == 0:
            print("📭 등록된 퀴즈가 없습니다.")
            return

        print()
        print(f"📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print()
        print("-" * 40)
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")
        print("-" * 40)

    def show_best_score(self):
        """최고 점수를 보여줘요"""
        if self.best_total == 0:
            print("📭 아직 퀴즈를 풀지 않았습니다.")
            return

        points = self.calc_points(self.best_score, self.best_total)
        print()
        print(
            f"🏆 최고 점수: {points}점 "
            f"({self.best_total}문제 중 {self.best_score}문제 정답)"
        )

    # ---------- 5. 기능 ----------
    def play_quiz(self):
        """저장된 퀴즈를 한 문제씩 내고 결과를 보여줘요"""
        if len(self.quizzes) == 0:
            print("📭 등록된 퀴즈가 없습니다.")
            return

        total = len(self.quizzes)
        print()
        print(f"📝 퀴즈를 시작합니다! (총 {total}문제)")

        correct = 0
        for number, quiz in enumerate(self.quizzes, start=1):
            quiz.display(number)
            user_answer = self.read_int("정답 입력: ", 1, 4)

            if quiz.check(user_answer):
                print("✅ 정답입니다!")
                correct += 1
            else:
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.")
            print()

        points = self.calc_points(correct, total)
        is_best = self.update_best_score(correct, total)

        print("=" * 40)
        print(f"🏆 결과: {total}문제 중 {correct}문제 정답! ({points}점)")
        if is_best:
            print("🎉 새로운 최고 점수입니다!")
        print("=" * 40)

        self.save()

    def add_quiz(self):
        """새 퀴즈를 입력받아 등록해요"""
        print()
        print("📌 새로운 퀴즈를 추가합니다.")
        print()

        question = self.read_text("문제를 입력하세요: ")

        choices = []
        for i in range(1, 5):
            choice = self.read_text(f"선택지 {i}: ")
            choices.append(choice)

        answer = self.read_int("정답 번호 (1-4): ", 1, 4)

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        print()
        print("✅ 퀴즈가 추가되었습니다!")

        self.save()

    # ---------- 6. 실행 ----------
    def run(self):
        """게임의 메인 반복"""
        try:
            while True:
                self.show_menu()
                choice = self.read_int("선택: ", 1, 5)

                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.show_quiz_list()
                elif choice == 4:
                    self.show_best_score()
                elif choice == 5:
                    print("👋 종료합니다.")
                    break
        except KeyboardInterrupt:
            print("\n⚠️ 강제 종료. 저장 후 종료합니다.")
        except EOFError:
            print("\n⚠️ 입력 종료. 저장 후 종료합니다.")

        self.save()