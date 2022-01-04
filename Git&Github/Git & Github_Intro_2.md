# Git & Github Intro_2

---

## 원격 저장소 관리

- git remote

  1. 원격 저장소 등록

     `git remote add <이름> <주소> `형식 으로 작성한다.

     ```bash
     $ git remote add origin https://github.com/username/TIL.git
     
     [풀이]
     git 명령어를 작성할건데, remote(원격 저장소)에 add(추가) 한다.
     origin이라는 이름으로 https://github.com/edukyle/TIL.git라는 주소의 원격 저장소를 add(추가)한다.
     ```

  2. 원격 저장소 조회

     `git remote -v` 로 작성한다.

     ```bash
     $ git remote -v
     origin  https://github.com/username/TIL.git (fetch)
     origin  https://github.com/username/TIL.git (push)
     
     
     add를 이용해 추가했던 원격 저장소의 이름과 주소가 출력된다.
     ```

    3. 원격 저장소 연결 삭제

       `git remote rm <이름>` 혹은 `git remote remove <이름>` 으로 작성한다.

       >  로컬과 원격 저장소의 연결을 끊는 것이지, 원격 저장소 자체를 삭제하는 게 아니다. 

       ```bash
       $ git remote rm origin
       $ git remote remove origin
       
       
       [풀이]
       git 명령어를 작성할건데, remote(원격 저장소)와의 연결을 rm(remove, 삭제) 한다.
       그 원격 저장소의 이름은 origin이다.
       ```

  			4. 원격 저장소에 업로드
        - 파일을 업로드 하는 것이 아니라 커밋을 업로드 하는 것이다.
        - 로컬 저장소에서 커밋을 생성해야 원격 저장소에 업로드를 할 수 있다.

​	      ` git push` 

​	로컬 저장소의 커밋을 원격 저장소에 업로드하는 명령어

​	git push <저장소 이름> <브랜치 이름>` 형식으로 작성한다..

​	`-u` 옵션을 사용하면, 두 번째 커밋부터는 `저장소 이름, 브랜치 이름`을 생략 가능하다.

```bash
$ git push origin master

[풀이]
git 명령어를 사용하며, origin이라는 이름의 원격 저장소의 master 브랜치에 push 한다.

------------------------------------------------

$ git push -u origin master
이후에는 $ git push 라고만 작성해도 push가 된다.
```

