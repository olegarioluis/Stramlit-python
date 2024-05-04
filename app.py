import streamlit as st

with st.sidebar:
    st.title('FORMULA DE BHASKARA')
    st.header('Definição:')
    st.write('A fórmula de Bhaskara é um cálculo matemático para determinar as raízes de uma função de segundo grau por meio de seus coeficientes. Esse coeficiente que multiplica a variável desconhecida (x) das equações. A termologia da fórmula é uma homenagem ao seu criador, o professor e astrólogo indiano Bhaskara Akaria.')

st.title('FORMULA DE BHASKARA')

valor_a = st.number_input(label='Digite o valor de A:',
                          value=None, format="%d", step=1)
valor_b = st.number_input(label='Digite o valor de b:',
                          value=None, format="%d", step=1)
valor_c = st.number_input(label='Digite o valor de c:',
                          value=None, format="%d", step=1)

if st.button('Calcular'):
    delta_ = (valor_b ** 2) - (4 * valor_a * valor_c)

    def delta():
        st.header('DELTA')
        st.write('Δ = b² - 4 * a * c')
        st.write(f'Δ = {valor_b}² - 4 * {valor_a} * {valor_c}')
        st.write(f'Δ = {valor_b ** 2} - 4 * {valor_a} * {valor_c}')
        st.write(f'Δ = {valor_b ** 2} - {4 * valor_a * valor_c}')
        st.write(f'Δ = {valor_b ** 2 - (4 * valor_a * valor_c)}')

    def x1():
        st.header('VALOR DE X1')
        st.write('X1 = (-b + √Δ) / (2 * a)')
        st.write(f'X1 = ({ - valor_b} + √{delta_}) / (2 * {valor_a})')
        st.write(f'X1 = ({ - valor_b} + {delta_ ** (1/2)}) / ({2 * valor_a})')
        st.write(f'X1 = ({ - valor_b + (delta_ ** (1/2))}) / ({2 * valor_a})')
        st.write(f'X1 = {( - valor_b + (delta_ ** (1/2))) / (2 * valor_a)}')

    def x2():
        st.header('VALOR DE X2')
        st.write('X2 = (-b - √Δ) / (2 * a)')
        st.write(f'X2 = ({ - valor_b} - √{delta_}) / (2 * {valor_a})')
        st.write(f'X2 = ({ - valor_b} - {delta_ ** (1/2)}) / ({2 * valor_a})')
        st.write(f'X2 = ({ - valor_b - (delta_ ** (1/2))}) / ({2 * valor_a})')
        st.write(f'X2 = {( - valor_b - (delta_ ** (1/2))) / (2 * valor_a)}')

    col1, col2, col3 = st.columns(3)

    col1.metric = (delta())
    st.divider()
    col2.metric = (x1())
    st.divider()
    col3.metric = (x2())