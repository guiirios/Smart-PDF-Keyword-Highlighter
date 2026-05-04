import streamlit as st
import fitz
import os

#Variavel de arquivos, para guardar
arquivos = os.listdir("pdf/")

st.title("🔎 Buscador de palavras em PDFs")

inputWord = st.text_input("Digite a palavra buscada: ")

#botão = gatilho
if st.button("Buscar"):

    #o split vai quebrar cada palavra e transformar em uma lista
    palavras = inputWord.split(",")

    for arquivo in arquivos:
        if arquivo.endswith(".pdf"):

            #abre os pdf
            pdf = fitz.open("pdf/" + arquivo)

            #variavel para salvar cada palavra
            textPdf = ""

            #aqui ele vai entender que estou falando de pagina
            for pagina in pdf: 
                #para ele ficar adicionando cada palavra do pdf
                textPdf += pagina.get_text()

                #highlight
                for palavra in palavras:
                    areas = pagina.search_for(palavra)

                    for area in areas:
                        pagina.add_highlight_annot(area)

            encontradas = []

            for palavra in palavras:
                if palavra.lower() in textPdf.lower():
                    encontradas.append(palavra)

            if encontradas:
                st.write(arquivo, "->", encontradas)
            else:
                st.write("palavra -> nao achada")

            pdf.save("resultado_" + arquivo)
            pdf.close()
