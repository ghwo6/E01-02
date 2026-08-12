
ghwo61351@c6r6s2 ~ % cd tasks_ghwo6 
ghwo61351@c6r6s2 tasks_ghwo6 % ls
E01-02	E1-1

ghwo61351@c6r6s2 tasks_ghwo6 % git clone git@github.com:ghwo6/E01-02.git E01-02-cloned
'E01-02-cloned'에 복제합니다...
remote: Enumerating objects: 116, done.
remote: Counting objects: 100% (116/116), done.
remote: Compressing objects: 100% (77/77), done.
remote: Total 116 (delta 58), reused 92 (delta 34), pack-reused 0 (from 0)
오브젝트를 받는 중: 100% (116/116), 793.49 KiB | 1.02 MiB/s, 완료.
델타를 알아내는 중: 100% (58/58), 완료.
ghwo61351@c6r6s2 tasks_ghwo6 % cd ./E01-02-cloned 
ghwo61351@c6r6s2 E01-02-cloned % cd ..
ghwo61351@c6r6s2 tasks_ghwo6 % cd E01-02
ghwo61351@c6r6s2 E01-02 % git branch
  develop
* main
  test_solving
ghwo61351@c6r6s2 E01-02 % cd ../E01-02-cloned 
ghwo61351@c6r6s2 E01-02-cloned % ls
custom_input.py		docs			pull_test		quiz.py			README.md		state.json.backup
data_handle.py		main.py			pull_test.txt		quizgame.py		state.json
ghwo61351@c6r6s2 E01-02-cloned % git branch
* develop
ghwo61351@c6r6s2 E01-02-cloned % git switch main
branch 'main' set up to track 'origin/main'.
새로 만든 'main' 브랜치로 전환합니다
ghwo61351@c6r6s2 E01-02-cloned % ls
custom_input.py		docs			pull_test.txt		quizgame.py		state.json
data_handle.py		main.py			quiz.py			README.md		state.json.backup
ghwo61351@c6r6s2 E01-02-cloned % rm pull_test.txt 
ghwo61351@c6r6s2 E01-02-cloned % echo "Pull해봤습니다." >> pull_test1.txt
ghwo61351@c6r6s2 E01-02-cloned % ls
custom_input.py		docs			pull_test1.txt		quizgame.py		state.json
data_handle.py		main.py			quiz.py			README.md		state.json.backup
ghwo61351@c6r6s2 E01-02-cloned % git add .
ghwo61351@c6r6s2 E01-02-cloned % git commit -m "TEST: pull_test1.txt를 클론하여 추가 하고 pull을 테스트 합니다."
[main 2f2749f] TEST: pull_test1.txt를 클론하여 추가 하고 pull을 테스트 합니다.
 2 files changed, 1 insertion(+), 1 deletion(-)
 delete mode 100644 pull_test.txt
 create mode 100644 pull_test1.txt
ghwo61351@c6r6s2 E01-02-cloned % git push origin main
오브젝트 나열하는 중: 4, 완료.
오브젝트 개수 세는 중: 100% (4/4), 완료.
Delta compression using up to 6 threads
오브젝트 압축하는 중: 100% (2/2), 완료.
오브젝트 쓰는 중: 100% (3/3), 368 bytes | 368.00 KiB/s, 완료.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:ghwo6/E01-02.git
   5b2c67f..2f2749f  main -> main
ghwo61351@c6r6s2 E01-02-cloned % cd ..
ghwo61351@c6r6s2 tasks_ghwo6 % cd E01-02
ghwo61351@c6r6s2 E01-02 % ls
__pycache__		data_handle.py		main.py			quiz.py			README.md		state.json.backup
custom_input.py		docs			pull_test.txt		quizgame.py		state.json
ghwo61351@c6r6s2 E01-02 % git pull origin main
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 3 (delta 1), reused 3 (delta 1), pack-reused 0 (from 0)
오브젝트 묶음 푸는 중: 100% (3/3), 348 bytes | 348.00 KiB/s, 완료.
github.com:ghwo6/E01-02 URL에서
 * branch            main       -> FETCH_HEAD
   5b2c67f..2f2749f  main       -> origin/main
업데이트 중 5b2c67f..2f2749f
Fast-forward
 pull_test.txt  | 1 -
 pull_test1.txt | 1 +
 2 files changed, 1 insertion(+), 1 deletion(-)
 delete mode 100644 pull_test.txt
 create mode 100644 pull_test1.txt
ghwo61351@c6r6s2 E01-02 % ls
__pycache__		data_handle.py		main.py			quiz.py			README.md		state.json.backup
custom_input.py		docs			pull_test1.txt		quizgame.py		state.json