import streamlit as st
import random

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
    margin-top:120px;
}

/* 버튼 */
div.stButton > button{
    background-color:white;
    color:black;
    font-size:20px;
    border:none;
    border-radius:12px;
    padding:10px 25px;
}

/* 풍선 */
.balloon{
    position:fixed;
    bottom:-120px;
    font-size:42px;
    animation:floatUp linear forwards;
    z-index:999;
}

@keyframes floatUp{
    from{
        transform:translateY(0);
        opacity:1;
    }
    to{
        transform:translateY(-120vh);
        opacity:0;
    }
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

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([4,2,4])

    with col2:
        if st.button("나도 인사하기", use_container_width=True):
            st.session_state.page = "celebrate"
            st.rerun()

# ==========================
# 축하 화면
# ==========================
else:

    st.markdown(
        """
        <div class="success-text">
            🎆 첫 웹페이지 제작을 축하해요! 🎆
        </div>
        """,
        unsafe_allow_html=True
    )

    # 풍선 애니메이션
    balloons = ""

    for _ in range(40):
        left = random.randint(0, 100)
        duration = random.uniform(5, 10)
        delay = random.uniform(0, 4)

        balloons += f"""
        <div class="balloon"
             style="
                left:{left}%;
                animation-duration:{duration}s;
                animation-delay:{delay}s;">
            🎈
        </div>
        """

    st.markdown(balloons, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([4,2,4])

    with col2:
        if st.button("돌아가기", use_container_width=True):
            st.session_state.page = "main"
            st.rerun()
