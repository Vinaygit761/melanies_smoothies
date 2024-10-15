# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
st.title(":cup_with_straw: Customize Your Smoothie!:cup_with_straw:")
st.write(
    """Choose the fruits you want in your custom smooothie!
    """
)
#import streamlit as st
name_on_order = st.text_input("Name on smoothie:")
st.write("The name on your smoothie will be:", name_on_order)
cnx = st.connection("snowflake")
session = cnx.session()
#my_dataframe = session.table("smoothies.public.orders").filter(col("ORDER_FILLED")==0).collect()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)
ingredients_list = st.multiselect(
    'choose up to 5 ingredients:'
   , my_dataframe,
    max_selections=5
)
if ingredients_list:
    ingredients_string = ''
         for fruit_chosen in ingredients_list:
         ingredients_string += fruit_chosen + ''
 #st.write(ingredients_list)
       my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """','"""+name_on_order +"""')"""
     st.write(my_insert_stmt)
     st.stop()
    #st.write(my_insert_stmt)   
time_to_insert = st.button("Submit Order")
if time_to_insert:
 session.sql(my_insert_stmt).collect() 
st.success('Your Smoothie is ordered!', icon="✅")





