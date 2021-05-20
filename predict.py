import streamlit as st
import pickle
import numpy as np
import pandas as pd

def load_model():
    with open('saved_steps.pkl','rb') as file:
        data = pickle.load(file)
    return(data)

data = load_model()

rf = data['model']
sc = data['num_scale']
enc = data['cat_enc']

def show_predict_page():
    st.title('Stock Prediction')

    st.write("Input 5 Yr. Hist. EPS Growth,	5 Yr Historical Sales Growth,\
            	ROA (5 Yr Avg),	ROI (5 Yr Avg) to predict whether a company \
                    will beat the S&P. This app was trained on traditional growth \
                        companies that give no dividend."
                     )


    sectors = ('Retail-Wholesale', 'Aerospace', 'Medical', 'Industrial Products',
       'Computer and Technology', 'Consumer Staples', 'Auto-Tires-Trucks',
       'Basic Materials', 'Construction', 'Transportation', 'Oils-Energy',
       'Consumer Discretionary', 'Business Services', 'Utilities',
       'Conglomerates')

    eps = st.text_input('5 Yr. Hist EPS Growth',0)
    sales = st.text_input('5 Yr. Hist Sales Growth',0)
    roa = st.text_input('ROA',0)
    roi = st.text_input('ROI',0)

    sector = st.selectbox('Sector',sectors)

    buy = st.button("Should I invest?")
    if buy:
        X = np.array([[float(eps),float(sales),float(roa),float(roi),sector]])
        X[:,:4] = sc.transform(X[:,:4])
        cat = enc.transform(np.array(X[:,4]).reshape(1,-1)).toarray()
        res = np.concatenate([X[:,:4],cat],axis=1)
        

        invest = rf.predict(res)
        if invest==1:
            st.subheader(f"Yes")
        else:
            st.subheader(f"No")