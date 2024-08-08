# Box Plot
# Shows the distribution of quantitative data across several levels of a categorical variable.

#Bar Plot
#A bar plot shows the relationship between a categorical variable and a continuous variable.

# Count Plot
# Similar to a bar plot but specifically for showing the count of observations in each category.




import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def show_cat(df):
    if df is not None and not df.empty:
        feature_columns = df.columns.tolist()
        object_type = df.select_dtypes(include=['object']).columns.tolist()
        numeric_type = df.select_dtypes(include=['int64', 'int32', 'float32','float64']).columns.tolist()

        plot_relational = ['Bar Plot', 'Count Plot', 'Box Plot']   #Line plot is mostly used for time-series data
        plot = st.selectbox("Type of relational plot" , options = plot_relational, index= None) 
            
        if plot == 'Bar Plot':
            with st.container():
                col1, col2= st.columns(2)
                st.info("Bar Plot shows the relationship between a categorical variable and a continuous variable.")
                with col1:
                    x_axis = st.selectbox("Select the Categorical Variable", object_type ,index = None)
                with col2:
                    y_axis = st.selectbox("Select the Numeric Variable", numeric_type, index = None) 

            if st.button("Generate Plot"):
                fig = sns.catplot(x=x_axis, y=y_axis, data=df, kind='bar')
                st.pyplot(fig)

        elif plot == 'Count Plot':
            st.info("Similar to a bar plot but specifically for showing the count of observations in each category.")
            with st.container():
                col1, col2= st.columns(2)

                with col1:
                    cat_col = st.selectbox("Select the categorical variable", numeric_type ,index = None)
                with col2:
                    Hue = st.selectbox("Hue Parameter", feature_columns, index = None) 
            if st.button("Generate Plot"):
                fig = sns.catplot(x=Hue, y=cat_col ,data=df, kind='count')
                st.pyplot(fig)

        elif plot == 'Box Plot':
            st.info("Shows the distribution of quantitative data across several levels of a categorical variable.")
            with st.container():
                col1, col2= st.columns(2)

                with col1:
                    cat_col = st.selectbox("Select the categorical variable", numeric_type ,index = None)
                with col2:
                    Hue = st.selectbox("Hue Parameter", feature_columns, index = None) 
            if st.button("Generate Plot"):
                fig = sns.catplot(x=Hue, y=cat_col, data=df, kind='box')
                st.pyplot(fig)