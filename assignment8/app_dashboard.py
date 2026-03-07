import streamlit as st

st.title("Simple Sales Dashboard")

months = ["January", "February", "March", "April"]
selected_month = st.selectbox("Select a month to view sales:", months)


sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

current_sales = sales[selected_month]
st.metric(label=f"Sales for {selected_month}", value=current_sales)

st.subheader("Sales Overview")
st.bar_chart(list(sales.values()))