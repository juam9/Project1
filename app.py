import streamlit as st

st.set_page_config(
    page_title="첫 웹앱",
    layout="wide"
)

# 페이지 상태
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
    font-size:60px;
    font-weight:bold;
    text-align:center;
    margin-top:180px;
}

/* 축하 문구 */
.success-text{
    color:white;
    font-size:45px;
    font-weight:bold;
    text-align:center;
    margin-top:150px;
}

/* 버튼 */
div.stButton > button{
    width:100%;
    background-color:white;
    color:black;
    font-size:22px;
    font-weight:bold;
    border:none;
    border-radius:12px;
    padding:12px;
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

    # 버튼 가운데 정렬
    left, center, right = st.columns([2, 1, 2])

    with center:
        if st.button("나도 인사하기", use_container_width=True):
            st.session_state.page = "celebrate"
            st.rerun()

# ==========================
# 축하 화면
# ==========================
else:

    # 풍선 효과
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

    # 버튼 가운데 정렬
    left, center, right = st.columns([2, 1, 2])

    with center:
        if st.button("돌아가기", use_container_width=True):
            st.session_state.page = "main"
            st.rerun()
