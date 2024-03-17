from dotenv import load_dotenv
load_dotenv()
import os
from langchain.prompts import PromptTemplate
from PyPDF2 import PdfReader
import google.generativeai as genai
import streamlit as st

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(diff,topic,material):
    prompt = f"""You are an expert teaching AI model with advanced knowledge of all programming languages.
    Your task is to generate 10 open-ended questions of {diff} difficulty on the topic:{topic}.
    The answer to these questions must be present in the following: {material}. If the topic is not available in the provided material return "information not available"\n\n
    
    <MESSAGE>:|"rate your responses on a scale on 1-10 based on your knowledge. if score is less than 4 generate
    a new response. do not display the rating." """
    # template = PromptTemplate(template=prompt,input_variables=['diff','topic','material'])
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(prompt)
    return response.text


st.set_page_config(page_title="StudyMate")
st.header("PRODUCT DESCRIPTION----->",divider='orange')
st.markdown('''
Introducing **StudyMate** - Your Personalized Learning Companion

Are you tired of monotonous study routines? Do you wish to engage in more meaningful and thought-provoking learning experiences? Look no further! **StudyMate** is here to revolutionize your study sessions.

**StudyMate** is a cutting-edge Web application designed to enhance your learning journey by generating tailor-made open-ended questions based on your study material, difficulty level, and topics of interest. Whether you're a student preparing for exams or a lifelong learner seeking intellectual stimulation, **StudyMate** caters to your unique needs.

Key Features:

1. Seamless PDF Integration: Simply upload your study material in PDF format, and **StudyMate** will extract the relevant content to create insightful questions.

2. Customizable Difficulty Levels: Choose from a range of difficulty levels, including easy, medium, and challenging, to suit your learning pace and preferences.

3. Topic Selection: Select your preferred topics from a diverse range of subjects, ensuring that the generated questions align with your interests and curriculum requirements.

4. Dynamic Question Generation: Utilizing advanced algorithms and natural language processing techniques, **StudyMate** generates open-ended questions that promote critical thinking, comprehension, and deeper understanding of the subject matter.

5. Personalized Learning Experience: Receive a curated list of questions tailored specifically to your input, allowing you to focus on areas of strength or areas requiring further exploration.

6. Interactive Study Sessions: Engage in stimulating study sessions by pondering over thought-provoking questions that encourage analytical reasoning and conceptual mastery.

7. Progress Tracking: Monitor your progress and performance over time, allowing you to identify areas of improvement and track your academic growth.

How It Works:

1. Upload your study material in PDF format.
2. Select the desired difficulty level and topics of interest.
3. Sit back and let **StudyMate** analyze your input to generate customized open-ended questions.
4. Dive into a transformative learning experience as you explore and reflect upon the generated questions.
5. Review your progress and continue your learning journey with newfound insights and knowledge.
6. Experience the power of personalized learning with **StudyMate**. Embark on a quest for knowledge like never before!







            ''')



st.subheader("",divider='orange')


col1,col2,col3=st.columns(3)
with col1:
    st.subheader("select difficulty")
    diff=st.selectbox(" ",options=['Easy','Medium','Hard'])

with col2:
    st.subheader("Enter Topic")
    topic=st.text_input("Enter topic of interest:")

# with col3:
st.subheader("upload study material(*PDF only*):")
material=st.file_uploader('upload file:',type="pdf")


text=""
if material is not None:
    reader=PdfReader(material)
    for page in reader.pages:
        text+=page.extract_text()
if st.button("generate"):
    response=get_gemini_response(diff,topic,text)
    print(response)
    st.write(response)


st.text("")
st.text("")
st.text("")
st.text("")
st.text("NOTE:- If the page gives an error while generation. Kindly reload.")