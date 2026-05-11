import streamlit as st
import fitz
import os

#Variavel de arquivos, para guardar
#lista tudo que tem na pasta pdf
arquivos = os.walk("pdf/")


st.title("🔎 Buscador de palavras em PDFs")

inputWord = st.text_input("Digite a palavra buscada: ")

#botão = gatilho
if st.button("Buscar"):

    #o split vai quebrar cada palavra e transformar em uma lista
    palavras = inputWord.split(",")
    achou_alguma = False
    
    for raiz, pastas, arquivos in os.walk("pdf/"):
        for arquivo in arquivos:
            caminho = raiz + "/" + arquivo
            if arquivo.endswith(".pdf"):

                #abre os pdf
                pdf = fitz.open(caminho)

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
                    achou_alguma = True

                    pdf.save("pdf_marcado/resultado_" + arquivo)
                pdf.close() 
               
    if not achou_alguma:
        st.write("Nenhuma palavra encontrada!")
            
    
    
