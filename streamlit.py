from streamlit as st
import requests
# Configurar la URL del servidor Flask

str.title('Ingrese su texto para clasificar')
flask_url = 'http://localhost:8008/procesar'

# Entrada de texto del usuario
texto = st.text_area('Ingrese el texto para clasificar:', '')

if st.button('Clasificar'):
    if texto:
        # Enviar la solicitud POST al servidor Flask
        response = requests.post(flask_url, data={'texto': texto})

        if response.status_code == 200:
            # Obtener la etiqueta clasificada
            resultado = response.json()
            st.write('La etiqueta más probable es:', resultado['label'])
        else:
            str.write('Error en la solicitud al servidor Flask.')
    else:
        str.write('Por favor, ingrese el texto a clasificar.')
