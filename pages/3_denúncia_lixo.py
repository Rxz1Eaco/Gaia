import streamlit as st
import pandas as pd

st.title("Denúncia")
form = st.form(key='cliente', clear_on_submit=True)
Apelidos = ["Repórter do Bairro","Rádio Ambulante","Informante Sorridente","Detetive de Fofocas","Fonte Inesgotável","Correspondente da Vizinhança","Espiã do Quarteirão","Investigador Social","Mensageira dos Segredos"]

Bairro_slz = [" ", "Bequimão", "Angelim", "Cohama", "Vicente Fialho", "São Cristovão", "Radional", "Turu", "Cohab" ]
Turno = ["Manhã","Tarde", "Noite","Madrugada"]


with form:
    nome = st.text_input("Nome:", placeholder="Seu nome irá ser modificado para sua segurança")
    apelido = st.selectbox("Apelido:",Apelidos)
    dia = st.text_input("Dia:", placeholder="Dia/Mês/Ano")
    horario = st.text_input("Horário:", placeholder="Hora:minuto:segundo")
    turno = st.selectbox("Selecione o turno:", Turno)
    bairro = st.selectbox("Selecione o bairro do acontecido:", Bairro_slz)
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "txt", "xlsx"])

    if uploaded_file is not None:
        st.write("Informações sobre a imagem:")
        st.write(f"Nome imagem: {uploaded_file.name}")
        st.write(f"Tipo imagem: {uploaded_file.type}")
        st.write(f"Tamanho imagem: {uploaded_file.size} bytes")

        data = None
        try:
            data = pd.read_csv(uploaded_file)
        except Exception as e:
            st.error(f"Erro ao processar o arquivo: {e}")

        if data is not None:
            st.write("Dados do imagem:")
            st.write(data)

btn_envio = form.form_submit_button("Confirmar")
