import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set Page Config
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="wide")

# Sidebar Navigation
st.sidebar.title("⚙️ Options")
page = st.sidebar.radio("Go to", ["Home", "Progress Graphs" ,"About", "Contact"])

# Home Page - Unit Converter
if page == "Home":
    st.title("🔄 Advanced Unit Converter")

    # Unit Type Selection
    unit_type = st.selectbox("Select Unit Type", ["Length", "Weight", "Temperature", "Speed", "Time", "Volume"])

    # Definitions and Formulas
    definitions = {
        "Length": "Length measures the distance between two points.",
        "Weight": "Weight is the force exerted by gravity on an object.",
        "Temperature": "Temperature measures the degree of heat present in an object.",
        "Speed": "Speed is the distance covered per unit of time.",
        "Time": "Time is the ongoing sequence of events taking place.",
        "Volume": "Volume measures the amount of space occupied by a substance.",
    }

    formulas = {
        "Length": "Formula: 1 km = 1000 m, 1 cm = 0.01 m",
        "Weight": "Formula: 1 kg = 1000 g, 1 pound = 0.453592 kg",
        "Temperature": "Formula: °C to °F: (°C × 9/5) + 32",
        "Speed": "Formula: 1 m/s = 3.6 km/h, 1 mph = 1.609 km/h",
        "Time": "Formula: 1 hour = 60 min, 1 day = 24 hours",
        "Volume": "Formula: 1 liter = 1000 mL, 1 gallon = 3.78541 L"
    }

    # Show Definition & Formula
    st.info(f"**{definitions[unit_type]}**")
    st.warning(f"📌 {formulas[unit_type]}")

    # Conversion Logic
    unit_data = {
        "Length": {"Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Millimeter": 0.001},
        "Weight": {"Kilogram": 1, "Gram": 0.001, "Pound": 0.453592, "Ounce": 0.0283495},
        "Speed": {"Meter/sec": 1, "Kilometer/hour": 0.277778, "Miles/hour": 0.44704, "Knots": 0.514444},
        "Time": {"Seconds": 1, "Minutes": 60, "Hours": 3600, "Days": 86400, "Weeks": 604800},
        "Volume": {"Liters": 1, "Milliliters": 0.001, "Gallons": 3.78541, "Cubic meters": 1000}
    }

    if unit_type == "Temperature":
        def convert_temperature(value, from_unit, to_unit):
            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                return (value - 32) * 5/9
            elif from_unit == "Celsius" and to_unit == "Kelvin":
                return value + 273.15
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                return value - 273.15
            return value

        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
        value = st.number_input("Enter Value", format="%.2f")

        if st.button("Convert"):
            result = convert_temperature(value, from_unit, to_unit)
            st.success(f"Converted Value: {result:.2f} {to_unit}")

    else:
        from_unit = st.selectbox("From", list(unit_data[unit_type].keys()))
        to_unit = st.selectbox("To", list(unit_data[unit_type].keys()))
        value = st.number_input("Enter Value", format="%.2f")

        if st.button("Convert"):
            result = value * (unit_data[unit_type][to_unit] / unit_data[unit_type][from_unit])
            st.success(f"Converted Value: {result:.4f} {to_unit}")

            # Download Button
            output_data = f"Converted {value} {from_unit} to {result:.4f} {to_unit}"
            st.download_button("📥 Download Result", output_data, file_name="conversion_result.txt")

# Progress Graphs Page
elif page == "Progress Graphs":
    st.title("📊 Your Progress Over Time")
    st.write("Track your learning journey with visual graphs.")

    st.markdown("### Enter Your Weekly Progress")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    default_progress = [20, 40, 60, 80, 100, 90, 50]

    progress_data = {}
    for i, day in enumerate(days):
        progress_data[day] = st.slider(f"{day} Progress (%)", 0, 100, default_progress[i])

    df = pd.DataFrame({"Day": list(progress_data.keys()), "Progress": list(progress_data.values())})
    fig, ax = plt.subplots()
    ax.plot(df["Day"], df["Progress"], marker="o", linestyle="-", color="#1DB954")
    ax.set_title("Your Weekly Progress")
    ax.set_xlabel("Days")
    ax.set_ylabel("Progress (%)")
    ax.grid(True)
    st.pyplot(fig)
    st.markdown("### 📋 Your Weekly Data")
    st.write(df)
    st.download_button("📥 Download CSV", df.to_csv(index=False), "progress_data.csv", "text/csv")

elif page == "About":
    st.title("📌 About User Converter")
    st.write("""
    **Advanced Unit Converter** is a versatile tool designed to quickly and accurately convert between multiple units of measurement. 
    Whether you need to convert **length, weight, temperature, speed, time, or volume**, this converter provides an intuitive and efficient solution.

    ✅ **User-Friendly Interface**
             
              – Simple and easy-to-use design for quick conversions.
             
    ✅ **Accurate Conversions**
             
              – Reliable formulas ensure precision in every calculation.
             
    ✅ **Multiple Unit Support** 
             
             – Convert between various metric and imperial units.

    ✅ **Downloadable Results**
             
              – Save your converted values for future reference.
             

    This tool is perfect for students, engineers, scientists, and anyone who needs **fast and accurate** unit conversions! 🚀
    """)

elif page == "Contact":
    st.title("📞 Contact Us")
    st.write("Have questions or feedback? Fill out the form below, and we'll get back to you!")

# User Inputs
username = st.text_input("Username", placeholder="Enter your username")
name = st.text_input("Full Name", placeholder="Enter your full name")
email = st.text_input("Email", placeholder="Enter your email address")
message = st.text_area("Message", placeholder="Type your message here...")

# Submit Button
if st.button("Submit"):
    if username and name and email and message:
        st.success("✅ Thank you! Your message has been sent successfully.")
    else:
        st.error("⚠️ Please fill in all the fields before submitting.")
