import streamlit as st
with st.form (" tables "):
    a=st.number_input("enter table")
    u=st.form_submit_button("view table")
#c=int(a)
if u:
    
    for i in range(1, 11):
        st.write(f"{a}*{i}={i*a}")