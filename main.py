from openai import OpenAI
import time
import streamlit as st

# 코드스니펫 - 제목
st.title('나만의 제품 홍보 생성기')

# 코드스니펫 - 입력
keyword = st.text_input("키워드를 입력하세요.")

if st.button('생성하기'):
  st.write('나만의 제품 홍보 포스터 완성~')
  with st.spinner('Wait for it...'):

    client = OpenAI(api_key=st.secrets["API_KEY"])

    chat_completion = client.chat.completions.create(
        messages=[{
            "role":
            "user",
            "content":
            keyword +
            '라는 주제로 새로운 제품을 홍보할 수 있는 카피를 150자 이내로, 기억에 잘 남도록 유명한 광고 문구를 참고해서 작성해줘.',
        }],
        model="gpt-4o",
    )

    chat_result = chat_completion.choices[0].message.content

    st.write(chat_result)

    client = OpenAI(api_key=st.secrets["API_KEY"])

    response = client.images.generate(
        model="dall-e-3",
        prompt=keyword,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    # 코드스니펫 - 이미지
    st.image(image_url)
