# Turtle Incubation Simulator


To Find Metabolic Clue for Embryonic Communication Amongst Freshwater Turtles


---


```
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
```


---


## Introduction


The given project is to emulate embryonic communicational phenomena amongst baby turtles inside their eggs.


The simulation design is highly inspired by the precedent research by McGlashan et al. (2011). On top of their experimental set-up, this model has made an assumption where there would be certain factors about $VCO_2$ as a clue of the synchronised hatchings.


The simulation from this model design has shown the promising probability where turtle embryos in rudimentary stages can catch up the advanced siblings.


The front-end is illustrated by the Python 3 Turtle library. Some Python development environments like Debian 11 (Bullseye) ought to additionally install python3-tk for the back-end processing of Python 3 Turtle.


In order to try the simulator, the following command would be executed within proper Python development environments (e.g. Anaconda).


<br>


```
$> python embryo-sync.py
```


---


## Method


Each agent (an egg) can detect not only environmental $VCO_2$ levels but also its own individual $VCO_2$ levels. From these gaps the agents can measure its relative development stages. If the development stage is too late compared to the environment, the agent can accelerate the metabolism to catch up the embryonic development.


---


## Project Aim


The project goal is to figure out appropriate formulas of the metabolism when it comes to synchronised hatchings.


---


## Intermediate Report


- 4 Simulation Stages $\approx$ 1 Real-life Week


- $Acc = (VCO_2$<sub>env</sub> $- VCO_2$<sub>self</sub>) $* a$


- $Grow_{rate} = 1 + (Acc + (\frac{heart_{rate}}{c} + r)) * u$


---


## Reference


Eckhardt, R. (1987). Stan Ulam, John von Neumann, and the Monte Carlo method.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Los Alamos Science (15): 131???137.


<br>


McGlashan, J.K., Spencer, R., Old, J.M. (2011). Embryonic communication in the nest:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; metabolic responses of reptilian embryos to developmental rates of siblings.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; doi:10.1098/rspb.2011.2074.


<br>


Rusli, M.J., Booth, D.T., Joseph, J. (2016). Synchronous activity lowers the energetic cost of

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; nest escape for sea turtle hatchlings. Nature 411: 476???480.


---
