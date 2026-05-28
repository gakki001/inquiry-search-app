import streamlit as st
import pandas as pd

# タイトル
st.title("問い合わせ検索ツール")

# CSV読み込み（あなたのURLに変更）
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRVoHcBTlvlpZkRjYrjV0JQA7e0IYgGkoJVKI2eTv3PLrAtuGwQKTXg8Ht3zkM4WJK9tDFyyNQcC-2H/pub?gid=350386044&single=true&output=csv"
df = pd.read_csv(url)

# =========================
# 🔽 一覧から選択（追加機能）
# =========================
st.write("### 一覧から選択")

all_options = df["問い合わせ内容"].dropna().tolist()
selected_list = st.selectbox("問い合わせ一覧", ["選択してください"] + all_options)

if selected_list != "選択してください":
    row = df[df["問い合わせ内容"] == selected_list].iloc[0]

    st.write("### 件名")
    st.write(row["件名"])

    st.write("### 返信文（編集できます）")
    edited_text = st.text_area("返信文を編集", value=row["返信文"], height=200)
    st.code(edited_text)

st.write("---")

# =========================
# 🔽 キーワード検索
# =========================
st.write("### キーワード検索")

keyword = st.text_input("キーワードを入力してください")

if keyword:
    filtered = df[df["問い合わせ内容"].str.contains(keyword, na=False)]

    if not filtered.empty:
        options = filtered["問い合わせ内容"].tolist()
        selected = st.selectbox("検索結果から選択", options)

        row = filtered[filtered["問い合わせ内容"] == selected].iloc[0]

        st.write("### 件名")
        st.write(row["件名"])

        st.write("### 返信文（編集できます）")
        edited_text = st.text_area("返信文を編集（検索結果）", value=row["返信文"], height=200)
        st.code(edited_text)

    else:
        st.write("該当なし")
