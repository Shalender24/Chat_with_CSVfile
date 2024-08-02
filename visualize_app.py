import streamlit as st
import pandas as pd
import plotly.express as px

def run_visualize_app():
    rad = st.sidebar.radio("Navigation", ["Visualize"])
    if rad == "Visualize":
        file_upload = st.sidebar.file_uploader(" ", type=["csv"])
        # st.sidebar.image("image_loan.png", use_column_width=True) 
        chart_select = st.sidebar.selectbox(
            label="Select the chart type",
            options=['ScatterPlots', 'Lineplots', 'Histogram', 'Boxplot']
        )
        html_temp = """
        <div style="background-color:red;padding:10px">
        <h2 style="color:white;text-align:center;">Automatic Machine Learning </h2>
        </div>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
        st.sidebar.title("Upload Input csv file : ")
        st.subheader('1.Datasets')
        st.write("""
        # Automated Machine Learning
        """)

        if file_upload is not None:
            df = pd.read_csv(file_upload)
            st.write(df)
            numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
            if chart_select == "ScatterPlots":
                st.sidebar.subheader("ScatterPlot Settings")
                x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
                y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
                plot = px.scatter(data_frame=df, x=x_values, y=y_values)
                st.plotly_chart(plot)
            elif chart_select == "Lineplots":
                st.sidebar.subheader("LinePlot Settings")
                x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
                y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
                plot = px.line(data_frame=df, x=x_values, y=y_values)
                st.plotly_chart(plot)
            elif chart_select == "Histogram":
                st.sidebar.subheader("Histogram Settings")
                x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
                y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
                plot = px.histogram(data_frame=df, x=x_values, y=y_values)
                st.plotly_chart(plot)
            elif chart_select == "Boxplot":
                st.sidebar.subheader("BoxPlot Settings")
                x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
                y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
                plot = px.box(data_frame=df, x=x_values, y=y_values)
                st.plotly_chart(plot)
        else:
            st.info('Awaiting for CSV file to be uploaded.')
