from infras import Infra

class Buildings:
    def __init__(self,id_building,liste_infras:list[Infra]):
        self.id_building = id_building
        self.liste_infras = liste_infras

    def get_building_difficulty(self):
        difficulty = 0
        for infra in self.list_infras:
            difficulty+=infra.get_infra_difficulty()
        return difficulty
    
    def __str__(self):
        return f"{self.id_building,self.liste_infras}"
        
