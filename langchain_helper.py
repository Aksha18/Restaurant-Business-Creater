from dotenv import load_dotenv
import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_openai import ChatOpenAI
load_dotenv()



llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7)

def generate_restaurant_plan(cuisine, location, scale):
    
    prompt_name = PromptTemplate(
        input_variables=["cuisine", "location", "scale"],
        template="Suggest a unique restaurant name and tagline for a {scale} focused on {cuisine} cuisine in {location}"
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_name, output_key="Restaurent")

    
    prompt_items = PromptTemplate(
        input_variables=['Restaurent', 'scale'],
        template="""suggest some menu items for the {Restaurent} provide items in the categories of starters ,main_course, desserts and Beverages based on {scale} and {Restaurent}
        Output format:
        Starters:
        - item 1
        - item 2
        - item 3
        Main Course:
        - item 1
        - item 2
        - item 3
        Desserts:
        - item 1
        - item 2
        Beverages:
        - item 1
        - item 2

        Do not add any explanations"""
    )
    items_chain = LLMChain(llm=llm, prompt=prompt_items, output_key="Menu_Items")

    
    prompt_places = PromptTemplate(
        input_variables=["scale", "location", "cuisine"],
        template="""You are a restaurant business consultant. 
        Given a {cuisine} cuisine type and a {location} (city or state), 
        suggest the best possible locations within {location} to start a {scale} restaurant. 
        Base your answer on popularity trends, customer footfall, and cultural acceptance of {cuisine} cuisine.

        Format output as:
        1. Area/Neighborhood Name - Reason for selection
        2. Area/Neighborhood Name - Reason for selection"""
    )
    places_chain = LLMChain(llm=llm, prompt=prompt_places, output_key="restaurant_location_suggestions")

    # Chain 4: Staffing
    prompt_staff = PromptTemplate(
        input_variables=["cuisine", "scale"],
        template="""Given a {cuisine} restaurant of {scale} size, suggest the ideal staffing plan with designations and recommended number of employees for each role.  
        Consider kitchen, service, management, and support staff separately.  

        Format output as:  
        Kitchen Staff:  
        - Role 1: Number of employees  
        Service Staff:  
        - Role 1: Number of employees  
        Management:  
        - Role 1: Number of employees  
        Support Staff:  
        - Role 1: Number of employees"""
    )
    staff_chain = LLMChain(llm=llm, prompt=prompt_staff, output_key="staff_plan")

    chain = SequentialChain(
        chains=[name_chain, items_chain, places_chain, staff_chain],
        input_variables=["cuisine", "location", "scale"],
        output_variables=["Restaurent", "Menu_Items", "restaurant_location_suggestions", "staff_plan"]
    )

   
    return chain({'cuisine': cuisine, 'location': location, 'scale': scale})