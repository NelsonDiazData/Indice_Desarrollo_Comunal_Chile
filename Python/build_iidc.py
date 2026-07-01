from Analytics.iidc_utils import (
    obtener_dataset_iidc,
    validar_dataset_iidc,
    seleccionar_variables_iidc,
    transformar_variables_iidc,
    normalizar_variables_iidc,
    calcular_dimensiones_iidc,
    calcular_iidc,
    exportar_dataset_iidc,
    cargar_iidc_sql,
)


def main():
    df = obtener_dataset_iidc()
    df = validar_dataset_iidc(df)
    df_iidc = seleccionar_variables_iidc(df)
    df_iidc = transformar_variables_iidc(df_iidc)
    df_iidc = normalizar_variables_iidc(df_iidc)
    df_iidc = calcular_dimensiones_iidc(df_iidc)
    df_iidc = calcular_iidc(df_iidc)
    df_iidc = exportar_dataset_iidc(df_iidc)
    df_iidc = cargar_iidc_sql(df_iidc)

    print("\nPrimeras filas del dataset IIDC normalizado:")
    print(df_iidc.head())

    print("\nColumnas finales:")
    print(df_iidc.columns.tolist())

    print("\nShape final:")
    print(df_iidc.shape)


if __name__ == "__main__":
    main()