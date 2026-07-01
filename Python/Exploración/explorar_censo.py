import pyarrow.parquet as pq

archivo = r"Datos/viviendas_censo2024.parquet"

pf = pq.ParquetFile(archivo)

print("\nFILAS:")
print(pf.metadata.num_rows)

print("\nCOLUMNAS:")
print(pf.schema.names)

print("\nTIPOS:")
print(pf.schema)

print("\nPRIMERAS 5 FILAS:")
df_sample = pf.read_row_group(0).to_pandas().head(5)
print(df_sample)