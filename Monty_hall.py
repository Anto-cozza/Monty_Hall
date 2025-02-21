import streamlit as st
from random import randint
import matplotlib.pyplot as plt
import numpy as np
from time import sleep
from random import shuffle, choice

"""
# Monty Hall Problem

Hi dear player, we have three doors! 
Behind one of them there is a car, behind the other a goat
"""

if not "exps" in st.session_state:
    st.session_state.exps = []
    
if not "doors" in st.session_state:
    st.session_state.doors = [True, False, False]
    shuffle(st.session_state.doors)

if not "monty_choose" in st.session_state:
    st.session_state.monty_choose = False 

if not "opened_door" in st.session_state:
    st.session_state.opened_door = None
    
st.write("doors:", st.session_state.doors)

chosen_door = st.number_input("Door", min_value = 0, max_value = 2, step = 1)

st.write("You chose door number", chosen_door)

prize_door = st.session_state.doors.index(True)

doors_available_to_reveal = set([0,1,2]) - set([chosen_door]) - set([prize_door])
    
st.write(doors_available_to_reveal)

if(not st.session_state.monty_choose):
    if(st.button("Monty, please open a door!")):
        st.session_state.opened_door = choice(list(doors_available_to_reveal))
        st.session_state.monty_choose = True
        st.rerun()
else: 
        st.write("Monty opened", st.session_state.opened_door)

if(st.button("open my door")):
    if st.session_state.doors[chosen_door] == True:
        st.balloons()
        st.session_state.exps.append(True)
    else:
        st.write("You loose!")
        st.session_state.exps.append(False)

if(st.button("New game")):
    shuffle(st.session_state.doors)
    st.session_state.monty_choose = False
    st.session_state.opened_door = None
    st.rerun()

st.write(st.session_state.exps)

estimate_prob = st.session_state.exps.count(True)/len(st.session_state.exps)
st.write(estimate_prob)

labels = 'win', 'loose'
sizes = [st.session_state.exps.count(True), st.session_state.exps.count(False)]
    
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels = labels, autopct = '%1.1f%%', shadow = True, startangle = 90)
ax1.axis('equal')  
st.pyplot(fig1)

st.write("number of experiments so far:", len(st.session_state.exps))
