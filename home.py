import streamlit as st
import geopandas
from PIL import Image

st.set_page_config(
    page_title="home",
    layout='wide'
)

#image_path=
image = Image.open('image.jpg')
st.sidebar.image(image,width=120)


st.sidebar.markdown('# House Rocket Company')
st.sidebar.markdown('## Buy & Sell houses ')
st.sidebar.markdown("""---""")
st.write(" ### House Rocket - Dashboard / Insights / Recommendation")

st.markdown(
    """
    House Rocket foi construído pra acompanhar a distribuição de imóveis, verificar Insights deste data base e Recomendar quais imóveis devem ser compradas e vendidas juntamente com os preços sugeridos.
    ### Como utilizar esse Growth Dasboard?
    - Dashbord:
        - Principais Métricas Gerais de distribuição de imóveis.
    - Insights:
        - Verificar os principais 10 Insights tirados do data base completo.
    - Recomendation:
        - Saber quais casas foram indicadas para comprar e estimar um preço de venda para obtenção de lucro.
        - Imóveis em período quente mêses (Novembro,Outubro,Setembro,Agosto,Julho,Junho,Maio) vão obter lucro de 30%.
        - Imóveis em período frio Mêses (Dezembro,Abril,Março,Fevereiro,Janeiro) vão obter lucro de 10%.
    ### Ask for Help
    - Time de Data Science no Discord
        - @Cida.vieira#8158
    """
)
