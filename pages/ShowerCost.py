import streamlit as st

st.title("Seattle Cold vs Hot Shower")
st.subheader("This is a simple app to compare the cost of a cold shower vs a hot shower in Seattle, WA.")

st.write("I've been reading about the benefits of cold showers in terms of health such as awakefulness, but I began to wonder if I was also saving any money from eletrical costs.")



#User number input

st.subheader("Enter the number of people in your household:")
num_people = st.number_input("", step=1, key = "num_people")
st.subheader("Enter the average length of shower in minutes:")
shower_length = st.number_input("", step=1, key= "shower_length")

#Calculate the cost of a hot shower
#2.47 watts per gallon per degree
#1 kWh = 1000 watts
#Delta Temperature * kwh cost per gallon * gallons/minute * minutes

hot_shower_cost_per_person_per_day = (105-60)* (0.12*2.47/1000) * 3 * shower_length

hot_shower_cost_per_year = hot_shower_cost_per_person_per_day * 365 * num_people

#Display Results

st.write("The cost of a hot shower per person per day is: $", round(hot_shower_cost_per_person_per_day,2))
st.write("The cost of a hot showers per year is: $", round(hot_shower_cost_per_year,2))

#Write Empty Lines

st.write('\n')

st.write("Assumptions")

st.write("1. The average shower temperature is 105 degrees F")
st.write("2. The average shower flow rate is 3 gallons per minute")
st.write("3. The average input water temperature is 60 degrees F")
st.write("4. Seattle's electricity rate is 0.12 cents per kWh")
st.write("5. Water left in pipes is considered neglibile")

st.write("Calculation: Calcuation 2.47 watts per gallon per degree \
1 kWh = 1000 watts \
\n \
Delta Temperature * kwh cost per gallon * gallons/minute * minutes \
hot_shower_cost_per_person_per_day = (105-60)* (0.12*2.47/1000) * 3 * shower_length")