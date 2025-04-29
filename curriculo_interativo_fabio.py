
import streamlit as st
import time

# Estilo personalizado
st.set_page_config(page_title="Currículo Interativo - Fábio Lucas", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
    }
    .section {
        border-left: 5px solid #4a90e2;
        padding-left: 20px;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.title("Fábio Lucas N. de Jesus")
st.subheader("Área: Administrativo")
st.write("Telefone: (21) 99097-1865 | Email: fabiolucastk175@gmail.com")

# Objetivo com animação
with st.container():
    st.markdown("### Objetivo Profissional", unsafe_allow_html=True)
    st.markdown("""
    <div class="section">
    Busco uma oportunidade que me permita desenvolver profissionalmente e contribuir para o sucesso da empresa, alinhando meus objetivos com os da organização.
    </div>
    """, unsafe_allow_html=True)
    st.balloons()

# Experiência
st.markdown("### Experiência Profissional")
st.markdown("""
<div class="section">
- 2019 - 2019 | **Auto Posto do Trabalho - Forza** – Frentista  
- 2015 - 2018 | **Supermercado JR Vale do Ipê** – Balconista de laticínios  
- 2019 - Atual | **Drogarias Pacheco**  
   - Atendente de loja (2019 a 2020)  
   - Balconista (2020 a 2024)  
   - Administrativo (cargo atual)  
</div>
""", unsafe_allow_html=True)
st.progress(70)

# Formação
st.markdown("### Formação Acadêmica")
st.markdown("""
<div class="section">
2022 - 2025 | **Universidade Estácio de Sá**  
Curso: Análise e Desenvolvimento de Sistemas
</div>
""", unsafe_allow_html=True)
time.sleep(0.5)
st.success("Formação em andamento")

# Certificações
st.markdown("### Certificações")
st.markdown("""
<div class="section">
- Programação de algoritmos escaláveis  
- Programação de sistemas de informação  
- Programação para dispositivos móveis  
- Programação para internet  
</div>
""", unsafe_allow_html=True)
st.info("Certificações técnicas atualizadas")

# Rodapé
st.markdown("---")
st.caption("Currículo interativo desenvolvido com Streamlit")
