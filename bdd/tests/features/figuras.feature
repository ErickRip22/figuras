Feature: Calcular Area
	Como usuario del sistema
	deseo realizar el calculo de diferetes figuras
	para obtener el area preciso

	Scenario: Area cuadrado 2
		Dado que ingreso el lado "2"
		cuando realizo la operacion
		entonces obtengo el area "4"

	Scenario: Area rectangulo de 7 por 5
		Dado que ingreso los lados "7" por "5"
		cuando realizo la operacion
		entonces obtengo el area "35"

	Scenario: Area de circulo de 10 de radio
		Dado que ingreso el radio "10"
		cuando realizo la operacion
		entonces obtengo el area "98.69604401089359"

	Scenario: Area trapecio 3 4 y 5
		Dado que ingreso la base menor "4", base mayor "5.0" y altura "3"
		cuando realizo la operacion
		entonces obtengo el area "13.5"
