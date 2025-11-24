import streamlit as st
from datetime import date, timedelta
from streamlit_dateinput_intl import streamlit_dateinput_intl


st.write("Streamlit DatePicker Example")

selected_date = streamlit_dateinput_intl(
   value="today",
   min=date.today() - timedelta(days=30),
   max=date.today() + timedelta(days=30),
   key="date_input_full",
   format="YYYY/MM/DD",
   disabled=False,
   width="stretch",
   locale="ja"
)

st.write("selected date: ", selected_date)
