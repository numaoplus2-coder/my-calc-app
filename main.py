import streamlit as st

# 画面の設定
st.set_page_config(page_title="20分割計算機", layout="centered")

st.title("🔢 20分割計算機")

# スタイル調整（数字を大きく表示するため）
st.markdown("""
    <style>
    .big-font { font-size:50px !important; font-weight: bold; color: #007bff; }
    </style>
    """, unsafe_allow_html=True)

# 入力エリア
val = st.number_input("数値を入力してください", min_value=0, step=1, value=0)

# 計算ロジック
sho = val // 20
amari = val % 20

# 結果表示
st.write("---")
st.subheader("計算結果 (商 - 余り)")
st.markdown(f'<p class="big-font">{sho} - {amari}</p>', unsafe_allow_html=True)

# 使い方の説明
st.info("入力欄に数字を入れると、自動的に20で割った結果が表示されます。")
