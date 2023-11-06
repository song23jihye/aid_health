from langchain.chat_models import ChatOpenAI
import streamlit as st
import time

chat_model=ChatOpenAI() #질문<->답변

st.title('클리블랜드 심장질환 진단')

content = st.text_input("진단사항에 대해 말씀해주세요.")

st.button("Reset", type="primary")
if st.button('시 작성 요청하기'):
    with st.spinner('Wait for it...'):
        result = chat_model.predict(content+"에 대한 시를 써줘")
        st.write('result')
