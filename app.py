import streamlit as st

st.title("📊 財富等級計算器：台灣 vs 美國")
st.markdown("輸入以下資訊，看看你目前的生活水準在哪個等級！")

# 基本輸入
region = st.selectbox("你目前在哪個國家？", ["台灣", "美國"])
annual_income = st.number_input("你的年收入（稅前）", min_value=0)
rent_or_mortgage = st.number_input("每月房租或房貸", min_value=0)
monthly_expenses = st.number_input("每月其他生活支出（交通、食物、水電...）", min_value=0)

# 可支配所得計算
disposable_income = annual_income / 12 - rent_or_mortgage - monthly_expenses

# 判斷等級函數
def determine_level(region, income, disposable):
    if region == "台灣":
        if income >= 2000000 or disposable >= 100000:
            return "💎 富裕"
        elif income >= 1000000 or disposable >= 40000:
            return "💰 小康"
        elif income >= 600000 or disposable >= 10000:
            return "💼 中等"
        else:
            return "🥲 貧窮"
    elif region == "美國":
        if income >= 150000 or disposable >= 5000:
            return "💎 Wealthy"
        elif income >= 90000 or disposable >= 2500:
            return "💰 Comfortable"
        elif income >= 50000 or disposable >= 800:
            return "💼 Moderate"
        else:
            return "🥲 Struggling"

level = determine_level(region, annual_income, disposable_income)

# 顯示結果
st.markdown(f"### 👉 你的財富等級是：**{level}**")
st.markdown(f"每月可支配所得：約 **{int(disposable_income):,} {'TWD' if region == '台灣' else 'USD'}**")

# 說明
with st.expander("📌 財富等級定義說明"):
    st.markdown("""
    #### 台灣標準：
    - 💎 富裕：年收200萬以上或月可支配10萬以上
    - 💰 小康：年收100～200萬或月可支配4～10萬
    - 💼 中等：年收60～100萬或月可支配1～4萬
    - 🥲 貧窮：年收60萬以下或月可支配少於1萬

    #### 美國標準：
    - 💎 Wealthy：年收15萬以上或月可支配5,000美元以上
    - 💰 Comfortable：年收9～15萬或月可支配2,500～5,000美元
    - 💼 Moderate：年收5～9萬或月可支配800～2,500美元
    - 🥲 Struggling：年收5萬以下或月可支配800美元以下
    """)
