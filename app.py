import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="ShareMate AI",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 ShareMate AI")
st.write("AI 영수증 인식 기반 쉐어하우스 공동생활 관리 서비스")

st.divider()

st.subheader("1. 영수증 이미지 업로드")

uploaded_file = st.file_uploader(
    "영수증 이미지를 업로드하세요",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="업로드한 영수증",
        use_container_width=True
    )

    st.success("이미지 업로드 성공")
else:
    st.info("JPG, JPEG, PNG 형식의 영수증 이미지를 선택해주세요.")