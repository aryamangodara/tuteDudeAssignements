import streamlit as st

st.title("Welcome to App Product form")
name = st.sidebar.text_input('Enter product name')
category=st.sidebar.selectbox('Choose Cateogry',options=['Electronics','Civil','IT','Mechanical','misc'])
price=st.sidebar.number_input('Enter Price',1)
if st.button('Add Product'):
    st.success('Product added successfully')
    st.write(f'Prodcut Name: {name} \n Product Category: {category} \n Product Price: ${price:.2f}')
