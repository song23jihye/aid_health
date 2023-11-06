# # from langchain.llms import OpenAI 
# # llm=OpenAI() #이어 작성
# # result = llm.predict('내가 좋아하는 음식은')
# # print(result)

from langchain.chat_models import ChatOpenAI

from langchain.llms import OpenAI
import streamlit as st
# import time

llm = OpenAI(openai_api_key="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")

st.title('클리블랜드 심장질환 진단')

chat_model = ChatOpenAI()
content = st.text_input("진단사항에 대해 말씀해주세요.")
result = chat_model.predict(content+"의 종류 한가지만 말해줘.")
st.write(result)
