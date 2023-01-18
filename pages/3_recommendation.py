import streamlit as st
import pandas as pd
st.set_page_config(page_title='Dashbord', layout='wide' )



data = pd.read_csv( 'dataset/kc_house_data.csv')
df=data[['zipcode','price']].groupby('zipcode').median().reset_index()
df['price_median']=df['price']
df=df.loc[:,['zipcode','price_median']]
df1=pd.merge(data,df,on='zipcode',how='inner')

for i in range(len(df1)):
    if (df1.loc[i,'price']< df1.loc[i,'price_median']) & (df1.loc[i,'condition']>=3):
        df1.loc[i,'status']='compra'
    else:
        df1.loc[i,'status']='nao compra'


relatorio1=df1.loc[:,['id','zipcode','condition','price','price_median','status']]

st.title('Recommendation Compra')

st.subheader('Price abaixo da Média Região')
st.subheader('O que Comprar? (status & id)')
st.subheader( 'E a qual preço comprar? (price)')
st.write(relatorio1)


df2=df1.loc[df1['status']=='compra',:].copy()
df2['month']= pd.DatetimeIndex(df2['date']).month
df2['periodo']= df2['month'].apply(lambda x: 'frio' if x==int(12) else
                                                 'quente' if x==int(11) else
                                                 'quente' if x>=int(5) else 'frio' )
df3=df2[['zipcode','periodo','price']].groupby(['zipcode','periodo']).median().reset_index()
df3['price_median']=df3['price']
df3=df3.drop(['price','periodo','price_median'],axis=1)
df4=pd.merge(df3,df2,on='zipcode',how='inner')
df4=df4.loc[df1['status']=='compra',:].copy()
df4['% venda']= df4['periodo'].apply(lambda x: (0.3 ) if x=='quente' else
                                                   0.1 )

df4['price_venda']=df4['price']*df4['% venda']+df4['price']

df4['lucro']=df4['price_venda']-df4['price']


st.title('Recommendation Venda')
st.subheader( 'Vender a qual preço? (price_venda)')
st.subheader('Em qual período (periodo)')
relatorio2=df4.loc[:,['id','zipcode','condition','price','price_median','price_venda','lucro','periodo','% venda']]
st.write(relatorio2)

st.title('Lucro Total')
st.subheader('Aproximadamente 936 Milhões')
st.subheader(df4['lucro'].sum())
st.write(df4['lucro'].sum())


