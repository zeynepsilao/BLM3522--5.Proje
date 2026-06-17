import streamlit as st
import pandas as pd
import random
import time

st.title("Akıllı Şehir Sensör Paneli")
placeholder = st.empty()

data = []
while True:
    new_data = {"sicaklik": random.uniform(20, 30), "nem": random.uniform(30, 60)}
    data.append(new_data)
    if len(data) > 20: data.pop(0) 
    
    df = pd.DataFrame(data)
    
    with placeholder.container():
        st.line_chart(df)
        st.write("Anlık Veri Akışı:")
        st.dataframe(df.tail(5)) 
        
    time.sleep(2)