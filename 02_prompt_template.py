from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

# 평가를 위한 프롬프트 템플릿을 정의합니다. 사용자의 리뷰를 기반으로 점수 범위를 정하템플릿을 작성합니다.
prompt_template = "이 음식 리뷰 '{review}'에 대해 '{rating1}'점부터 '{rating2}'점까지의 평가를 해주세요."
prompt = PromptTemplate(
    input_variables=["review", "rating1", "rating2"], template=prompt_template
)

# temperature 속성을 설정하여, 낮은 값은 보다 일관된 결과를, 높은 값은 다양한 결과를 생성하도록 합니다.
openai = ChatOpenAI(model="gpt-3.5-turbo",
                    api_key=os.getenv("OPENAI_API_KEY"), 
                    temperature=0.7)