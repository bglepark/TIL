# Git & Github Intro_1

## 1. Git과 Github란?

- Git

  - 프로그램 등의 소스 코드관리를 하는 버전 관리 프로그램	
  - 작업의 기록을 남겨서 수정 및 보완 등의 이력을 추적하기 위하여 사용한다.
  - 이를 통해 다른 작업자와의 협업을 용이하게 한다.

  > 파일을 여러번 수정후 저장하면서 `파일명_최종.txt` , `파일명_리얼최종.txt` 등의 네이밍을 할 필요가 없다.

- Github
  - Git이 소스 코드 관리를 하는 버전 관리 프로그램이라면, Github은 파일의 버전 관리에 대해 타 사용자들과 공유를 할 수 있는 일종의 서비스를 제공하는 서버이다. 
  - 이를 통해 원활하게 협업을 하고 소스에 대한 이력관리를 하며 소셜코딩을 할 수 있다.
  - 다른 사람들이 개발한 코드를 보거나 공유를 할 수 있고, 진행되고 있는 프로젝트에 함께 참여하면서 수정 및 보완 작업을 진행할 수 있다.



## 2. Git 초기설정

> 최초 한 번만 설정을 하며, 매번 Git을 사용할 때마다 설정할 필요가 없다.

1. Github에서 협업을 하기 위해서는 누가 커밋 기록을 남겼는지 확인할 수 있도록 이름과 이메일을 설정한다.

   ```bash
   $ git config --global user.name "이름"
   $ git config --global user.email "메일 주소"
   ```

2. 이름과 이메일을 확인한다.

   ```bash
   $ git config --global -l
   
   또는
   
   $ git config --global --list
   ```

   등록한 이름과 이메일을 삭제하기 위해서는 아래의 코드를 이용한다.

   ```bash
   $ git config --unset user.name
   $ git config --unset user.email
   ```



## 3. Git 기본 명령어

- 로컬 저장소

![](Git & Github Intro.assets/local 저장소.png)

​	

- `Working Directory (= Working Tree)` : 사용자의 일반적인 작업이 일어나는 곳
- `Staging Area (= Index)` : 커밋을 위한 파일 및 폴더가 추가되는 곳
- `Repository` : staging area에 있던 파일 및 폴더의 변경사항(커밋)을 저장하는 곳
- Git은 **Working Directory → Staging Area → Repository** 의 과정으로 버전 관리를 수행한다.



1. git init

   ```bash
   $ git init
   Initialized empty Git repository in C:/Users/user/git-practice/.git/
   
   user@PC ~/git-practice (master)
   ```

   - 현재 작업 중인 디렉토리를 Git으로 관리한다는 명령어
   - `.git` 이라는 숨김 폴더를 생성하고, 터미널에는 `(master)`라고 표기된다.
   - ls -a 명령어를 통해 `.git` 을 확인할 수 있다.

> **Caution**  ❗
>
> 1. 이미 Git 저장소인 폴더 내에 또 다른 Git 저장소를 만들지 않는다. (중첩 금지) 즉, 터미널에 이미 (master)가 있다면, 
>
>    `git init`을 절대 입력하면 안된다.
>
> 2. 절대로 홈 디렉토리에서 `git init`을 하지 않습니다. 터미널의 경로가 ~ 인지 확인합니다.



2. git status

   ```bash
   $ git status
   On branch master
   
   No commits yet
   
   nothing to commit (create/copy files and use "git add" to track)
   ```

   - Working Directory와 Staging Area에 있는 파일의 현재 상태를 알려주는 명령어
   - 어떤 작업을 시행하기 전에 수시로 status를 확인하면 좋다.

   - 상태
     - `Untracked` : Git이 관리하지 않는 파일 (한번도 Staging Area에 올라간 적 없는 파일) -> U로 표시됨
     - `Untracked `: Git이 관리하지 않는 파일 (한번도 Staging Area에 올라간 적 없는 파일)
       - `Unmodified` : 최신 상태
       - `Modified` : 수정되었지만 아직 Staging Area에는 반영하지 않은 상태
       - `Staged` : Staging Area에 올라간 상태

   ![](Git & Github Intro.assets/file lifecycle.png)



3. git add

   ```bash
   # 특정 파일
   $ git add a.txt
   
   # 특정 폴더
   $ git add my_folder/
   
   # 현재 디렉토리에 속한 파일/폴더 전부
   $ git add .
   ```

   - Working Directory에 있는 파일을 Staging Area로 올리는 명령어
   - Git이 해당 파일을 추적(관리)할 수 있도록 만든다.
   - `Untracked, Modified → Staged` 로 상태를 변경한다.



4. git commit

   ```bash
   $ git commit -m "원하는 메세지 입력"
   [master (root-commit) c02659f] first commit
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 a.txt
   ```

   - Staging Area에 올라온 파일의 변경 사항을 하나의 버전(커밋)으로 저장하는 명령어
   - `커밋 메세지`는 현재 변경 사항들을 잘 나타낼 수 있도록 `의미` 있게 작성하는 것이 좋다.
   - 각각의 커밋은 `SHA-1` 알고리즘에 의해 반환 된 고유의 해시 값을 ID로 가진다.
   - `(root-commit)` 은 해당 커밋이 최초의 커밋 일 때만 표시된다. 이후 커밋부터는 사라진다.



5. git log

   ```bash
   $ git log
   commit 1870222981b4731d14ef91d401c68c0bbb2f6e7d (HEAD -> master)
   Author: user <user1@email.com>
   Date:   Thu Dec 9 15:26:46 2021 +0900
   
       first commit
   ```

   - 커밋의 내역(ID, 작성자, 시간, 메세지 등)을 조회할 수 있는 명령어
   - git log 의 옵션
     - `--oneline` : 한 줄로 축약해서 보여준다.
     - `--graph` : 브랜치와 머지 내역을 그래프로 보여준다.
     - `--all` : 현재 브랜치를 포함한 모든 브랜치의 내역을 보여준다.
     - `--reverse` : 커밋 내역의 순서를 반대로 보여준다. (최신이 가장 아래)
     - `-p` : 파일의 변경 내용도 같이 보여준다.
     - `-2` : 원하는 갯수 만큼의 내역을 보여줍니다. (2 말고 임의의 숫자 사용 가능)