print("曾经沧海难为水")
print("除却巫山不是云")
print("取次花丛懒回顾\n半缘修道半缘君")

leader = "王伦"
print("第一任梁山首领：")
print(leader)
print("王伦嫉贤妒能被林冲杀害")
leader = "晁盖"
print("第二任梁山首领：")
print(leader)
print("晁盖曾家战役中毒箭身亡")
leader = "宋江"
print("第三任梁山首领：")
print(leader)
print("朝廷诏安赐毒酒，自此再无梁山")

name="托尼·斯塔克"
print("姓名",end = "")
print ('nihao', end = "")
print("Welcome to" , end = "")


print("name")
height=185.3
print("身高（cm）",end="")
number=50
print("战甲数量,",end="")
print(number)
debut="1963"
print("首次登场",end="")
print(debut)
actor="小罗伯特·唐尼"
print("扮演者",end="")
print(actor)

books=["三国演义","水浒传","红楼梦","西游记","镜花缘","封神演义","聊斋志异"]
print(books[2])
subbbooks = books[1:4]
shuihu=books[1]
print(shuihu)
shuihu=books[-6]
print(shuihu)
subbooks=books[1:6]
print(subbooks)
subbooks=books[1:-1]
print(subbooks)

books=["三国演义","水浒传","红楼梦","西游记","镜花缘","封神演义","聊斋志异"]
print(books[2])
books.append("儒林外史")
print(books[-1])
print(books[-2])

books=["三国演义","水浒传","红楼梦","西游记","镜花缘","封神演义","聊斋志异"]
books.insert(4,"儒林外史")
print(books)



col1=["玩具","饮料","唇彩","眉笔"]
col2=["眉笔","粉底液","手办","卡片"]
col3=["手办","手套","粉底液","卡片"]
row=[col1,col2,col3]
c=row[1]
print(c)
print(c[2])

print(row[1][2])
print(row[-1][-1])


Lisa={"name":"Lisa","age":23,"weight":53.3}
print(Lisa)

#取某一信息
w = Lisa["weight"]
print(w)
print(Lisa["weight"])

#更新数值
Lisa["weight"] = 50.3
print(Lisa["weight"])
增添数值
Lisa["birthday"] = "1996-01-03"
print(Lisa)

#删除数据
Lisa.opp("birthday")  #(根据键删除)

Lisa.opp("birthday")
print(Lisa)

students = []
stu1 = {"no": "1234", "name": "张晓明", "age": 23, "nation": "汉", "birthday": "1996-06-07",
        "father": {"name": "张建国", "company": "中国移动总公司", "job": "客户经理"},
        "mother": {"name": "吴艳玲", "company": "师大附中", "job": "教师"}}

students.append(stu1)
print(students)
no = students[-1]["no"]
name = students[-1]["name"]
nation = students[-1]["nation"]
fname = students[-1]["father"]["name"]
print(no + "-" + name + "-" + nation + "-"
+ fname)

stu1 = {"no": "1235", "name": "李玲", "age": 24, "nation": "汉", "birthday": "1995-06-07",
        "father": {"name": "李想", "company": "中国石油总公司", "job": "人事经理"},
        "mother": {"name": "王花", "company": "第一人民医院", "job": "医生"}}

students.append(stu2)
print(students)
print(
    students[-1]["no"] + "-" + students[-1]["name"] + "-" + students[-1]["nation"] + "-" + students[-1]["father"]["ame"])

#循环（while不定次循环）

i = 0
while i < 4:
    print(i * 100)
    i = i + 1
print("循环结束")

i = 1
result = 3
while i <= 10:
    print(result)
    result = result * 3
    i = i + 1

#循环（for定次循环___列表变量）(可读性好)
#for i in range(10, 15)(左闭右开)

    # books=["三国演义","水浒传","红楼梦","西游记","镜花缘","封神演义","聊斋志异"]
    # for book in books:
    #     if book != "镜花缘"
    #         print(book)

    for i in range(10, 15):
        print(i)

    n = 153

    for n in range(100, 1000):
        i = n / 100
    i = int(i)
    j = n / 10 % 10
    j = int(j)
    k = n % 10
    result = i * i * i + j * j * j + k * k * k
    if n == result:
        print(n, end="")
        print("是水仙花数")
    else:
        print(n, end="")
        print("不是水仙花数")

    n = 100
    while n < 1000:
        i = n / 100
        i = int(i)
        j = n / 10 % 10
        j = int(j)
        k = n % 10
        result = i * i * i + j * j * j + k * k * k
        if n == result:
            print(n, end="")
            print("是水仙花数")
        n = n + 1

    col1 = ["玩具", "饮料", "唇彩", "眉笔"]
    col2 = ["眉笔", "粉底液", "手办", "卡片"]
    col3 = ["手办", "手套", "粉底液", "卡片"]
    row = [col1, col2, col3]
    c = row[1]

    for col in row:
        for box in col:
            print(box)
        print("========")

    movies = []
    m = {"year": 1902, "title": "月球之旅", "director": "乔治·梅利斯", "description": "历史上第一部科幻电影"}
    movies.append(m)
    movies.append({"year": 1916, "title": "海底两万里", "director": "理查德·弗莱彻", "description": "第一本水下拍摄的科幻电影"})