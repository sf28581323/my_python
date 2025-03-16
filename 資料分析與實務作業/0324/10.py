list = ['資工', '電機', '化工']

class Myschool:
    
    def __init__(self, title):
        self.title = '東海大學'

    def departments():

        global list

        print('現在有的系所為:', list)

    def add():

        global list

        n = input('請輸入要新增的系所:')

        list.append(n)

        print('現在有的系所為:', list)

    def omit():

        global list

        m = input('請輸入要刪除的系所:')

        list.remove(m)

        print('現在有的系所為:', list)
        

Myschool.departments()
Myschool.add()
Myschool.omit()  
