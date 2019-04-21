import random
import copy

Vitorias = []
for i in xrange(0,29):
    Vitorias.append(0)
Fronteiras = [[2,3,5,6,8,10,14,15,16,17,18,19,20,21,24,25,26,28]]
Fronteiras.append([4,22])
Fronteiras.append([17,26,5,0])
Fronteiras.append([14,0])
Fronteiras.append([11,14,22,23,1])
Fronteiras.append([2,26,17,18,13,8,9,27,0])
Fronteiras.append([18,20,15,17,0])
Fronteiras.append([9,13])
Fronteiras.append([5,13,19,0])
Fronteiras.append([27,11,12,13,5,7])
Fronteiras.append([0,18,14,27])
Fronteiras.append([4,14,27,9,12,22])
Fronteiras.append([11,9,25,16])
Fronteiras.append([5,19,8,25,9,12,7])
Fronteiras.append([11,27,10,4,23,3,0])
Fronteiras.append([6,17,20,0])
Fronteiras.append([25,12,24,0])
Fronteiras.append([15,2,5,18,6,0])
Fronteiras.append([10,27,6,17,5,0])
Fronteiras.append([13,25,8,0])
Fronteiras.append([6,15,0])
Fronteiras.append([24,28,0])
Fronteiras.append([1,4,11])
Fronteiras.append([14,4])
Fronteiras.append([21,16,0])
Fronteiras.append([19,16,12,13,0])
Fronteiras.append([0,2,5])
Fronteiras.append([5,18,10,9,11,14])
Fronteiras.append([21,0])
Estados = []
Controlado = []
Estados.insert(0, "XXXXX")
Controlado.insert(0, 0)
Estados.insert(1, "Acre")
Controlado.insert(1, 22)
Estados.insert(2, "Alagoas")
Controlado.insert(2, 16)
Estados.insert(3, "Amapa")
Controlado.insert(3, 16)
Estados.insert(4, "Amazonas")
Controlado.insert(4, 22)
Estados.insert(5, "Bahia")
Controlado.insert(5, 7)
Estados.insert(6, "Ceara")
Controlado.insert(6, 20)
Estados.insert(7, "Distrito Federal")
Controlado.insert(7, 21)
Estados.insert(8, "Espirito Santo")
Controlado.insert(8, 19)
Estados.insert(9, "Goias")
Controlado.insert(9, 7)
Estados.insert(10, "Maranhao")
Controlado.insert(10, 16)
Estados.insert(11, "Mato Grosso")
Controlado.insert(11, 21)
Estados.insert(12, "Mato Grosso do Sul")
Controlado.insert(12, 7)
Estados.insert(13, "Minas Gerais")
Controlado.insert(13, 21)
Estados.insert(14, "Para")
Controlado.insert(14, 7)
Estados.insert(15, "Paraiba")
Controlado.insert(15, 19)
Estados.insert(16, "Parana")
Controlado.insert(16, 7)
Estados.insert(17, "Pernambuco")
Controlado.insert(17, 16)
Estados.insert(18, "Piaui")
Controlado.insert(18, 7)
Estados.insert(19, "Rio de Janeiro")
Controlado.insert(19, 21)
Estados.insert(20, "Rio Grande do Norte ")
Controlado.insert(20, 20)
Estados.insert(21, "Rio Grande do Sul")
Controlado.insert(21, 21)
Estados.insert(22, "Rondonia")
Controlado.insert(22, 22)
Estados.insert(23, "Roraima")
Controlado.insert(23, 22)
Estados.insert(24, "Santa Catarina")
Controlado.insert(24, 21)
Estados.insert(25, "Sao Paulo")
Controlado.insert(25, 21)
Estados.insert(26, "Sergipe")
Controlado.insert(26, 16)
Estados.insert(27, "Tocantins")
Controlado.insert(27, 7)
Estados.insert(28, "Cisplatina")
Controlado.insert(28, 21)
for i in xrange(0,29):
	Controlado[i] = i
backup = Controlado[:]
for i in xrange(0,10000):
	terminou = 0
	vencedor = 0
	while (terminou != 1):
		atacante = 0
		text = "por Terra"
		while (atacante == 0):
		    atacante = random.choice(range(1,29))
		atacado = random.choice(Fronteiras[atacante])
		if Controlado[atacante] == Controlado[atacado]:
			continue
		while atacado == 0:
		    atacado = random.choice(Fronteiras[0])
		    text = "pela Agua"

		#print Estados[atacante],"(",Estados[Controlado[atacante]],")", "ataca", text, Estados[atacado],"(",Estados[Controlado[atacado]],")"
		
		Controlado[atacado] = Controlado[atacante]
		vencedor = Controlado[1]
		itercontrol = iter(Controlado)
		next(itercontrol)
		next(itercontrol)
		terminou = 1
		for i in itercontrol:
			if i != vencedor:
				terminou = 0
	#print "Vencedor:", Estados[vencedor]
	Vitorias[vencedor] += 1
	Controlado = backup[:]

print "Vitorias"
for i in xrange(0,29):
	if (Vitorias[i] != 0):
		print Estados[i], Vitorias[i]
