import streamlit as st

def two_parameter_interpolation(x1, x2, y1, y2, x):
    """
    Simple linear interpolation:
    y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    """
    return y1 + (y2 - y1) * (x - x1) / (x2 - x1)

def three_parameter_interpolation(x1, x2, y1, y2, z11, z12, z21, z22, x, y):
    """
    Bilinear interpolation:
    Step 1: interpolate along x at y1 and y2
    Step 2: interpolate along y between the two results
    """
    a = z11 + (z21 - z11) * (x - x1) / (x2 - x1)
    b = z12 + (z22 - z12) * (x - x1) / (x2 - x1)
    ans = a + (b - a) * (y - y1) / (y2 - y1)
    return ans

st.set_page_config(page_title="Interpolation Tool", page_icon="📊", layout="centered")

st.title("📊 Interpolation Tool")

st.markdown("""
This tool calculates interpolated values:
- **Case 1:** Linear interpolation with 2 parameters.
- **Case 2:** Bilinear interpolation with 3 parameters.
""")

case = st.radio("Select interpolation case:", ["Case 1: Two-parameter interpolation", "Case 2: Three-parameter interpolation"])

if case == "Case 1: Two-parameter interpolation":
    st.subheader("Input data for Case 1")
    col1, col2 = st.columns(2)
    with col1:
        x1 = st.number_input("Parameter 1: x1", value=1.0)
        y1 = st.number_input("Parameter 2: y1 corresponding to x1", value=10.0)
    with col2:
        x2 = st.number_input("Parameter 1: x2", value=2.0)
        y2 = st.number_input("Parameter 2: y2 corresponding to x2", value=20.0)
    
    x = st.number_input("Value to interpolate at (x)", value=1.2)

    if st.button("Calculate"):
        answer = two_parameter_interpolation(x1, x2, y1, y2, x)
        st.success(f"✅ Interpolated value at x={x}: **{answer}**")

elif case == "Case 2: Three-parameter interpolation":
    st.subheader("Input data for Case 2")
    col1, col2 = st.columns(2)
    with col1:
        x1 = st.number_input("Parameter 1: x1", value=1.0)
        x2 = st.number_input("Parameter 1: x2", value=2.0)
    with col2:
        y1 = st.number_input("Parameter 2: y1", value=1.0)
        y2 = st.number_input("Parameter 2: y2", value=2.0)

    st.markdown("### Enter Para3 values for each (para1, para2) pair")
    colz1, colz2 = st.columns(2)
    with colz1:
        z11 = st.number_input("Para3 at (x1, y1)", value=1.0)
        z12 = st.number_input("Para3 at (x1, y2)", value=2.0)
    with colz2:
        z21 = st.number_input("Para3 at (x2, y1)", value=3.0)
        z22 = st.number_input("Para3 at (x2, y2)", value=4.0)

    x = st.number_input("Value to interpolate at (x)", value=1.3)
    y = st.number_input("Value to interpolate at (y)", value=1.8)

    if st.button("Calculate"):
        answer = three_parameter_interpolation(x1, x2, y1, y2, z11, z12, z21, z22, x, y)
        st.success(f"✅ Interpolated value at (x={x}, y={y}): **{answer}**")
