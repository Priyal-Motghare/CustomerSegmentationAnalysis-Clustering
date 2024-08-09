# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 15:06:16 2024

@author: Hiren
"""

import streamlit as st
import pandas as pd
from pickle import load

def create_page():
    st.title('Customer Cluster Prediction')
    Education = st.sidebar.radio('Education',[0, 1, 2, 3, 4])
    st.sidebar.write('0 : Basic, 1 : Secondary, 2 : Graduation, 3 : Master, 4 : PhD')
    Marital_Status = st.sidebar.radio('Marital Status', [0, 1, 2])
    st.sidebar.write('0 : Single, 1 : Together, 2 : Was Married')
    Income = st.slider('Income', min_value=7500, max_value=110000, step = 1)
    MntWines = st.slider('Wines', min_value=0, max_value=1300, step=1)
    MntFruits = st.slider('Fruits', min_value=0, max_value=145, step=1)
    MntMeatProducts = st.slider('Meat Products', min_value=0, max_value=800, step=1)
    MntFishProducts = st.slider('Fish Products', min_value=0, max_value=190, step=1)
    MntSweetProducts = st.slider('Sweet Products', min_value=0, max_value=130, step=1)
    MntGoldProds = st.slider('Gold Products', min_value=0, max_value=180,step=1)
    NumDealsPurchases = st.slider('Number of Deal Purchases', min_value=0, max_value=10, step=1)
    NumWebPurchases = st.slider('Number of Web Purchases', min_value=0, max_value=15, step=1)
    NumCatalogPurchases = st.slider('Number of Catalog Purchases', min_value=0, max_value=10, step=1)
    NumStorePurchases = st.slider('Number of Store Purchases', min_value=0, max_value=15, step=1)
    NumWebVisitsMonth = st.slider('Number of Web Visits per Month', min_value=0, max_value=10, step=1)
    num_kids = st.sidebar.radio('Children', [0,1,2,3])
    total_cmp_accepted = st.radio('Total Campaigns Accepted', [0,1,2,3,4,5])
    
    total_amt_spent = MntWines + MntFruits + MntFishProducts + MntGoldProds + MntSweetProducts + MntMeatProducts
    total_purchases = NumWebPurchases + NumCatalogPurchases + NumStorePurchases + NumDealsPurchases

    data1 = {'Education': Education,'Marital_Status': Marital_Status, 'Income': Income,
        'MntWines': MntWines, 'MntFruits': MntFruits, 'MntMeatProducts': MntMeatProducts, 'MntFishProducts': MntFishProducts,
        'MntSweetProducts': MntSweetProducts, 'MntGoldProds': MntGoldProds, 'NumDealsPurchases': NumDealsPurchases,
        'NumWebPurchases': NumWebPurchases, 'NumCatalogPurchases': NumCatalogPurchases,
        'NumStorePurchases': NumStorePurchases, 'NumWebVisitsMonth': NumWebVisitsMonth,
        'num_kids': num_kids, 'total_cmp_accepted': total_cmp_accepted, 'total_amt_spent': total_amt_spent, 'total_purchases': total_purchases}

    df = pd.DataFrame(data1, index=[0])
    return df
features = create_page()

if st.button('Predict Now'):
    st.write(features)
    loaded = load(open(r'C:/Users/Hiren/Desktop/Data Science/Project/final2.pkl', 'rb'))
    cluster_label = loaded.predict(features)

    st.write(f'Belongs to cluster {cluster_label[0]}')