import streamlit as st
import webbrowser
from streamlit_image_comparison import image_comparison

st.set_page_config(page_title="Página Descarte")

st.sidebar.markdown("[Desenvolvido por Rxz1Eaco](https://github.com/Rxz1Eaco)")
st.write("## Importância do Descarte Correto 🌎")

image_comparison(
img1="https://www.blogsoestado.com/danielmatos/files/2015/12/lixo-slz.jpg",
img2="https://www.viagensecaminhos.com/wp-content/uploads/2016/11/vista-aerea-centro-historico-sao-luis.jpg")

btn = st.button("Dê uma olhada em nosso site")
if btn:
    webbrowser.open_new_tab(
        "https://www.saoluis.ma.gov.br/semmam"
    )
#st.image(
   # "https://www.blogsoestado.com/danielmatos/files/2015/12/lixo-slz.jpg",
   # caption="Imagem Pókemon",
  #  width=300,
  #  use_column_width=True,
#)



st.markdown(
    
    "De acordo com o Comitê de Limpeza Pública de São Luís, o descarte irregular de lixo teve aumento de 30% com relação ao lixo recolhido no ano passado.\n Durante o ano de 2016, cerca de 230 toneladas de lixo irregular eram recolhidas diariamente na capital maranhense. \nMas nesses primeiros meses de 2017 a quantidade de lixo descartada irregularmente chegou a 300 toneladas diárias.\n Isso representa 1/4 dos resíduos coletados diariamente em São Luís."
    "É extremamente preocupante o aumento no descarte irregular de resíduos sólidos, pois esses materiais descartados em locais indevidos, como canteiros e terrenos baldios, podem causar uma série de problemas, desde risco à saúde humana a prejuízos ao meio ambiente."
    "Uma das consequências dessa atitude irresponsável é a contribuição para a proliferação, entre outros, do mosquito Aedes aegypti, transmissor da dengue, chikungunya e zika vírus.\n O acúmulo de lixo nesses locais permitem que outros animais, que também oferecem riscos à saúde do homem, consigam se reproduzir com maior facilidade. Entre esses animais estão ratos, baratas, escorpiões e moscas. \nOutro problema é entupimento de bueiros que leva ao alagamento das vias e a maior probabilidade de contaminação por doenças como a leptospirose."
    "A Prefeitura de São Luís informou que intensificou o serviço de coleta de lixo na capital e que além dos caminhões que já fazem o recolhimento dos resíduos, há também a remoção manual e mecanizada dos resíduos, nos casos necessários. A população pode contar também com os Ecopontos, destinados à entrega voluntaria de resíduos sólidos em grande volume, como restos de poda, entulho da construção civil, madeiras e móveis velhos."  )