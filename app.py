import streamlit as st
import pandas as pd

# タイトル
st.title("問い合わせ検索ツール")

# CSV読み込み（あなたのURLに変更）
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRVoHcBTlvlpZkRjYrjV0JQA7e0IYgGkoJVKI2eTv3PLrAtuGwQKTXg8Ht3zkM4WJK9tDFyyNQcC-2H/pub?gid=350386044&single=true&output=csv"
df = pd.read_csv(url)

# =========================
# 🔽 カテゴリー選択
# =========================
st.write("### カテゴリーから選択")

# カテゴリー一覧（重複削除＋並び替え）
categories = sorted(df["カテゴリー"].dropna().unique().tolist())

selected_category = st.selectbox(
    "カテゴリーを選択",
    ["選択してください"] + categories
)

# =========================
# 🔽 カテゴリー選択後
# =========================
if selected_category != "選択してください":

    # 選んだカテゴリーで絞る
    filtered = df[df["カテゴリー"] == selected_category]

    # 問い合わせ一覧
    options = filtered["問い合わせ内容"].dropna().tolist()

    selected_inquiry = st.selectbox(
        "問い合わせを選択",
        options
    )

    # 選択されたデータ取得
    row = filtered[filtered["問い合わせ内容"] == selected_inquiry].iloc[0]

    # 表示
    st.write("### 件名")
    st.write(row["件名"])

    st.write("### 返信文（編集できます）")
    edited_text = st.text_area(
        "返信文を編集",
        value=row["返信文"],
        height=200
    )

    # コピーしやすい表示
    st.code(edited_text)

# 区切り
st.write("---")

# =========================
# 🔽 キーワード検索（そのまま残す）
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
