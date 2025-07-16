import streamlit as st

st.set_page_config(page_title="Interpolation Tool", layout="centered")
st.title("🔢 Interpolation Tool")

st.markdown("""
## 📌 Case 1: Linear interpolation
""")

with st.form("case1_form"):
    st.markdown("#### Enter values:")
    # Top row
    col1, col2 = st.columns(2)
    with col1:
        x1 = st.number_input("x1", value=1.0, key="x1_case1")
    with col2:
        y1 = st.number_input("y1", value=10.0, key="y1_case1")

    # Middle row
    col3, col4 = st.columns(2)
    with col3:
        x = st.number_input("x", value=1.2, key="x_case1")
    with col4:
        st.markdown("**ans** (will be calculated)")

    # Bottom row
    col5, col6 = st.columns(2)
    with col5:
        x2 = st.number_input("x2", value=2.0, key="x2_case1")
    with col6:
        y2 = st.number_input("y2", value=20.0, key="y2_case1")

    submit_case1 = st.form_submit_button("✅ Calculate Case 1")

if submit_case1:
    if x2 - x1 != 0:
        ans1 = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
        st.success(f"Answer: {ans1:.4f}")
    else:
        st.error("x2 and x1 cannot be the same (division by zero).")

st.markdown("---")
st.markdown("""
## 📌 Case 2: Bilinear interpolation
""")

with st.form("case2_form"):
    st.markdown("#### Enter values:")

    # First header row
    colh0, colh1, colh2, colh3 = st.columns(4)
    with colh0:
        st.markdown(" ")
    with colh1:
        y1_2 = st.number_input("y1", value=1.0, key="y1_case2")
    with colh2:
        y = st.number_input("y", value=1.8, key="y_case2")
    with colh3:
        y2_2 = st.number_input("y2", value=2.0, key="y2_case2")

    # Row for x1
    colx1, colz11, coldash1, colz12 = st.columns(4)
    with colx1:
        x1_2 = st.number_input("x1", value=1.0, key="x1_case2")
    with colz11:
        z11 = st.number_input("z11", value=1.0)
    with coldash1:
        st.markdown("--")
    with colz12:
        z12 = st.number_input("z12", value=2.0)

    # Row for x
    colx, coldash2, colans, coldash3 = st.columns(4)
    with colx:
        x = st.number_input("x", value=1.3, key="x_mid_case2")
    with coldash2:
        st.markdown("--")
    with colans:
        st.markdown("**ans** (will be calculated)")
    with coldash3:
        st.markdown("--")

    # Row for x2
    colx2, colz21, coldash4, colz22 = st.columns(4)
    with colx2:
        x2_2 = st.number_input("x2", value=2.0, key="x2_case2")
    with colz21:
        z21 = st.number_input("z21", value=3.0)
    with coldash4:
        st.markdown("--")
    with colz22:
        z22 = st.number_input("z22", value=4.0)

    submit_case2 = st.form_submit_button("✅ Calculate Case 2")

if submit_case2:
    if (x2_2 - x1_2 != 0) and (y2_2 - y1_2 != 0):
        # Interpolate in x at y1
        a = z11 + (z21 - z11) * (x - x1_2) / (x2_2 - x1_2)
        # Interpolate in x at y2
        b = z12 + (z22 - z12) * (x - x1_2) / (x2_2 - x1_2)
        # Interpolate in y
        ans2 = a + (b - a) * (y - y1_2) / (y2_2 - y1_2)
        st.success(f"Answer: {ans2:.4f}")
    else:
        st.error("x2≠x1 and y2≠y1 are required (division by zero).")

