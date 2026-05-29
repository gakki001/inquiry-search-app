import streamlit as st
import pandas as pd

# タイトル
st.title("問い合わせ検索ツール")

# CSV読み込み
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRVoHcBTlvlpZkRjYrjV0JQA7e0IYgGkoJVKI2eTv3PLrAtuGwQKTXg8Ht3zkM4WJK9tDFyyNQcC-2H/pub?gid=350386044&single=true&output=csv"
df = pd.read_csv(url)

# =========================
# 🔽 カテゴリーボタン
# =========================
st.write("### カテゴリーを選択")

categories = df["カテゴリー"].dropna().unique().tolist()

# 選択状態を保持
if "selected_category" not in st.session_state:
    st.session_state.selected_category = None

# ボタンを横並びにする
cols = st.columns(3)

for i, category in enumerate(categories):
    if cols[i % 3].button(category):
        st.session_state.selected_category = category

# =========================
# 🔽 カテゴリー選択後
# =========================
if st.session_state.selected_category:

    st.write(f"### 選択中：{st.session_state.selected_category}")

    filtered = df[df["カテゴリー"] == st.session_state.selected_category]

    options = filtered["問い合わせ内容"].dropna().tolist()

    selected_inquiry = st.selectbox("問い合わせを選択", options)

    row = filtered[filtered["問い合わせ内容"] == selected_inquiry].iloc[0]

    st.write("### 件名")
    st.write(row["件名"])

    st.write("### 返信文（編集できます）")
    edited_text = st.text_area(
        "返信文を編集",
        value=row["返信文"],
        height=200
    )

    st.code(edited_text)

# 区切り
st.write("---")

# =========================
# 🔽 キーワード検索
# =========================
st.write("### キーワード検索")

keyword = st.text_input("キーワードを入力してください")

if keyword:
    filtered_kw = df[df["問い合わせ内容"].str.contains(keyword, na=False)]

    if not filtered_kw.empty:
        options = filtered_kw["問い合わせ内容"].tolist()

        selected_kw = st.selectbox("検索結果から選択", options)

        row = filtered_kw[filtered_kw["問い合わせ内容"] == selected_kw].iloc[0]

        st.write("### 件名")
        st.write(row["件名"])

        edited_text = st.text_area(
            "返信文を編集（検索結果）",
            value=row["返信文"],
            height=200
        )

        st.code(edited_text)
    else:
        st.write("該当なし")
