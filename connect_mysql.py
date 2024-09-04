import pymysql

# 1. mysql 연결
conn = pymysql.connect(
    host='127.0.0.1',   # IP address
    user='root',        # check from MySQL
    password='0000',    # check from MySQL
    db='DBName',        # check from MySQL
    charset='utf8'
    )

# 2. 커서 생성하기
cur = conn.cursor()

# 3. 테이블 만들기 - 0이 나오면 잘 되는 것
cur.execute("CREATE TABLE userTable (id char(4), userName char(15), email char(20))")

# 4. 데이터 입력하기 - 1이 나오면 잘 되는 것
cur.execute("INSERT INTO userTable VALUES('hong', '김민수', 'hong@naver.com')")
cur.execute("INSERT INTO userTable VALUES('kim', '김재연', 'kim@daum.com')")
cur.execute("INSERT INTO userTable VALUES('star', '박정훈', 'star@paran.com')")
cur.execute("INSERT INTO userTable VALUES('yang', '밤양갱', 'yang@gmail.com')")

# 5. 입력한 데이터 저장하기
conn.commit()

# 6. MySQL 연결 종료하기
conn.close()