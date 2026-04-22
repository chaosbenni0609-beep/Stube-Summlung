from numpy import *
import streamlit as st
from random import * 
User_in = []
User_in.append(st.text_input("was ist dein beruf /studium/Ausbildung",))

User_in.append(st.slider("Wie gerne arbeite ich in einem Labor?",1,5,3))
User_in.append(st.slider("Wie gerne arbeite ich in einem Museum?",1,5,3))
User_in.append(st.slider("Ich arbeite gerne mit Kindern",1,5,3))
User_in.append(st.slider("Ich arbeite gerne mit Menschen",1,5,3))
User_in.append(st.slider("Ich arbeite gerne mit Tieren",1,5,3))
User_in.append(st.slider("Ich mag es kreativ zu sein",1,5,3))
User_in.append(st.slider("Ich spreche gerne andere Sprachen",1,5,3))
User_in.append(st.slider("Ich mag es lange in der Natur zu sein",1,5,3))
User_in.append(st.slider("Ich arbeite gerne mit Computern",1,5,3))
User_in.append(st.slider("Ich mag es mit Zahlen zu arbeiten",1,5,3))
User_in.append(st.slider("Ich arbeite gerne allein",1,5,3))
User_in.append(st.slider("Ich mag Routine",1,5,3))
User_in.append(st.slider("Ich löse gerne Probleme",1,5,3))
User_in.append(st.slider("Ich verfasse gerne Texte",1,5,3))
User_in.append(st.slider("Ich mag es mit meinen Händen zu arbeiten",1,5,3))
User_in.append(st.slider("Ich mag es mich körperlich zu betätigen",1,5,3))
User_in.append(st.slider("Ich mag es vor Leuten zu sprechen",1,5,3))
User_in.append(st.slider("Ich mag es Verantwortung zu übernehmen",1,5,3))
User_in.append(st.slider("Mir ist es wichtig Menschen oder Tieren zu helfen (biologisch)",1,5,3))
User_in.append(st.slider("Ich mag es neue Themen zu erfahren",1,5,3))
User_in.append(st.slider("Ich arbeite gerne Experimente durchzuführen",1,5,3))
User_in.append(st.slider("Ich setze mich gerne mit theoretischen Fragen auseinander",1,5,3))
User_in.append(st.slider("Ich setze gerne meine eigenen Ideen um",1,5,3))
User_in.append(st.slider("Ich beschäftige mich gerne mit Kunst, Musik oder Literatur",1,5,3))
User_in.append(st.slider("Ich lese gerne wissenschaftliche Texte",1,5,3))
User_in.append(st.slider("Ich diskutiere gerne",1,5,3))
User_in.append(st.slider("Ich setze mich gerne mit anderen Kulturen auseinander",1,5,3))
User_in.append(st.slider("Ich beschäftige mich gerne mit Geschichte",1,5,3))
User_in.append(st.slider("Ich koordiniere oder sortiere gerne",1,5,3))
User_in.append(st.slider("Ich arbeite gerne von verschiedenen Orten",1,5,3))
User_in.append(st.slider("Ich gehe/würde gerne oft auf Arbeitsreisen gehen",1,5,3))

User_in_format = ','.join(User_in)

st.write(User_in)


