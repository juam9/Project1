import streamlit as st

st.set_page_config(
    page_title="첫 웹앱",
    layout="wide"
)

# 페이지 상태 저장
if "page" not in st.session_state:
    st.session_state.page = "main"

# CSS
st.markdown("""
<style>
.stApp{
    background-color:#0b1f4d;
}

/* 메인 문구 */
.big-text{
    color:white;
    font-size:55px;
    font-weight:bold;
    text-align:center;
    margin-top:180px;
}

/* 축하 문구 */
.success-text{
    color:white;
    font-size:42px;
    font-weight:bold;
    text-align:center;
    margin-top:140px;
}

/* 버튼 */
div.stButton > button{
    background-color:white;
    color:black;
    font-size:20px;
    font-weight:bold;
    border:none;
    border-radius:12px;
    padding:10px 25px;
}

div.stButton{
    display:flex;
    justify-content:center;
}
</style>
""", unsafe_allow_html=True)

# ==========================
# 메인 화면
# ==========================
if st.session_state.page == "main":

    st.markdown(
        """
        <div class="big-text">
            👋 안녕하세요 👋
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    if st.button("나도 인사하기"):
        st.session_state.page = "celebrate"
        st.rerun()

# ==========================
# 축하 화면
# ==========================
else:

    # 풍선 애니메이션
    st.balloons()

    st.markdown(
        """
        <div class="success-text">
            🎆 첫 웹페이지 제작을 축하해요! 🎆
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")
    st.write("")

    if st.button("돌아가기"):
        st.session_state.page = "main"
        st.rerun()
