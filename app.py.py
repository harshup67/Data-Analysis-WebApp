import pandas as pd
import streamlit as st
import seaborn as sns

#title and subheader
st.title("Data analysis")
st.subheader("Data Analysis using pandas & Streamlit")

#upload dataset
upload = st.file_uploader("Upload your dataset(In CSV format)")
if upload is not None:
    data = pd.read_csv(upload)

#show dataset
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())

#check datatype of each column
if upload is not None:
    if st.checkbox("Datatypes of each Column"):
        st.write(data.dtypes)
#find shape of our dataset(number of rows and number of columns)
if upload is not None:
    data_shape = st.radio("What dimension do you want to check?",('Rows','Columns'))
    if data_shape=='Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape=='Columns':
        st.text("Number of Columns")
        st.write(data.shape[1])

#check dataset is null or not
if upload is not None:
    test = data.isnull().values.any()
    if test==True:
        if st.checkbox("Null values in the dataset"):
            sns.heatmap(data.isnull())
            st.pyplot
    else:
        st.success("Congratulations! No missing value found")
if upload is not None:
    test = data.duplicated().any()
    if test==True:
        st.warning("This dataset contains duplicate values")
        dup = st.selectbox("Do you want to remove duplicate values?",("Select one","Yes","No"))
        if dup=="Yes":
            data = data.drop_duplicates()
            st.text("Duplicate values are removed")
        if dup=="No":
            st.text("OK! No problem")

#Get overall statistics
if upload is not None:
    if st.checkbox("Summary of the dataset"):
        st.write(data.describe(include='all'))

#About section
if st.button("About App"):
    st.text("Built with Streamlit")
    st.text("Thanks to Streamlit")

if st.checkbox("By"):
    st.success("Harsh Vardhan")



