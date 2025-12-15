
class Infra:
    def __init__(self,infra_id,longueur,nb_maisons,infra_state):
        self.infra_id = infra_id
        self.longueur = longueur
        self.nb_maisons = nb_maisons
        self.infra_state =infra_state
    
    def repair_infra(self):
        self.infra_state = 'infra_intacte'

    def get_infra_difficulty(self):
        return self.longueur /self.nb_maisons

    