from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SequentialChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Temperature 설정
openai = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPENAI_API_KEY, temperature=0.7)


# Temperature 설정
# openai = ChatOpenAI(model="gpt-4o",api_key=os.getenv("OPENAI_API_KEY"), temperature=0.7)

# 프롬프트 템플릿 설정
prompt1 = PromptTemplate.from_template(
   "다음 식당 리뷰를 한 문장으로 요약하세요.\n\n{review}"
)
chain1 = LLMChain(llm=openai, prompt=prompt1, output_key="summary")

prompt2 = PromptTemplate.from_template(
   "다음 식당 리뷰를 읽고 0점부터 10점 사이에서 부정/긍정 점수를 매기세요. 숫자만 대답하세요.\n\n{review}"
)
chain2 = LLMChain(llm=openai, prompt=prompt2, output_key="sentiment_score")


prompt3 = PromptTemplate.from_template(
   "다음 식당 리뷰 요약에 대해 공손한 답변을 작성하세요.\n리뷰 요약:{summary}"
)
chain3 = LLMChain(llm=openai, prompt=prompt3, output_key="reply")