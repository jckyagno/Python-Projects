


# parent class
class boardgame:
    name = "Unknown"
    genre = "Unknown"
    numberOfPlayers = "Unknown"
    averageGameMinutes = None
    coop = True

    def information(self):
        msg = "\nName: {} \nGenre: {}\nNumber of Players: {}\nAverage Game Time (in Minutes): {}\nCo-operative?: {}".format(self.name,self.genre,self.numberOfPlayers,self.averageGameMinutes,self.coop)
        return msg

# child class instance
class Scythe(boardgame):
    name = "Scythe"
    genre = "Strategy"
    numberOfPlayers = "1-5"
    averageGameMinutes = "115"
    coop = False

    def intro(self):
        msg = "\nIt is a time of unrest in 1920s Europa. The ashes from the first great war \
        \nstill darken the snow. The capitalistic city-state known simply as “The Factory”, \
        \nwhich fueled the war with heavily armored mechs, has closed its doors, drawing the\
        \nattention of several nearby countries.\n"
        return msg

# another child class instance
class Champions_of_Midgard(boardgame):
    name = "Champions of Midgard"
    genre = "Strategy"
    numberOfPlayers = "2-4"
    averageGameMinutes = "90"
    coop = False

    def summary(self):
        msg = "\nChampions of Midgard is a middleweight, Viking-themed, worker placement game \
        \nwith dice rolling in which players are leaders of Viking clans who have traveled to \
        \nan embattled Viking harbor town to help defend it against the threat of trolls, draugr,\
        \nand other mythological Norse beasts.\n"
        return msg



if __name__ == "__main__":
    Scythe = Scythe()
    print(Scythe.information())
    print(Scythe.intro())

    CoM = Champions_of_Midgard()
    print(CoM.information())
    print(CoM.summary())
