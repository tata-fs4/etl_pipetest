# etl_pipetest

Description:
O código apresentado realiza um fluxo de trabalho típico de ETL (Extração, Transformação e Carga) utilizando Apache Spark e Apache Hive em conjunto com o Hadoop Distributed File System (HDFS). Ele inicia uma sessão do Spark, lê dados de um arquivo CSV armazenado no HDFS, transforma esses dados renomeando uma coluna, e então os salva em formato Parquet no HDFS. Em seguida, o código cria uma tabela externa no Hive para facilitar consultas interativas e executa uma consulta SQL para exibir os dados. Por fim, a sessão do Spark é encerrada.
