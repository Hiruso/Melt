class Profession:
        """Class นี้คือข้อมูลของตัวละคร มี health,stamina,defs"""
        def __init__(this, health, stamina, defs):
            this.health = health
            this.stamina = stamina
            this.defent = defs

class teacher(Profession):
    def __init__(this, health, stamina, defs):
        super().__init__(health, stamina, defs)
