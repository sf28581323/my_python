msg = '我喜歡看小龍女與楊過，不僅因為小龍女美麗，楊過在戲中所扮演的角色更是讓我喜歡。'

while True:
  
    s = str(input('請輸入搜尋字串:'))

    print('所搜尋字串 %s 共出現' % s, msg.count(s), '次')

    print('')

    n = str(input('是否繼續，輸入Y或y則程式繼續，否則結束:'))

    print('')

    if n  != 'Y' and n  != 'y':

        break

