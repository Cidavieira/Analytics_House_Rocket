import streamlit as st
import pandas as pd
import plotly as plt
import plotly.express as px
import datetime

from datetime import datetime,time

st.set_page_config(page_title='Insights',layout='wide')

#===========================================
# Funçoes
#===========================================

def set_feature(data):
    # add new features
    data['price_m2'] = data['price'] / data['sqft_lot']
    data['year'] = pd.DatetimeIndex(data['date']).year
    # change format
    #data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')
    return data


def hipotese1(data):
    st.title('Insights')
    st.subheader('H1: Imóveis que possuem vista para o mar, são 3 vezes mais caros, na média.')
    st.subheader('H1: Verdadeira')
    # data selection
    df1 = data[['price', 'waterfront']].groupby('waterfront').mean().reset_index()
    df1['waterfront'] = df1['waterfront'].apply(lambda x: 'Sem Vista' if x == int(0) else
    'Com Vista')
    # plot
    st.write(df1)
    fig = px.bar(df1, x='waterfront', y='price',title='Preço Médio por vista mar')
    st.plotly_chart(fig, use_container_width=True)

    return None

def hipotese2(data):
    st.subheader('H2: Imóveis com data de construção menor que 1955, são 50% mais baratos, na média.')
    st.subheader('H2: Falsa')
    df1 = data.loc[data['yr_built'] <= int(1955), ['price']].mean()[0]
    df2 = data.loc[data['yr_built'] > int(1955), ['price']].mean()[0]
    data_plot = {'Yr_Built': ['Maior_1955', 'Menor_1955'], 'Median_price': [df2, df1]}
    df = pd.DataFrame(data_plot)
    st.write (df)

    # plot
    fig = px.bar(df, x='Yr_Built', y='Median_price',title='Preço Médio por Ano Construção')
    st.plotly_chart(fig, use_container_width=True)
    return None


def hipotese3(data):
    st.subheader('H3: Imóveis sem porão possuem área total (sqrt lot) menores do que os imóveis com porão.')
    st.subheader('H3: Falsa')
    df1 = data.loc[data['sqft_basement'] == int(0), ['sqft_lot']].mean()[0]
    df2 = data.loc[data['sqft_basement'] > int(0), ['sqft_lot']].mean()[0]
    data_plot = {'Porao': ['Sem_porao', 'Com_porao'], 'Area_total_media': [df1, df2]}
    df = pd.DataFrame(data_plot)
    st.write(df)
    # plot
    fig = px.bar(df, x='Porao', y='Area_total_media',title='Área total imóveis com e sem porão')
    st.plotly_chart(fig, use_container_width=True)

    return None

def hipotese4(data):
    st.subheader('H4: O Crescimento de preço dos imóveis YoY (Year over Year) é de 10%.')
    st.subheader('H4: Falsa')
    df1 = data[['price', 'year']].groupby('year').mean().reset_index()

    # plot
    fig=px.line(df1,x='year',y='price')
    st.plotly_chart(fig, use_container_width=True)

    return None

def hipotese5(data):
    st.subheader('H5: Imóveis com 3 banheiros tem um crescimento de MoM (Month over Month) de 15%.')
    st.subheader('H5: Falsa')

    #df1 = data.loc[data['bathrooms'] == 3, :].copy()
    #df2 = df1.loc[data['year'] == int('2014'), 'price'].median()
    #df3 = df1.loc[data['year'] == int('2015'), 'price'].median()

    # plot
    #data_plot = {'Porao': ['Sem_porao', 'Com_porao'], 'Area_total_media': [df1, df2]}
    #fig=px.line(df5,x='floors',y='percentual')
    #st.plotly_chart(fig, use_container_width=True)


    return None

def hipotese6(data):
    st.subheader('H6: Imovéis com 3 ou mais andares são raros representam menos de 4% do dashbord. ')
    st.subheader('H6: Verdadeiro')
    df5 = data[['id', 'floors']].groupby('floors').count().reset_index()
    df5['percentual'] = df5['id'] / len(data)
    st.write(df5)


    return None

def hipotese7(data):
    st.subheader('H7: Imovéis sem banheiros são raros representam menos de 0.05% do dashbord.')
    st.subheader('H7: Verdadeira')
    df5 = data[['id', 'bathrooms']].groupby('bathrooms').count().reset_index()
    df5['percentual'] = df5['id'] / len(data)
    st.write(df5)

    return None

def hipotese8(data):
    st.subheader('H8: Imovéis com mais quartos são mais caros.')
    st.subheader('H8: Falso')
    df5 = data[['price', 'bedrooms']].groupby('bedrooms').mean().reset_index()
    st.write(df5)
    # plot
    fig=px.line(df5,x='bedrooms',y='price')
    st.plotly_chart(fig, use_container_width=True)

    return None

def hipotese9(data):
    st.subheader('H9: Metade dos Imoveis disponíveis são bons candidatos a dar lucro.')
    st.subheader('H9: Verdadeira')

   # status = relatorio1.loc[:, ['status', 'id']].groupby('status').count().reset_index()
   # plt.bar(status['status'], status['id'])
    # plot
    #fig = px.bar(status, x='status', y='id',title='Imóveis candidatos a dar lucro')
    #st.plotly_chart(fig, use_container_width=True)

    return None

def hipotese10(data):
    st.subheader('H:10 Imóveis com condição mediana = 3, representa 65% do dashboard.')
    st.subheader('H:10 Verdadeira')

    df5 = data[['id', 'condition']].groupby('condition').count().reset_index()
    df5['percentual'] = df5['id'] / len(data)
    st.write(df5)

    # plot
    fig = px.bar(df5, x='condition', y='id',title='Imóveis medianos')
    st.plotly_chart(fig, use_container_width=True)

    return None
#===========================================
#Import Dataset
#===========================================

df=pd.read_csv('dataset/kc_house_data.csv')

#===========================================
# Barra Lateral
#===========================================

st.sidebar.markdown('# House Rocket')
st.sidebar.markdown("""---""")
st.sidebar.markdown('### Powered by Aparecida Vieira')

# ===========================================
# Layout no streamlit
# ===========================================

#with st.container():
    #st.title("Overal Metrics")

    #col1, col2, col3, col4, col5, col6 = st.columns(6)
    #col1=st.columns(1)
    #with col1:
        #imoveis_unicos = df['id'].nunique()
        #ol1.metric('Imóveis', imoveis_unicos)
        #with col2:
            #avg_distance = distance(df1, fig=False)
            #col2.metric('A dist média entregas', avg_distance)

        #with col3:
            #festivais = avg_std_time_delivery(df1, 'Yes', 'avg_time')
            #col3.metric('Tempo médio c/ fest', festivais)
        #with col4:
            #festivais = avg_std_time_delivery(df1, 'Yes', 'std_time')
            #col4.metric('Std entrega c/ fest', festivais)
        #with col5:
            #festivais = avg_std_time_delivery(df1, 'No', 'avg_time')
            #col5.metric('Tempo médio s/ fest', festivais)
        #with col6:
            #festivais = avg_std_time_delivery(df1, 'No', 'std_time')
            #col6.metric('Std entrega s/ fest', festivais)

with st.container():
    #st.markdown("""---""")
    #st.title("Tempo Médio de entrega por cidade")
    data = set_feature(df)
    hipotese1(df)

with st.container():
    #st.markdown("""---""")
    #st.title("Tempo Médio de entrega por cidade")
    hipotese2(df)

with st.container():
    #st.markdown("""---""")
    #st.title("Tempo Médio de entrega por cidade")
    hipotese3(df)


with st.container():
    #st.markdown("""---""")
    #st.title("Tempo Médio de entrega por cidade")
    hipotese4(df)


with st.container():
    #st.markdown("""---""")
    #st.title("Tempo Médio de entrega por cidade")
    hipotese5(df)

with st.container():
    #st.markdown("""---""")
    #st.title("Tempo Médio de entrega por cidade")
    hipotese6(df)

with st.container():
    #st.markdown("""---""")
    #st.title("Tempo Médio de entrega por cidade")
    hipotese7(df)

with st.container():
    #st.markdown("""---""")
    #st.title("Tempo Médio de entrega por cidade")
    hipotese8(df)


with st.container():
    #st.markdown("""---""")
    #st.title("Tempo Médio de entrega por cidade")
    hipotese9(df)

with st.container():
    #st.markdown("""---""")
    #st.title("Tempo Médio de entrega por cidade")
    hipotese10(df)
