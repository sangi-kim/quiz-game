class QuizGame:
    """게임 전체를 관리하는 클래스"""

    def __init__(self):
        # 퀴즈 목록, 최고 점수 (나중 단계에서 채워요)
        self.quizzes = []
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
                    print("📝 퀴즈 풀기는 준비 중입니다.")
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