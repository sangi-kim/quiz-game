from default_quizzes import get_default_quizzes


class QuizGame:
    """게임 전체를 관리하는 클래스"""

    def __init__(self):
        # 임시: 12단계에서 파일 불러오기(load)로 바꿔요
        self.quizzes = get_default_quizzes()
        self.best_score = 0   # 최고 기록 때 맞힌 개수
        self.best_total = 0   # 그때 전체 문제 수 (0이면 아직 안 푼 것)

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

    def play_quiz(self):
        """저장된 퀴즈를 한 문제씩 내고 결과를 보여줘요"""
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

        points = correct * 100 // total

        # 최고 점수와 비교해서 더 높으면 바꿔요
        if self.best_total == 0:
            is_best = True
        else:
            best_points = self.best_score * 100 // self.best_total
            is_best = points > best_points

        print("=" * 40)
        print(f"🏆 결과: {total}문제 중 {correct}문제 정답! ({points}점)")
        if is_best:
            self.best_score = correct
            self.best_total = total
            print("🎉 새로운 최고 점수입니다!")
        print("=" * 40)

        self.save()

    def save(self):
        """저장하기 (12단계에서 완성해요)"""
        pass

    def run(self):
        """게임의 메인 반복"""
        try:
            while True:
                self.show_menu()
                choice = self.read_int("선택: ", 1, 5)

                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    print("📌 퀴즈 추가는 준비 중입니다.")
                elif choice == 3:
                    print("📋 퀴즈 목록은 준비 중입니다.")
                elif choice == 4:
                    print("🏆 점수 확인은 준비 중입니다.")
                elif choice == 5:
                    print("👋 종료합니다.")
                    break
        except KeyboardInterrupt:
            print("\n⚠️ 강제 종료. 저장 후 종료합니다.")
        except EOFError:
            print("\n⚠️ 입력 종료. 저장 후 종료합니다.")

        self.save()