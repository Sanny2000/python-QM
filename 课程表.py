#用来保存课程的所有信息
str1 ='软件测试实训'
str2 ='java web 编程基础'
str3 ='软件测试'
str4 ='python基础'
str5 ='软件项目管理'
str6='计算机网络技术'
str7 ='军事课'
str8='毛泽东思想'
str9 ='职业发展'
str10='形式与政策'
str11='创新创业基础'
str12='心里健康教育'
time1 ='第一节'
time2='第二节'
time3 ='第三节'
time4 ='第四节'
time5='第五节'
time6 ='第六节'
time7 ='第七节'
time8='第八节'
time9='第九节'
time10='第九节'
week1 ='星期一'
week2 ='星期二'
week3 ='星期三'
week4 ='星期四'
week5 ='星期五'
courseInfos=[[time1,str1,str1,str1,str3,str4],
          [time2,str5,str1,str2,str3,str4],
          [time3,str1,str1,str1,str3,str4],
          [time4,str5,str1,str2,str3,str4],
          [time5,str1,str6,str1,str9,str9],
          [time6,str1,str1,str8,str9,str9],
          [time7,str1,str6,str10," "," "],
          [time8,str1,str1,str1," "," "],
          [time9,"","","","","",str7],
          [time10,"","","","","",str7]
          ]
#打印功能提示
def printMenu():
    print("="*30)
    print(" 课程表系统 ")
    print("1.添加课表信息")
    print("2.删除课表信息")
    print("3.修改课表信息")
    print("4.显示所有课表信息")
    print("0.退出系统")
    print("="*30)
#添加一个课表信息
def addCourseInfo():
    # 提示并获取上课时间
    dtime = input("请输入时间（第几节）：")
    # 提示并获取上课日期
    wtime = input("请输入日期(星期几)：")
    # 提示并获取课程信息
    kinfo = input("请输入课程信息：")
    newInfo = {}
    newInfo['dtime'] = dtime
    newInfo['wtime'] = wtime
    newInfo['kinfo'] = kinfo
    if dtime==time1:
        if wtime==week1:
            courseInfos[0][1] =kinfo
        elif wtime==week2:
            courseInfos[0][2] =kinfo
        elif wtime==week3:
            courseInfos[0][3] =kinfo
        elif wtime==week4:
            courseInfos[0][4] =kinfo
        elif wtime==week5:
            courseInfos[0][5] =kinfo
    elif dtime==time2:
        if wtime==week1:
            courseInfos[1][1] =kinfo
        elif wtime==week2:
            courseInfos[1][2] =kinfo
        elif wtime==week3:
            courseInfos[1][3] =kinfo
        elif wtime==week4:
            courseInfos[1][4] =kinfo
        elif wtime==week5:
            courseInfos[1][5] =kinfo
    elif dtime == time3:
        if wtime == week1:
            courseInfos[2][1] = kinfo
        elif wtime == week2:
            courseInfos[2][2] = kinfo
        elif wtime == week3:
            courseInfos[2][3] = kinfo
        elif wtime == week4:
            courseInfos[2][4] = kinfo
        elif wtime == week5:
            courseInfos[2][5] = kinfo
    elif dtime ==time4:
        if wtime == week1:
            courseInfos[3][1] = kinfo
        elif wtime == week2:
            courseInfos[3][2] = kinfo
        elif wtime == week3:
            courseInfos[3][3] = kinfo
        elif wtime == week4:
            courseInfos[3][4] = kinfo
        elif wtime == week5:
            courseInfos[3][5] = kinfo
    elif dtime ==time5:
        if wtime == week1:
            courseInfos[4][1] = kinfo
        elif wtime == week2:
            courseInfos[4][2] = kinfo
        elif wtime == week3:
            courseInfos[4][3] = kinfo
        elif wtime == week4:
            courseInfos[4][4] = kinfo
        elif wtime == week5:
            courseInfos[4][5] = kinfo
    elif dtime==time6:
        if wtime == week1:
            courseInfos[5][1] = kinfo
        elif wtime == week2:
            courseInfos[5][2] = kinfo
        elif wtime == week3:
            courseInfos[5][3] = kinfo
        elif wtime == week4:
            courseInfos[5][4] = kinfo
        elif wtime == week5:
            courseInfos[5][5] = kinfo
    elif dtime==time7:
        if wtime == week1:
            courseInfos[6][1] = kinfo
        elif wtime == week2:
            courseInfos[6][2] = kinfo
        elif wtime == week3:
            courseInfos[6][3] = kinfo
        elif wtime == week4:
            courseInfos[6][4] = kinfo
        elif wtime == week5:
            courseInfos[6][5] = kinfo
    elif dtime==time8:
        if wtime == week1:
            courseInfos[7][1] = kinfo
        elif wtime == week2:
            courseInfos[7][2] = kinfo
        elif wtime == week3:
            courseInfos[7][3] = kinfo
        elif wtime == week4:
            courseInfos[7][4] = kinfo
        elif wtime == week5:
            courseInfos[7][5] = kinfo
    elif dtime==time9:
        if wtime == week1:
            courseInfos[8][1] = kinfo
        elif wtime == week2:
            courseInfos[8][2] = kinfo
        elif wtime == week3:
            courseInfos[8][3] = kinfo
        elif wtime == week4:
            courseInfos[8][4] = kinfo
        elif wtime == week5:
            courseInfos[8][5] = kinfo
    elif dtime==time10:
        if wtime == week1:
            courseInfos[9][1] = kinfo
        elif wtime == week2:
            courseInfos[9][2] = kinfo
        elif wtime == week3:
            courseInfos[9][3] = kinfo
        elif wtime == week4:
            courseInfos[9][4] = kinfo
        elif wtime == week5:
            courseInfos[9][5] = kinfo
#删除一个课表信息
def removeInfo():
    dtime =input("请输入需要删除的课表信息天时间（第几节）：")
    wtime =input("请输入需要删除的课表信息周时间（星期几）：")
    if dtime==time1:
        if wtime==week1:
            courseInfos[0][1] =''
        elif wtime==week2:
            courseInfos[0][2] =''
        elif wtime==week3:
            courseInfos[0][3] =''
        elif wtime==week4:
            courseInfos[0][4] =''
        elif wtime==week5:
            courseInfos[0][5] =''
    elif dtime==time2:
        if wtime==week1:
            courseInfos[1][1] =''
        elif wtime==week2:
            courseInfos[1][2] =''
        elif wtime==week3:
            courseInfos[1][3] =''
        elif wtime==week4:
            courseInfos[1][4] =''
        elif wtime==week5:
            courseInfos[1][5] =''
    elif dtime == time3:
        if wtime == week1:
            courseInfos[2][1] = ''
        elif wtime == week2:
            courseInfos[2][2] = ''
        elif wtime == week3:
            courseInfos[2][3] = ''
        elif wtime == week4:
            courseInfos[2][4] = ''
        elif wtime == week5:
            courseInfos[2][5] = ''
    elif dtime ==time4:
        if wtime == week1:
            courseInfos[3][1] = ''
        elif wtime == week2:
            courseInfos[3][2] = ''
        elif wtime == week3:
            courseInfos[3][3] = ''
        elif wtime == week4:
            courseInfos[3][4] = ''
        elif wtime == week5:
            courseInfos[3][5] = ''
    elif dtime ==time5:
        if wtime == week1:
            courseInfos[4][1] = ''
        elif wtime == week2:
            courseInfos[4][2] = ''
        elif wtime == week3:
            courseInfos[4][3] = ''
        elif wtime == week4:
            courseInfos[4][4] = ''
        elif wtime == week5:
            courseInfos[4][5] = ''
    elif dtime==time6:
        if wtime == week1:
            courseInfos[5][1] = ''
        elif wtime == week2:
            courseInfos[5][2] = ''
        elif wtime == week3:
            courseInfos[5][3] = ''
        elif wtime == week4:
            courseInfos[5][4] = ''
        elif wtime == week5:
            courseInfos[5][5] = ''
    elif dtime==time7:
        if wtime == week1:
            courseInfos[6][1] = ''
        elif wtime == week2:
            courseInfos[6][2] = ''
        elif wtime == week3:
            courseInfos[6][3] = ''
        elif wtime == week4:
            courseInfos[6][4] = ''
        elif wtime == week5:
            courseInfos[6][5] = ''
    elif dtime==time8:
        if wtime == week1:
            courseInfos[7][1] = ''
        elif wtime == week2:
            courseInfos[7][2] = ''
        elif wtime == week3:
            courseInfos[7][3] = ''
        elif wtime == week4:
            courseInfos[7][4] = ''
        elif wtime == week5:
            courseInfos[7][5] = ''
    elif dtime==time9:
        if wtime == week1:
            courseInfos[8][1] = ''
        elif wtime == week2:
            courseInfos[8][2] = ''
        elif wtime == week3:
            courseInfos[8][3] = ''
        elif wtime == week4:
            courseInfos[8][4] = ''
        elif wtime == week5:
            courseInfos[8][5] = ''
    elif dtime==time10:
        if wtime == week1:
            courseInfos[9][1] = ''
        elif wtime == week2:
            courseInfos[9][2] = ''
        elif wtime == week3:
            courseInfos[9][3] = ''
        elif wtime == week4:
            courseInfos[9][4] = ''
        elif wtime == week5:
            courseInfos[9][5] = ''
# 显示课表信息
def showCourseInfo():
    print("=" * 30)
    print("课表信息信息如下:")
    print("=" * 30)
    print("时间\t\t    |星期一\t\t        |星期二\t\t        |星期三\t \t        |星期四\t\t    |星期五   \t    |")
    for i in courseInfos:
        print("-"*100)
        for j in i:
                print(j.ljust(10,' ')+"\t|",end='')

        print('')
def main():
    while True:
        printMenu()
        key = input("请输入功能对应的数字")
        if key == '1':
            addCourseInfo()
        elif key=='2':
            removeInfo()
        elif key == '3':
            addCourseInfo()
        elif key == '4':
            showCourseInfo()
        elif key=='0':
            break
main()
