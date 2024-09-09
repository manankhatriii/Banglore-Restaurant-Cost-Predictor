import streamlit as st
import pandas as pd
import joblib

best_rf = joblib.load('grid_rf.pkl')

location_dict = {
    'Banashankari': 0,
    'Basavanagudi': 1,
    'Mysore Road': 2,
    'Jayanagar': 3,
    'Kumaraswamy Layout': 4,
    'Rajarajeshwari Nagar': 5,
    'Vijay Nagar': 6,
    'Uttarahalli': 7,
    'JP Nagar': 8,
    'South Bangalore': 9,
    'City Market': 10,
    'Nagarbhavi': 11,
    'Bannerghatta Road': 12,
    'BTM': 13,
    'Kanakapura Road': 14,
    'Bommanahalli': 15,
    'CV Raman Nagar': 16,
    'Electronic City': 17,
    'HSR': 18,
    'Marathahalli': 19,
    'Wilson Garden': 20,
    'Shanti Nagar': 21,
    'Koramangala 5th Block': 22,
    'Koramangala 8th Block': 23,
    'Richmond Road': 24,
    'Koramangala 7th Block': 25,
    'Jalahalli': 26,
    'Koramangala 4th Block': 27,
    'Bellandur': 28,
    'Sarjapur Road': 29,
    'Whitefield': 30,
    'East Bangalore': 31,
    'Old Airport Road': 32,
    'Indiranagar': 33,
    'Koramangala 1st Block': 34,
    'Frazer Town': 35,
    'RT Nagar': 36,
    'MG Road': 37,
    'Brigade Road': 38,
    'Lavelle Road': 39,
    'Church Street': 40,
    'Ulsoor': 41,
    'Residency Road': 42,
    'Shivajinagar': 43,
    'Infantry Road': 44,
    'St. Marks Road': 45,
    'Cunningham Road': 46,
    'Race Course Road': 47,
    'Commercial Street': 48,
    'Vasanth Nagar': 49,
    'HBR Layout': 50,
    'Domlur': 51,
    'Ejipura': 52,
    'Jeevan Bhima Nagar': 53,
    'Old Madras Road': 54,
    'Malleshwaram': 55,
    'Seshadripuram': 56,
    'Kammanahalli': 57,
    'Koramangala 6th Block': 58,
    'Majestic': 59,
    'Langford Town': 60,
    'Central Bangalore': 61,
    'Sanjay Nagar': 62,
    'Brookefield': 63,
    'ITPL Main Road, Whitefield': 64,
    'Varthur Main Road, Whitefield': 65,
    'KR Puram': 66,
    'Koramangala 2nd Block': 67,
    'Koramangala 3rd Block': 68,
    'Koramangala': 69,
    'Hosur Road': 70,
    'Rajajinagar': 71,
    'Banaswadi': 72,
    'North Bangalore': 73,
    'Nagawara': 74,
    'Hennur': 75,
    'Kalyan Nagar': 76,
    'New BEL Road': 77,
    'Jakkur': 78,
    'Rammurthy Nagar': 79,
    'Thippasandra': 80,
    'Kaggadasapura': 81,
    'Hebbal': 82,
    'Kengeri': 83,
    'Sankey Road': 84,
    'Sadashiv Nagar': 85,
    'Basaveshwara Nagar': 86,
    'Yeshwantpur': 87,
    'West Bangalore': 88,
    'Magadi Road': 89,
    'Yelahanka': 90,
    'Sahakara Nagar': 91,
    'Peenya': 92
}

type_dict = {
    'Buffet': 0,
    'Cafes': 1,
    'Delivery': 2,
    'Desserts': 3,
    'Dine-out': 4,
    'Drinks & nightlife': 5,
    'Pubs and bars': 6
}

st.title("Restaurant Approximate Cost Prediction")

online_order = st.selectbox('Online Order', ['Yes', 'No'])
book_table = st.selectbox('Book Table', ['Yes', 'No'])
votes = st.slider('Votes', 0, 10000, 500)
location = st.selectbox('Location', list(location_dict.keys()))
listed_in_type = st.selectbox('Listed in (Type)', list(type_dict.keys()))

online_order_encoded = 1 if online_order == 'Yes' else 0
book_table_encoded = 1 if book_table == 'Yes' else 0
location_encoded = location_dict[location]
listed_in_type_encoded = type_dict[listed_in_type]

input_data = pd.DataFrame({
    'online_order': [online_order_encoded],
    'book_table': [book_table_encoded],
    'votes': [votes],
    'location': [location_encoded],
    'listed_in(type)': [listed_in_type_encoded]
})

if st.button('Predict Approximate Cost'):
    predicted_cost = best_rf.predict(input_data)[0]
    st.success(f'The predicted approximate cost for two people is: ₹{predicted_cost:.2f}')

if __name__ == '__main__':
    st.set_option('deprecation.showPyplotGlobalUse', False)
