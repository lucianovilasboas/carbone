import streamlit as st

def main():
    st.title("Calculadora de Pegada de Carbono")
    
    st.header("1. Energia e Eletricidade")
    eletricidade = st.number_input("Consumo mensal de eletricidade (kWh):", min_value=0.0, step=1.0)
    emissao_eletricidade = eletricidade * 0.5  # Média de emissão por kWh (em kg de CO2)

    st.header("2. Transporte")
    km_carro = st.number_input("Quilômetros percorridos de carro por mês:", min_value=0.0, step=1.0)
    tipo_combustivel = st.selectbox("Tipo de combustível:", ["Gasolina", "Diesel", "Álcool"])
    
    if tipo_combustivel == "Gasolina":
        emissao_carro = km_carro * 0.2  # Emissão média para gasolina (em kg de CO2 por km)
    elif tipo_combustivel == "Diesel":
        emissao_carro = km_carro * 0.27  # Emissão média para diesel
    else:
        emissao_carro = km_carro * 0.1  # Emissão média para álcool

    st.header("3. Resíduos")
    quantidade_residuos = st.number_input("Quantidade de resíduos produzidos por semana (kg):", min_value=0.0, step=1.0)
    emissao_residuos = quantidade_residuos * 4 * 0.1  # Aproximação para CO2 por kg de resíduo em um mês

    st.header("4. Alimentação")
    dieta = st.selectbox("Qual o seu tipo de dieta?", ["Onívora", "Vegetariana", "Vegana"])
    
    if dieta == "Onívora":
        emissao_alimentacao = 300  # Aproximação de emissão mensal em kg de CO2
    elif dieta == "Vegetariana":
        emissao_alimentacao = 200
    else:
        emissao_alimentacao = 150

    emissao_total = emissao_eletricidade + emissao_carro + emissao_residuos + emissao_alimentacao
    
    st.subheader("Resultados")
    st.write(f"Emissões de eletricidade: {emissao_eletricidade:.2f} kg CO2 por mês")
    st.write(f"Emissões de transporte: {emissao_carro:.2f} kg CO2 por mês")
    st.write(f"Emissões de resíduos: {emissao_residuos:.2f} kg CO2 por mês")
    st.write(f"Emissões de alimentação: {emissao_alimentacao:.2f} kg CO2 por mês")
    st.write(f"Emissão total estimada: {emissao_total:.2f} kg CO2 por mês")

if __name__ == "__main__":
    main()
