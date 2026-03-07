import streamlit as st

st.title("Welcome to Price Calculator")
price=st.number_input('Enter product price',1,100000,100,10)
discount_percentage=st.slider('Enter discount percentage',0,50,25,1)
if st.button("Calculate"):
    net = price -(price * (discount_percentage/100))
    st.success(f"Discounted price, ${net}!") 
    data = [
        ["Original Price", price],
        ["Discount (%)", f"{discount_percentage}%"],
        ["Final Price", net]
    ]
    st.table(data)