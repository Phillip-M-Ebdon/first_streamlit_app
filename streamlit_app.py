import streamlit
import pandas 
import requests
import snowflake.connector

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

# smoothie ingredient table
fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

# API response area
streamlit.header('Fruityvice Fruit Advice!')

# get user input
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)

# make web request
fruityvice_response = requests.get('https://fruityvice.com/api/fruit/' + fruit_choice)
fruit_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruit_normalized)


# snowflake connector
my_cnx = snowflake.connector.connect(**streamlit.secrets['snowflake'])
my_cur = my_cnx.cursor()
my_cur.execute('SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()')
my_data_row = my_cur.fetchone()
streamlit.text('Hello from snowflake:')
streamlit.text(my_data_row)
