import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, Text input, Slider, Sub header
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
forecast = st.slider("Forecast Days: ", min_value=1, max_value=5, help="Select the number of forecasted days")
data_to_view = st.selectbox(label="Select Data to view", options=["Temperature", "Sky"])


if place:
    try:
        # get the temperature/ sky data
        filtered_data = get_data(place, forecast)

        if data_to_view == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temperature Plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperatures(C)"})
            st.subheader(f"{data_to_view} for the next {forecast} day(s) in {place.title()}")
            st.plotly_chart(figure)

        if data_to_view == "Sky":
            st.subheader(f" Sky for the next {forecast} day(s) in {place.title()}")
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_path = [images[condition] for condition in sky_conditions]
            st.image(image_path, width=115)

    except KeyError:
        st.markdown(f"<h1 style='color: red;'>{place.title()} doesn't exist!</h1>", unsafe_allow_html=True)
