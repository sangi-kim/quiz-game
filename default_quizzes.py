from quiz import Quiz


def get_default_quizzes():
    """처음 실행할 때 사용하는 기본 퀴즈 목록 (Git 명령어 주제)"""
    return [
        Quiz(
            "내 폴더를 새로운 Git 저장소로 시작하는 명령어는?",
            ["git add", "git init", "git push", "git pull"],
            2,
        ),
        Quiz(
            "변경한 파일을 커밋할 목록(준비 상자)에 담는 명령어는?",
            ["git commit", "git clone", "git add", "git merge"],
            3,
        ),
        Quiz(
            "담아 둔 변경 내용을 설명 메시지와 함께 기록으로 남기는 명령어는?",
            ["git pull", "git init", "git checkout", "git commit"],
            4,
        ),
        Quiz(
            "내 컴퓨터의 커밋을 GitHub에 올리는 명령어는?",
            ["git push", "git pull", "git clone", "git add"],
            1,
        ),
        Quiz(
            "GitHub의 새로운 변경 내용을 내 컴퓨터로 가져와 합치는 명령어는?",
            ["git push", "git commit", "git pull", "git init"],
            3,
        ),
        Quiz(
            "GitHub 저장소를 내 컴퓨터에 통째로 복제하는 명령어는?",
            ["git clone", "git checkout", "git merge", "git add"],
            1,
        ),
        Quiz(
            "다른 브랜치로 이동하거나, -b 옵션으로 새 브랜치를 만드는 명령어는?",
            ["git merge", "git checkout", "git commit", "git pull"],
            2,
        ),
        Quiz(
            "다른 브랜치의 작업 내용을 지금 브랜치에 합치는 명령어는?",
            ["git checkout", "git push", "git clone", "git merge"],
            4,
        ),
    ]