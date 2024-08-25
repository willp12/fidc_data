import pandas as pd
import streamlit as st

df_final = pd.read_csv('data/output/inf_mensal_fidc_tab_VII_consolidado.csv')

st.write("My first Streamlit app!")

selected_company = st.selectbox("Selecione um Fundo", list(df_final.DENOM_SOCIAL.unique())[::-1])

if selected_company:
    df_selected_company = df_final[df_final['DENOM_SOCIAL'] == selected_company]
    st.bar_chart(df_selected_company[['DT_COMPTC', 'DENOM_SOCIAL', 'TAB_VII_A1_2_VL_DIRCRED_RISCO']],
             x='DT_COMPTC',
             y='TAB_VII_A1_2_VL_DIRCRED_RISCO')

st.data_editor(df_final)
