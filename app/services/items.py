from app.adapters.dragontail import Dragon


class ItemsService():
    def store(self):
        data = self.__get_data()
        items = self.__parse_data(data)
        return items
        
    def __get_data(self):
        dragon = Dragon()
        response = dragon.get_items()
        data = response['data']
        return data

    def __parse_data(self, data):
        items = []
        for x in data:
            item = {}
            item['name'] = data[x]['name']
            item['description'] = data[x]['description']
            item['gold'] = data[x]['gold']
            item['stats'] = data[x]['stats']
            item['image'] = data[x]['image']
            items.append(item)
        return items

    def __parse_items_by_name(self, items, name):
        for x in range(len(items)):
            if items[x]['name'] == name:
                print(name)
                return items[x]

    def item_by_name(self, name):
        data = self.__get_data()
        items = self.__parse_data(data)
        item = self.__parse_items_by_name(items, name)
        return item