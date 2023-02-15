############################################
#                                          #
#    Intelligence in Animals & Machines    #
#                                          #
############################################
#                        #
#    TURTLE SIMULATOR    #
#                        #
##########################
#
# Institute: University of Sussex
# Supervisor:
#             Prof Paul Graham
#             Dr   Chris Johnson
#
# Script Writer: Equosile (jk488@sussex.ac.uk)
# https://github.com/Equosile/Turtle_Incubation_Simulator
#
#
#
#
###################################################################################
#                                                                                 # 
# The BSD Zero Clause License (0BSD)                                              #
#                                                                                 #
# Copyright (c) 2023 Equosile.                                                    #
#                                                                                 #
# Permission to use, copy, modify, and/or distribute this software for any        #
# purpose with or without fee is hereby granted.                                  #
#                                                                                 #
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH   #
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY     #
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,    #
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM     #
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR   #
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR          #
# PERFORMANCE OF THIS SOFTWARE.                                                   #
#                                                                                 #
###################################################################################
#
#
#
#
# PYTHON3 BUILT-IN LIBRARIES
import multiprocessing
import time
import random
import copy
import math
import turtle

# PYTHON3 EXTERNAL LIBRARIES
import numpy as np

#################
# TURTLE MACROS #
#################
#
# WINDOW SIZE (SIMULATION BOARD)
STRETCH_SCALE = 3
SIZE_MULTIPLIER_WIDTH = 128
SIZE_MULTIPLIER_HEIGHT = 72
BOARD_SIZE = 10
SCREEN_WIDTH = BOARD_SIZE*SIZE_MULTIPLIER_WIDTH
SCREEN_HEIGHT = BOARD_SIZE*SIZE_MULTIPLIER_HEIGHT
#
# COLOURS
bg_colour = "black"
board_colour = "light steel blue"
egg_colour = "antiquewhite"
turtle_colour = "sea green"
indicator_colour_A = "light coral"
indicator_colour_B = "white"
button_colour = "lime"
TYPEFACE = "Courier"
FONT_SIZE_BIG = 16
FONT_SIZE_SMALL = 12
#
# OUTSKIRT WINDOW ---> sim_app
sim_app = turtle.Screen()
sim_app.title("Turtle Simulator by Python 3 Turtle")
sim_app.bgcolor(bg_colour)
sim_app.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
# WINDOW UPDATE MODULE
sim_app.tracer(0)
#
# AGENT VISUAL IMPLEMENTATIONS
turtle_agent_A = turtle.Turtle()
turtle_agent_B = turtle.Turtle()
turtle_agent_C = turtle.Turtle()
turtle_agent_A.speed(0)
turtle_agent_B.speed(0)
turtle_agent_C.speed(0)
turtle_agent_A.shape("circle")
turtle_agent_B.shape("circle")
turtle_agent_C.shape("circle")
turtle_agent_A.color(egg_colour)
turtle_agent_B.color(egg_colour)
turtle_agent_C.color(egg_colour)
turtle_agent_A.shapesize(stretch_wid=1, stretch_len=1)
turtle_agent_B.shapesize(stretch_wid=1, stretch_len=1)
turtle_agent_C.shapesize(stretch_wid=1, stretch_len=1)
turtle_agent_A.penup()
turtle_agent_B.penup()
turtle_agent_C.penup()
turtle_agent_A.goto(-330, 0)
turtle_agent_B.goto(0, 0)
turtle_agent_C.goto(330, 0)
#
# DEBUGGING & INTERFACE FEATURES
turtle_pen_A = turtle.Turtle()
turtle_pen_B = turtle.Turtle()
turtle_pen_C = turtle.Turtle()
turtle_pen_D = turtle.Turtle()
turtle_pen_E = turtle.Turtle()
turtle_pen_A.speed(0)
turtle_pen_B.speed(0)
turtle_pen_C.speed(0)
turtle_pen_D.speed(0)
turtle_pen_E.speed(0)
turtle_pen_A.color(indicator_colour_A)
turtle_pen_B.color(indicator_colour_A)
turtle_pen_C.color(indicator_colour_A)
turtle_pen_D.color(indicator_colour_A)
turtle_pen_E.color(indicator_colour_A)
turtle_pen_A.penup()
turtle_pen_B.penup()
turtle_pen_C.penup()
turtle_pen_D.penup()
turtle_pen_E.penup()
turtle_pen_A.hideturtle()
turtle_pen_B.hideturtle()
turtle_pen_C.hideturtle()
turtle_pen_D.hideturtle()
turtle_pen_E.hideturtle()
turtle_pen_A.goto(-400, -240)
turtle_pen_B.goto(0, -240)
turtle_pen_C.goto(400, -240)
turtle_pen_D.goto(0, 250)
turtle_pen_E.goto(270, 200)
button_play = turtle.Turtle()
button_play.speed(0)
button_play.shape("classic")
button_play.color(button_colour)
button_play.shapesize(stretch_wid=6, stretch_len=6)
button_play.penup()
button_play.goto(300, 280)
str_content_pen_E = "Next Step\n"
turtle_pen_E.write( str_content_pen_E, \
    align="center", font=(TYPEFACE, FONT_SIZE_BIG, "normal") \
)
#
#
#
#
#
# ANALYTICAL-PROCESSING-PART
class Agent:
    def __init__(self, model, enamel_pen, stage, \
                    previous_agent=None, next_agent=None):
        self.model = model
        self.enamel_pen = enamel_pen
        self.stage = stage
        self.vco2 = np.random.uniform(low=0.0, high=1.0)
        self.meta_rate = np.random.uniform(low=0.0, high=1.0)
        self.heart_rate = 50.0 + np.random.uniform(low=-19.0, high=19.0)
        self.growth_rate = 1 + np.random.uniform(low=0.0, high=1.0)
        self.is_pipping = False
        self.hatching_count = 0
    
    def develope(self, temperature):
        self.stage = self.stage + \
                    ( self.growth_rate * temperature * (1 / 26) ) / (2**(1/2)) 
    
    # "env_variables" are as in the followings:
    # index No. 0 = temperature
    # index No. 1 = either "previous_agent.vco2"
    #               or     "next_agent.vco2"
    def metabolise(self, env_variables):
        # Assumption from concepts of basic metabolisms
        self.vco2 = 0.5 + (1.1 * (self.stage / 14)) + \
                    (((1 + self.meta_rate) + (self.heart_rate / 80)) / 2)
        
        # From McGlashan et al.(2011), whichever egg is picked,
        # the VCO2 level is representative for the egg cluster,
        # since all eggs in the cluster shares similar VCO2 level.
        neo_vco2 = (self.vco2 + env_variables[1]) / 2
        
        accelerator = (neo_vco2 - self.vco2) * 1.5
        
        # From McGlashan et al. (2011),
        # treatment group (higher temperature) has higher heart rate.
        self.heart_rate = 80 + (15 * (self.stage / 17)) + \
                            ((env_variables[0] / 26) / 30)
        
        # Assumption from basic metabolism
        #
        # Certain factors are affecting the growth rate
        # to catch up the presence of other hatchings.
        self.growth_rate = 1 + (accelerator + \
                            ((self.heart_rate / 90) + \
                            self.vco2) / 2 \
                            )

    def try_pipping(self):
        if self.stage > 14:
            success_factor = \
                            (self.stage / 14) * \
                            (1 + np.random.uniform(low=0.0, high=1.0))
            if success_factor > 1.9:
                self.is_pipping = True
            else:
                self.is_pipping = False
        else:
            #pass
            self.is_pipping = False
        
        if self.is_pipping:
            self.hatching_count = self.hatching_count + 1
    
    # Until observing, it is unclear about
    # whether the Schrodinger's cat is still alive or not.
    #
    # Observing is crucial.
    def observe(self, tag=''):
        size_int_neoEx = 1
        if self.stage > 0:
            size_neoExpectation = 1 + (self.stage / 5)
            size_int_neoEx = int( size_neoExpectation )
        else:
            size_int_neoEx = 1
        
        str_stage = "{:.4f}".format( self.stage       )
        str_gr    = "{:.4f}".format( self.growth_rate )
        str_hr    = "{:.4f}".format( self.heart_rate  )
        str_vco2  = "{:.4f}".format( self.vco2        )
        str_isPip = str( self.is_pipping  )
        
        bool_hatching = False
        if self.hatching_count > 2:
            bool_hatching = True
        str_hatching = str( bool_hatching )
        
        str_content = ""
        if not bool_hatching:
            str_content = \
                tag + " | Stage      :" + str_stage + '\n' +\
                tag + " | Growth Rate:" + str_gr    + '\n' +\
                tag + " | Heart Rate :" + str_hr    + '\n' +\
                tag + " | VCO2       :" + str_vco2  + '\n' +\
                tag + " | Is pipping?:" + str_isPip + '\n'
                
        else:
            str_content = \
                tag + " | Stage      :" + str_stage    + '\n' +\
                tag + " | Growth Rate:" + str_gr       + '\n' +\
                tag + " | Heart Rate :" + str_hr       + '\n' +\
                tag + " | VCO2       :" + str_vco2     + '\n' +\
                tag + " | Is hatched?:" + str_hatching + '\n'
        
        if bool_hatching:
            self.model.shape("turtle")
        
        self.model.shapesize( \
            stretch_wid=size_int_neoEx, \
            stretch_len=size_int_neoEx + 1)
        
        print( str_content )
        self.enamel_pen.clear()
        self.enamel_pen.write( str_content, \
            align="center", font=(TYPEFACE, FONT_SIZE_SMALL, "normal") \
        )






#########################################            
# Constant Temperature Regime Emulation #
#########################################

room_temperature = 30

analysis_agent_A = Agent(turtle_agent_A, turtle_pen_A, -10.1)
analysis_agent_B = Agent(turtle_agent_B, turtle_pen_B, 0.01, analysis_agent_A)
analysis_agent_A.next_agent = analysis_agent_B
analysis_agent_C = Agent(turtle_agent_C, turtle_pen_C, 0.05, analysis_agent_B)
analysis_agent_B.next_agent = analysis_agent_C

switch_A = True
time_rp_A = -1
time_ep_A = -1
switch_B = True
time_rp_B = -1
time_ep_B = -1
switch_C = True
time_rp_C = -1
time_ep_C = -1

time_sp = time.time()
int_iteration = 0

def emul_cycle():
    global switch_A
    global switch_B
    global switch_C
    global time_rp_A
    global time_rp_B
    global time_rp_C
    global time_ep_A
    global time_ep_B
    global time_ep_C
    global time_sp
    global int_iteration
    global analysis_agent_A
    global analysis_agent_B
    global analysis_agent_C
    global room_temperature
    
    # One-Simulation-Time-Step == One-Iteration in For-Loop
    multiprocessing.Process( \
                            target= \
                            analysis_agent_A.metabolise([ \
                                room_temperature, \
                                analysis_agent_B.vco2]) \
                            )
    multiprocessing.Process(target= \
                            analysis_agent_A.develope(room_temperature))
    multiprocessing.Process( \
                            target= \
                            analysis_agent_B.metabolise([ \
                                room_temperature, \
                                analysis_agent_A.vco2]) \
                            )
    multiprocessing.Process(target= \
                            analysis_agent_B.develope(room_temperature))
    multiprocessing.Process( \
                            target= \
                            analysis_agent_C.metabolise([ \
                                room_temperature, \
                                analysis_agent_B.vco2]) \
                            )
    multiprocessing.Process(target= \
                            analysis_agent_C.develope(room_temperature))
    
    if int_iteration > 5:
        multiprocessing.Process(target=analysis_agent_A.try_pipping())
        multiprocessing.Process(target=analysis_agent_B.try_pipping())
        multiprocessing.Process(target=analysis_agent_C.try_pipping())
    
    if analysis_agent_A.is_pipping:
        if switch_A:
            time_rp_A = time.time()
            switch_A = False
    
    if analysis_agent_B.is_pipping:
        if switch_B:
            time_rp_B = time.time()
            switch_B = False
    
    if analysis_agent_C.is_pipping:
        if switch_C:
            time_rp_C = time.time()
            switch_C = False
    
    
    stage_A = analysis_agent_A.stage
    stage_B = analysis_agent_B.stage
    stage_C = analysis_agent_C.stage
    stage_group = (stage_A + stage_B + stage_C) / 3
    stage_to_week = stage_group * 0.4
    str_week = "{:.2f}".format( stage_to_week )
    str_iteration = str( int_iteration )
    
    print("Week " + str_week + " ( " + str_iteration + " ) Report:")
    analysis_agent_A.observe("Turtle_A")
    if not switch_A:
        time_ep_A = time_rp_A - time_sp
        print("Hatching Real-time Period:", time_ep_A)
    
    analysis_agent_B.observe("Turtle_B")
    if not switch_B:
        time_ep_B = time_rp_B - time_sp
        print("Hatching Real-time Period:", time_ep_B)
        
    analysis_agent_C.observe("Turtle_C")
    if not switch_C:
        time_ep_C = time_rp_C - time_sp
        print("Hatching Real-time Period:", time_ep_C)
    
    print("")
    
    str_content_pen_D = \
        "Week " + str_week + " ( " + str_iteration + " )\n" \
        "Room Temperature: " + str( room_temperature ) + "\u00B0C"
    turtle_pen_D.clear()
    turtle_pen_D.write( str_content_pen_D, \
        align="center", font=(TYPEFACE, FONT_SIZE_BIG, "normal") \
    )
    
    int_iteration = int_iteration + 1





# Assigning Properties...
#
# BUTTON FUNCTION FOR THE NEXT SIMULATION STEP
def btn_fnc_next(x, y):
    emul_cycle()
    button_play.onrelease( btn_fnc_next )

button_play.onrelease( btn_fnc_next )

########
# MAIN #
########
while True:
    sim_app.update()
    
    
    
