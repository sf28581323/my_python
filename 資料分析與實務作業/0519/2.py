import pygal.maps.world
worldMap = pygal.maps.world.World()
worldMap.title = 'Populations in Europe/Africa/North America'
worldMap.add('Europe',{'fr':60762406,
                       'se':1011781,
                       'ch':71847981})
worldMap.add('Africa',{'eg':67649043,
                       'cg':49626496,
                       'za':44000833})
worldMap.add('Europe',{'us':282162848,
                       'ca':30770661,
                       'mx':99959895})
worldMap.render_to_file('out_21_17.svg')
