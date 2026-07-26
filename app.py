import streamlit as st
import pickle

model = pickle.load(open('Car_Price_Prediction.pkl','rb'))

st.title("🚗 Car Price Prediction")
st.write("Enter Car Details Below")
engine_size = st.number_input("Enter Engine size in Litres")
horse_power = st.number_input("Enter Horsepower",min_value=100,max_value=3000)
mileage = st.number_input("Enter Mileage kmpl")
# Brand Input
brand = st.selectbox("Select Brand",['Honda', 'Hyundai', 'Kia', 'MG',
       'Mahindra', 'Maruti', 'Skoda', 'Tata',
       'Toyota', 'Volkswagen'])
brand_dict = {
    'Honda': (1,0,0,0,0,0,0,0,0,0),
    'Hyundai': (0,1,0,0,0,0,0,0,0,0),
    'Kia': (0,0,1,0,0,0,0,0,0,0),
    'MG': (0,0,0,1,0,0,0,0,0,0),
    'Mahindra': (0,0,0,0,1,0,0,0,0,0),
    'Maruti': (0,0,0,0,0,1,0,0,0,0),
    'Skoda': (0,0,0,0,0,0,1,0,0,0),
    'Tata': (0,0,0,0,0,0,0,1,0,0),
    'Toyota': (0,0,0,0,0,0,0,0,1,0),
    'Volkswagen': (0,0,0,0,0,0,0,0,0,1),
}
Honda , Hyundai,Kia,MG,Mahindra,Maruti,Skoda,Tata,Toyota,Volkswagen = brand_dict[brand]

# Model Input
car_model = st.selectbox("Select Car Model",['Altroz', 'Amaze',
       'Astor', 'Baleno', 'Brezza', 'Carens',
       'City', 'Comet', 'Creta', 'Elevate',
       'Glanza', 'Hector', 'Hyryder', 'Innova',
       'Kushaq', 'Nexon', 'Polo', 'Punch',
       'Scorpio', 'Seltos', 'Slavia', 'Sonet',
       'Superb', 'Swift', 'Taigun', 'Venue',
       'Virtus', 'XUV300', 'XUV700', 'i20'])
car_model_dict={
    'Altroz':(1, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'Amaze':(0, 1, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'Astor':(0, 0, 1, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'Baleno':(0, 0, 0, 1, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'Brezza':(0, 0, 0, 0, 1, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'Carens':(0, 0, 0, 0, 0, 1, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'City':(0, 0, 0, 0, 0, 0, 1, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'Comet':(0, 0, 0, 0, 0, 0, 0, 1, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'Creta':(0, 0, 0, 0, 0, 0, 0, 0, 1, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'Elevate':(0, 0, 0, 0, 0, 0, 0, 0, 0, 1,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'Glanza':(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,1, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'Hector':(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 1, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'Hyryder':(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 1, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'Innova':(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 1, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'Kushaq':(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 1, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'Nexon':(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 1, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'Polo':(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 1, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'Punch':(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 1, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'Scorpio':(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 1, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'Seltos':(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 1,0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'Slavia':(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'Sonet':(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    'Superb':(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
    'Swift':(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
    'Taigun':(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
    'Venue':(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
    'Virtus':(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
    'XUV300':(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
    'XUV700':(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
    'i20':(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
}
Altroz,Amaze,Astor,Baleno,Brezza,Carens,City,Comet,Creta,Elevate,Glanza,Hector,Hyryder,Innova,Kushaq,Nexon,Polo,Punch,Scorpio,Seltos,Slavia,Sonet,Superb,Swift,Taigun,Venue,Virtus,XUV300,XUV700,i20 = car_model_dict[car_model]

# Fuel Type
fuel_type = st.selectbox("Select Car Fuel Type",[ 'CNG', 'Diesel', 'Electric','Petrol'])
fuel_type_dict = {
    'CNG':(1,0,0,0),
    'Diesel':(0,1,0,0),
    'Electric':(0,0,1,0),
    'Petrol':(0,0,0,1),
}
CNG,Diesel,Electric,Petrol = fuel_type_dict[fuel_type]

# Transmission
transmission = st.selectbox("Select Transmission",['Automatic', 'Manual'])
transmission_dict = {
    'Automatic':(1,0),
    'Manual':(0,1),
}
Automatic,Manual = transmission_dict[transmission]

data = [[engine_size,horse_power,mileage,Honda , Hyundai,Kia,MG,Mahindra,Maruti,Skoda,Tata,Toyota,Volkswagen,
         Altroz,Amaze,Astor,Baleno,Brezza,Carens,City,Comet,Creta,Elevate,Glanza,Hector,Hyryder,Innova,Kushaq,Nexon,Polo,Punch,Scorpio,
         Seltos,Slavia,Sonet,Superb,Swift,Taigun,Venue,Virtus,XUV300,XUV700,i20,
         CNG,Diesel,Electric,Petrol,
         Automatic,Manual]]
st.markdown("""
    <style>
    div.stButton > button:first-child{
        background-color: red;
        color: white;
        border-radius: 8px;
        font-size: 18px;
    }
 </style>
""",unsafe_allow_html=True)

if st.button("Predict"):
    pred = model.predict(data)
    st.info(f"Predicted Car Price: ₹{pred[0]:,.2f}")

st.divider()
st.markdown("""
<div style="
background-color:green;
padding:10px;
border-radius:8px;
font-size:12px;
color:black;
">


This application predicts Car Price using a **Multiple Linear Regression** model trained on a **randomly generated sample dataset**.

⚠️ The predictions are for **educational and demonstration purposes only**.

**👨‍💻 Developed by:** **TheDevCodex**
""", unsafe_allow_html=True)