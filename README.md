
~~~sh

ghwo61351@c6r2s2 E01-02 % git add .
ghwo61351@c6r2s2 E01-02 % git status
On branch feature/quizGame-py/menu
Your branch is ahead of 'origin/feature/quizGame-py/menu' by 1 commit.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md
        modified:   main.py
        modified:   quizgame.py
        modified:   state.json
        new file:   state.json.backup

ghwo61351@c6r2s2 E01-02 % git commit -m "문제 보기 추가"
[feature/quizGame-py/menu ddfb3f0] 문제 보기 추가
 5 files changed, 91 insertions(+), 28 deletions(-)
 create mode 100644 state.json.backup
ghwo61351@c6r2s2 E01-02 % git branch
  develop
* feature/quizGame-py/menu
ghwo61351@c6r2s2 E01-02 % git checkout develop
Switched to branch 'develop'
Your branch is up to date with 'origin/develop'.
ghwo61351@c6r2s2 E01-02 % git merge feature/quizGame-py/menu
Updating 2febdaf..ddfb3f0
Fast-forward
 .gitignore        |   4 ++-
 README.md         |   5 +--
 main.py           |   9 +++++
 quiz.py           |  26 ++++++++++++++
 quizgame.py       | 297 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 state.json        |  65 +++++++++++++++++++++++++++++++++++
 state.json.backup |  55 +++++++++++++++++++++++++++++
 7 files changed, 458 insertions(+), 3 deletions(-)
 create mode 100644 main.py
 create mode 100644 quiz.py
 create mode 100644 quizgame.py
 create mode 100644 state.json
 create mode 100644 state.json.backup
ghwo61351@c6r2s2 E01-02 % git log --oneline
ddfb3f0 (HEAD -> develop, feature/quizGame-py/menu) 문제 보기 추가
83ae257 FEAT: state.json 파일 읽기 및 쓰기 기능 추가
58944f7 (origin/feature/quizGame-py/menu) FEAT : gitignore수정 및 __pycache__ 폴더 제거
f5ccbf9 FEAT:문제 추가 기능을 추가함 (try except KeyboardInterrupt와 EOF수정)
ad7b097 FEAT:문제풀기 가능
d9cc573 FEAT:5개 퀴즈 데이터 추가완료
3a9a6b9 FEAT: Quiz클래스 추가(함수 실행을 위해 main.py추가)
4d9f99f FEAT:종료 구현 완료
d857ebf FEAT:메뉴출력완료
2febdaf (origin/develop, origin/HEAD) FEAT: 브랜치별로 작성할 README폴더  준비
6378852 feat. 초기화 완료 (md파일 추가 및 gitignore및 기능별 구현후 작성할 readme폴더 생성)
ghwo61351@c6r2s2 E01-02 % 
~~~


~~~
배운것 입력
> git commit -m "~" main에 아무 커밋이 없으면 브랜치를 생성할 수 없음
> 빈 폴더를 git add . 한다고 해서 추가 되지 않는다.
> 이전 커밋에 수정사항을 추가하려고 한다면 (git add .후에) git commit --amend하면 된다고 함
> git branch 이동 하는법
> (레포에 1개라도 커밋 기록이 있는상태)
> git switch -c <브랜치>   - 브랜치에 입력하길 원하는 이름 생성

Switched to a new branch 'develop' 확인 가능

> git branch 입력시 현재 어디에 있는지 확인 가능함
* develop
  main
> 빈 폴더를 유지하기 위해서 .gitkeep 생성함
> 퀴즈가 추가 됬을때, 하이스코어가 갱신됬을떄 data는 어떻게 바뀔까? 바뀌지 않는다. 그 이유는?
~~~