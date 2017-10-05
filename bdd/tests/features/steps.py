# -*- coding: utf-8 -*-
from lettuce import step, world
from fig import Figuras

@step(u'cuando realizo la operacion')
def cuando_realizo_la_operacion(step):
    pass

@step(u'Dado que ingreso el lado "([^"]*)"')
def dado_que_ingreso_el_lado_group1(step, lado):
    world.figs = Figuras()
    world.figs.calcular_area_cuadrado(int(lado))

@step(u'entonces obtengo el area "([^"]*)"')
def entonces_obtengo_el_area_group1(step, esperado):
    obtenido =  world.figs.get_area()
    assert float(esperado) == obtenido, 'El resultado esperado es' + esperado + ' y el obtenido es ' + obtenido

@step(u'Dado que ingreso los lados "([^"]*)" por "([^"]*)"')
def dado_que_ingreso_los_lados_group1_por_group2(step, num1, num2):
    world.figs = Figuras()
    world.figs.calcular_area_rectangulo(int(num1), int(num2) + 0.0)
@step(u'Dado que ingreso el radio "([^"]*)"')
def dado_que_ingreso_el_radio_group1(step, radio):
	world.figs = Figuras()
	world.figs.calcular_area_circulo(int(radio))
@step(u'Dado que ingreso la base menor "([^"]*)", base mayor "([^"]*)" y altura "([^"]*)"')
def dado_que_ingreso_la_base_menor_group1_base_mayor_group2_y_altura_group3(step, basema, baseme, altura):
	world.figs = Figuras()
	world.figs.calcular_area_trapecio(float(altura), float(basema), float(baseme))