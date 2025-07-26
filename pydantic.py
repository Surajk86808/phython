# type validation for Python data classes using Pydantic
from pydantic import BaseModel, EmailStr,AnyUrl,Field
from typing import List, Dict,Optional,Annotated

# Define the Patient model(class) with validation
class Patient(BaseModel):
    name: Annotated[str ,Field(max_length=50,title ='Name Of the patient' ,description="Name must be less than 50 characters",examples = ['Nitish','Ansh'] )]  # Name must be less than 50 characters
    # Annotated is used to add metadata to the field above is the synatx to use annonated
    age: int = Field(gt=0,lt = 120, description="Age must be between 1 and 120")  # Age must be between 1 and 120
    weight : float = Field(gt=0, description="Weight must be greater than 0")  # Weight must be greater than 0
    height : float = Field(gt=0, description="Height must be greater than 0")
    married: bool = False  # Default value is False
    linked_in: Annotated[AnyUrl,Field(strict= True)]  # LinkedIn URL must be a valid URL
    email: EmailStr 
    gender: str = Field(default='Not Specified', description="Please specify")  
    allergies : Optional[List[str]] = None  #optional field and defaulr none
    contact_numbers : Dict[str,str]
 
# Function to insert patient data
def insert_patient_data(patient: Patient):
    print("Patient Name:", patient.name)
    print("Patient Age:", patient.age)
    print("Patient Email:", patient.email)
    print("Data inserted successfully")

# Patient data as dictionary
patient_info = {
    'name': 'John',
    'age': 30,
    'email': 'john@example.com',  
    'allergies': ['peanuts', 'shellfish'],
    'contact_numbers': {
        'home': '123-456-7890',
        'work': '098-765-4321'
    }
}

# Create Patient instance(object) using unpacking (**)
patient_1 = Patient(**patient_info)

# Call the function with the patient instance
insert_patient_data(patient_1)
