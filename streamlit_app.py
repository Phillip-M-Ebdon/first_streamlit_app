import streamlit
import pandas 
import requests
import snowflake.connector
from urllib.error import URLError

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



try:
  
  # get user input
  fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
  streamlit.write('The user entered', fruit_choice)
  if not fruit_choice:
    streamlit.error("Please select a fruit")
  else:
    # make web request
    fruityvice_response = requests.get('https://fruityvice.com/api/fruit/' + fruit_choice)
    fruit_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruit_normalized)
except URLError as e:
  strealit.error()


# snowflake connector
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur = my_cnx.cursor()
    my_cur.execute('select * from fruit_load_list')
    return my_cur.fetchall()
  
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets['snowflake'])
  streamlit.header('The fruit load list contains')
  streamlit.dataframe(get_fruit_load_list())
  my_cnx.close()

my_new_fruit = streamlit.text_input('What fruit would you like to add?')
def insert_row(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')")
    return 'Thanks for adding ' + new_fruit
    
if streamlit.button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets['snowflake'])
  back_from_func = insert_row(my_new_fruit)
  my_cnx.close()

