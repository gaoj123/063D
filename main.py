from display import *
from draw import *
from parser2 import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print

##RUNS MR. DW's SCRIPT
#parse_file( 'script', edges, transform, screen, color )

##RUNS MY SCRIPT: TRAFFIC LIGHT
parse_file( 'script2', edges, transform, screen, color )
