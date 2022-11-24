import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title("Streamlit 超入門")

st.write("プログレスバーの表示")
"Start!!"

# df = pd.DataFrame(
#     np.random.randn(100, 2) / [50, 50] + [35.69, 139.70],
#     columns=["lat", "lon"]
# )

# st.dataframe(df.style.highlight_max(axis="rows"), width=150, height=300)
# st.table(df.style.highlight_max(axis="rows"))

# st.line_chart(df)

# st.map(df)

# if st.checkbox("Show Image"): 
#     img = Image.open("sample_fig.png")
#     st.image(img, caption="sample", use_column_width=True)

# option = st.selectbox(
#     "あなたが好きな数字を教えてください、",
#     list(range(1, 11))
# )
# "あなたの好きな数字は、", option, "です。"



# text = st.text_input("あなたの趣味を教えて下さい。")
# condition = st.slider("あなたの今の調子は？", 0, 100, 50)

# "あなたの趣味：", text
# "コンディション：", condition

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    print(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)
 

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander = st.expander("問い合わせ1")
expander.write("問い合わせ1の回答")
expander2 = st.expander("問い合わせ2")
expander2.write("問い合わせ2の回答")
expander3 = st.expander("問い合わせ3")
expander3.write("問い合わせ3の回答")
