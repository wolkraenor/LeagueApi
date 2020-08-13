from app.adapters.dragontail import Dragon


class ChampionsService():

    dragon = Dragon()

    def store(self):
        response = self.dragon.get_champions()
        data = response['data']
        champions = []
        for x in data:
            champions.append(x)
        return champions
    
    def champion_data(self, name):
        response = self.dragon.get_champions()
        data = response['data']
        champion = 'Not found'
        for x in data:
            if name == x:
                champion = {name: data[x]}

        return champion
