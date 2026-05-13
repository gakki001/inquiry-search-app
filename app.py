import pandas as pd
import streamlit as st

# ▼スプレッドシートURL
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRVoHcBTlvlpZkRjYrjV0JQA7e0IYgGkoJVKI2eTv3PLrAtuGwQKTXg8Ht3zkM4WJK9tDFyyNQcC-2H/pub?gid=350386044&single=true&output=csv"

df = pd.read_csv(url)

st.title("問い合わせテンプレ検索")

keyword = st.text_input("キーワード入力")

if keyword:
    result = df[df.apply(
        lambda row: row.astype(str).str.contains(keyword, case=False, na=False).any(),
        axis=1
    )]

    if result.empty:
        st.write("該当なし")
    else:
        for i, row in result.head(5).iterrows():
            with st.expander(row["問い合わせ内容"]):
                st.write("件名")
                st.write(row["件名"])
                st.write("返信文")
                st.code(row["返信文"])