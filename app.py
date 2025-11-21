import streamlit as st

from datetime import datetime

import locale

st.title("DateInput Streamlit!")

try:
    locale.setlocale(locale.LC_ALL, "ja_JP.UTF-8")
    st.write("Successfully set locale to ja_JP.UTF-8")
except locale.Error:
    st.write("Failed to set locale")

st.write(f"st.context.locale: {st.context.locale}")

selected_date = st.date_input("Select a date", value=datetime.now().date())
# Format date using locale-aware formatting
date_datetime = datetime.combine(selected_date, datetime.min.time())
# Use locale's date format, or fallback to Japanese format
try:
    date_format = locale.nl_langinfo(locale.D_FMT)
    japanese_date = date_datetime.strftime(date_format)
    st.write(f"date_format: {date_format}")
    st.write(f"japanese_date: {japanese_date}")
except (AttributeError, locale.Error):
    st.error("Failed to get locale date format")
