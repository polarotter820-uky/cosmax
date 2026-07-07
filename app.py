import pathlib
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="오토차트 스튜디오",
    page_icon="📊",
    layout="wide",
)

# 이미지 등 모든 리소스가 base64로 내장된 단일 HTML 파일을 그대로 불러와 렌더링합니다.
HTML_PATH = pathlib.Path(__file__).parent / "autochart_studio.html"
html_code = HTML_PATH.read_text(encoding="utf-8")

# 화면이 길어질 수 있으므로 넉넉한 높이 + 스크롤 허용
components.html(html_code, height=1600, scrolling=True)
