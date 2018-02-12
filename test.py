from soccersimulator import SoccerTeam, Simulation, Player
from soccersimulator import show_simu
from module.Strategy import *

## Creation d'une equipe
pyteam = SoccerTeam(name="PyTeam")
thon = SoccerTeam(name="ThonTeam")
pyteam.add("PyPlayer",DefenseurStrategy())
thon.add("ThonPlayer",FonceurStrategy())


#Creation d'une partie
simu = Simulation(pyteam,thon)
#Jouer et afficher la partie
show_simu(simu)


