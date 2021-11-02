init python:
    class Profession:
        """Class นี้คือข้อมูลของตัวละคร มี health,stamina,defs"""
        def __init__(this, health, stamina, defs):
            this.health = health
            this.stamina = stamina
            this.defent = defs


    class Melt(Profession):
        def __init__(this, health, stamina, defs, heat):
            super().__init__(health, stamina, defs)
            this.heating = heat

    class NormalPeople(Profession):


    class GoodPeople
