def greedy(radios, cities):

    greedy_radios = set()
    while cities:
        greedy_choose = None
        city_cover = set()
        for radio, area in radios.items():
            cover = cities & area
            if len(cover) > len(city_cover):
                greedy_choose = radio
                city_cover = cover
        cities -= city_cover
        greedy_radios.add(greedy_choose)
    return greedy_radios

cities = set(['台北', '基隆', '桃園', '新竹', '苗栗',
              '雲林', '台中', '南投', '嘉義', '台南',
              '高雄', '屏東', '宜蘭', '花蓮', '台東']
              )

radios = {}
radios['電台1'] = set(['新竹', '台中', '嘉義'])
radios['電台2'] = set(['基隆', '新竹', '台北'])
radios['電台3'] = set(['桃園', '台中', '台南'])
radios['電台4'] = set(['台中', '南投', '嘉義'])
radios['電台5'] = set(['台南', '高雄', '屏東'])
radios['電台6'] = set(['宜蘭', '花蓮', '台東'])
radios['電台7'] = set(['苗栗', '雲林', '嘉義', '南投'])

print(greedy(radios, cities))
