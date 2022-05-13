import streamlit
import pandas 

# data stuff
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

# streamlit stuff
streamlit.title('My Parenets New Healthy Diet')
## breakfast
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

## smoothies
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index), ['Avocado', 'Strawberries'])

# smoothie ingredient table
streamlit.dataframe(my_fruit_list)
