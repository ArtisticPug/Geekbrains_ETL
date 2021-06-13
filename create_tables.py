import psycopg2


config = {
    'constring_a': "host='localhost' port=54320 dbname='database_a' user='postgres' password='postgres'",
    'constring_b': "host='localhost' port=54321 dbname='database_b' user='postgres' password='postgres'",
    'constring_c': "host='localhost' port=54322 dbname='database_c' user='postgres' password='postgres'",
    'sae_schema_query': 'CREATE SCHEMA sae;',
    'sal_schema_query': 'CREATE SCHEMA sal;',
    'dds_schema_query': 'CREATE SCHEMA dds;',
    'statistic_schema_query': 'CREATE SCHEMA statistic;',
    'sal_table_query': '''
  SET search_path TO sal;

  CREATE TABLE NATION  ( NATION_bk  INTEGER NOT NULL,
                        NAME         CHAR(25) NOT NULL,
                        REGION_bk    INTEGER NOT NULL,
                        COMMENT      VARCHAR(152),
                        launch_id      int,
                        effective_dttm date DEFAULT now());

  CREATE TABLE REGION  ( REGION_bk  INTEGER NOT NULL,
                        NAME         CHAR(25) NOT NULL,
                        COMMENT      VARCHAR(152),
                        launch_id      int,
                        effective_dttm date DEFAULT now());

  CREATE TABLE PART  ( PART_bk     INTEGER NOT NULL,
                      NAME         VARCHAR(55) NOT NULL,
                      MFGR         CHAR(25) NOT NULL,
                      BRAND        CHAR(10) NOT NULL,
                      TYPE         VARCHAR(25) NOT NULL,
                      SIZE         INTEGER NOT NULL,
                      CONTAINER    CHAR(10) NOT NULL,
                      RETAILPRICE  DECIMAL(15,2) NOT NULL,
                      COMMENT      VARCHAR(23) NOT NULL ,
                      launch_id      int,
                      effective_dttm date DEFAULT now());

  CREATE TABLE SUPPLIER ( supplier_bk     INTEGER NOT NULL,
                          NAME         CHAR(25) NOT NULL,
                          ADDRESS      VARCHAR(40) NOT NULL,
                          NATION_bk   INTEGER NOT NULL,
                          PHONE        CHAR(15) NOT NULL,
                          ACCTBAL      DECIMAL(15,2) NOT NULL,
                          COMMENT      VARCHAR(101) NOT NULL,
                          launch_id      int,
                          effective_dttm date DEFAULT now());

  CREATE TABLE PARTSUPP ( PART_bk     INTEGER NOT NULL,
                          SUPPlier_bk     INTEGER NOT NULL,
                          AVAILQTY    INTEGER NOT NULL,
                          SUPPLYCOST  DECIMAL(15,2)  NOT NULL,
                          COMMENT     VARCHAR(199) NOT NULL,
                          launch_id      int,
                          effective_dttm date DEFAULT now());

  CREATE TABLE CUSTOMER ( CUSTomer_bk     INTEGER NOT NULL,
                          NAME         VARCHAR(25) NOT NULL,
                          ADDRESS      VARCHAR(40) NOT NULL,
                          NATION_bk    INTEGER NOT NULL,
                          PHONE        CHAR(15) NOT NULL,
                          ACCTBAL      DECIMAL(15,2)   NOT NULL,
                          MKTSEGMENT   CHAR(10) NOT NULL,
                          COMMENT      VARCHAR(117) NOT NULL,
                          launch_id      int,
                          effective_dttm date DEFAULT now());

  CREATE TABLE ORDERS  ( orders_bk       INTEGER NOT NULL,
                        CUSTomer_bk        INTEGER NOT NULL,
                        ORDERSTATUS    CHAR(1) NOT NULL,
                        TOTALPRICE     DECIMAL(15,2) NOT NULL,
                        ORDERDATE      DATE NOT NULL,
                        ORDERPRIORITY  CHAR(15) NOT NULL,  
                        CLERK          CHAR(15) NOT NULL, 
                        SHIPPRIORITY   INTEGER NOT NULL,
                        COMMENT        VARCHAR(79) NOT NULL,
                        launch_id        int,
                        effective_dttm   date DEFAULT now());

  CREATE TABLE LINEITEM ( orders_bk    INTEGER NOT NULL,
                          PART_BK        INTEGER NOT NULL,
                          SUPPlier_bk        INTEGER NOT NULL,
                          LINENUMBER     INTEGER NOT NULL,
                          QUANTITY       DECIMAL(15,2) NOT NULL,
                          EXTENDEDPRICE  DECIMAL(15,2) NOT NULL,
                          DISCOUNT       DECIMAL(15,2) NOT NULL,
                          TAX            DECIMAL(15,2) NOT NULL,
                          RETURNFLAG     CHAR(1) NOT NULL,
                          LINESTATUS     CHAR(1) NOT NULL,
                          SHIPDATE       DATE NOT NULL,
                          COMMITDATE     DATE NOT NULL,
                          RECEIPTDATE    DATE NOT NULL,
                          SHIPINSTRUCT   CHAR(25) NOT NULL,
                          SHIPMODE       CHAR(10) NOT NULL,
                          COMMENT        VARCHAR(44) NOT NULL,
                          launch_id        int,
                          effective_dttm   date DEFAULT now());
''',
    'sae_table_query': '''
  SET search_path TO sae;

  CREATE TABLE NATION  ( NATION_bk  INTEGER NOT NULL,
                        NAME         CHAR(25) NOT NULL,
                        REGION_bk    INTEGER NOT NULL,
                        COMMENT      VARCHAR(152),
                        launch_id      int,
                        effective_dttm date DEFAULT now());

  CREATE TABLE REGION  ( REGION_bk  INTEGER NOT NULL,
                        NAME         CHAR(25) NOT NULL,
                        COMMENT      VARCHAR(152),
                        launch_id      int,
                        effective_dttm date DEFAULT now());

  CREATE TABLE PART  ( PART_bk     INTEGER NOT NULL,
                      NAME         VARCHAR(55) NOT NULL,
                      MFGR         CHAR(25) NOT NULL,
                      BRAND        CHAR(10) NOT NULL,
                      TYPE         VARCHAR(25) NOT NULL,
                      SIZE         INTEGER NOT NULL,
                      CONTAINER    CHAR(10) NOT NULL,
                      RETAILPRICE  DECIMAL(15,2) NOT NULL,
                      COMMENT      VARCHAR(23) NOT NULL ,
                      launch_id      int,
                      effective_dttm date DEFAULT now());

  CREATE TABLE SUPPLIER ( SUPPlier_bk     INTEGER NOT NULL,
                          NAME         CHAR(25) NOT NULL,
                          ADDRESS      VARCHAR(40) NOT NULL,
                          NATION_bk   INTEGER NOT NULL,
                          PHONE        CHAR(15) NOT NULL,
                          ACCTBAL      DECIMAL(15,2) NOT NULL,
                          COMMENT      VARCHAR(101) NOT NULL,
                          launch_id      int,
                          effective_dttm date DEFAULT now());

  CREATE TABLE PARTSUPP ( PART_bk     INTEGER NOT NULL,
                          SUPPlier_bk     INTEGER NOT NULL,
                          AVAILQTY    INTEGER NOT NULL,
                          SUPPLYCOST  DECIMAL(15,2)  NOT NULL,
                          COMMENT     VARCHAR(199) NOT NULL,
                          launch_id      int,
                          effective_dttm date DEFAULT now());

  CREATE TABLE CUSTOMER ( CUSTomer_bk     INTEGER NOT NULL,
                          NAME         VARCHAR(25) NOT NULL,
                          ADDRESS      VARCHAR(40) NOT NULL,
                          NATION_bk    INTEGER NOT NULL,
                          PHONE        CHAR(15) NOT NULL,
                          ACCTBAL      DECIMAL(15,2)   NOT NULL,
                          MKTSEGMENT   CHAR(10) NOT NULL,
                          COMMENT      VARCHAR(117) NOT NULL,
                          launch_id      int,
                          effective_dttm date DEFAULT now());

  CREATE TABLE ORDERS  ( orders_bk       INTEGER NOT NULL,
                        CUSTomer_bk        INTEGER NOT NULL,
                        ORDERSTATUS    CHAR(1) NOT NULL,
                        TOTALPRICE     DECIMAL(15,2) NOT NULL,
                        ORDERDATE      DATE NOT NULL,
                        ORDERPRIORITY  CHAR(15) NOT NULL,  
                        CLERK          CHAR(15) NOT NULL, 
                        SHIPPRIORITY   INTEGER NOT NULL,
                        COMMENT        VARCHAR(79) NOT NULL,
                        launch_id        int,
                        effective_dttm   date DEFAULT now());

  CREATE TABLE LINEITEM ( orders_bk   INTEGER NOT NULL,
                          PART_bk        INTEGER NOT NULL,
                          SUPPlier_bk        INTEGER NOT NULL,
                          LINENUMBER     INTEGER NOT NULL,
                          QUANTITY       DECIMAL(15,2) NOT NULL,
                          EXTENDEDPRICE  DECIMAL(15,2) NOT NULL,
                          DISCOUNT       DECIMAL(15,2) NOT NULL,
                          TAX            DECIMAL(15,2) NOT NULL,
                          RETURNFLAG     CHAR(1) NOT NULL,
                          LINESTATUS     CHAR(1) NOT NULL,
                          SHIPDATE       DATE NOT NULL,
                          COMMITDATE     DATE NOT NULL,
                          RECEIPTDATE    DATE NOT NULL,
                          SHIPINSTRUCT   CHAR(25) NOT NULL,
                          SHIPMODE       CHAR(10) NOT NULL,
                          COMMENT        VARCHAR(44) NOT NULL,
                          launch_id        int,
                          effective_dttm   date DEFAULT now());
''',
    'dds_table_query': '''
  SET search_path TO dds;

  CREATE TABLE dds.h_customer (
    h_customer_rk SERIAL NOT NULL,
    customer_bk int4 NOT NULL,
    launch_id        int,
    source_system varchar(50),
    proccesed_dttm date NULL DEFAULT now()
  );


  CREATE TABLE dds.s_customer (
    h_customer_rk int4 NOT NULL,	
    name varchar(25) NOT NULL,
    address varchar(40) NOT NULL,
    phone bpchar(15) NOT NULL,
    acctbal numeric(15,2) NOT NULL,
    mktsegment bpchar(10) NOT NULL,
    comment varchar(117) NOT NULL,
    launch_id        int,
    valid_from date NULL DEFAULT now(),
    valid_to date,
    source_system varchar(50),
    proccesed_dttm date NULL DEFAULT now()
  );

  CREATE TABLE dds.h_part (
    h_part_rk SERIAL NOT NULL,
    part_bk int4 NOT NULL,
    launch_id        int,
    source_system varchar(50),
    proccesed_dttm date NULL DEFAULT now()
  );

  CREATE TABLE dds.s_part (
    h_part_rk int4 NOT NULL,
    name varchar(55) NOT NULL,
    mfgr bpchar(25) NOT NULL,
    brand bpchar(10) NOT NULL,
    type varchar(25) NOT NULL,
    size int4 NOT NULL,
    container bpchar(10) NOT NULL,
    retailprice numeric(15,2) NOT NULL,
    comment varchar(23) NOT NULL,
    launch_id        int,
    valid_from date NULL DEFAULT now(),
    valid_to date,
    source_system varchar(50),
    proccesed_dttm date NULL DEFAULT now()
  );

  CREATE TABLE dds.h_nation (
    h_nation_rk SERIAL NOT NULL,
    nation_bk int4 NOT NULL,
    launch_id        int,
    source_system varchar(50),
    proccesed_dttm date NULL DEFAULT now()
  );

  CREATE TABLE dds.s_nation (
    h_nation_rk int4 NOT NULL,
    name bpchar(25) NOT NULL,
    comment varchar(152) NULL,
    launch_id        int,
    valid_from date NULL DEFAULT now(),
    valid_to date,
    source_system varchar(50),
    proccesed_dttm date NULL DEFAULT now()
  );

  CREATE TABLE dds.h_region (
    h_region_rk SERIAL NOT NULL,
    region_bk int4 NOT NULL,
    launch_id        int,
    source_system varchar(50),
    proccesed_dttm date NULL DEFAULT now()
  );

  CREATE TABLE dds.s_region (
    h_region_rk int4 NOT NULL,
    name bpchar(25) NOT NULL,
    comment varchar(152) NULL,
    launch_id        int,
    valid_from date NULL DEFAULT now(),
    valid_to date,
    source_system varchar(50),
    proccesed_dttm date NULL DEFAULT now()
  );

  CREATE TABLE dds.h_supplier (
    h_supplier_rk SERIAL NOT NULL,
    supplier_bk int4 NOT NULL,
    launch_id        int,
    source_system varchar(50),
    proccesed_dttm date NULL DEFAULT now()
  );

  CREATE TABLE dds.s_supplier (
    h_supplier_rk int4 NOT NULL,
    name bpchar(25) NOT NULL,
    address varchar(40) NOT NULL,
    phone bpchar(15) NOT NULL,
    acctbal numeric(15,2) NOT NULL,
    comment varchar(101) NOT NULL,
    launch_id        int,
    valid_from date NULL DEFAULT now(),
    valid_to date,
    source_system varchar(50),
    proccesed_dttm date NULL DEFAULT now()
  );


  CREATE TABLE dds.h_orders (
    h_orders_rk SERIAL NOT NULL,
    orders_bk int4 NOT NULL,
    launch_id        int,
    source_system varchar(50),
    proccesed_dttm date NULL DEFAULT now()
  );

  CREATE TABLE dds.s_orders (
    h_orders_rk int4 NOT NULL,
    orderstatus bpchar(1) NOT NULL,
    totalprice numeric(15,2) NOT NULL,
    orderdate date NOT NULL,
    orderpriority bpchar(15) NOT NULL,
    clerk bpchar(15) NOT NULL,
    shippriority int4 NOT NULL,
    comment varchar(79) NOT NULL,
    launch_id        int,
    valid_from date NULL DEFAULT now(),
    valid_to date,
    source_system varchar(50),
    proccesed_dttm date NULL DEFAULT now()
  );

  CREATE TABLE dds.l_customer_nation (
    l_customer_nation_rk SERIAL NOT NULL,
    h_customer_rk int4 NOT NULL,
    h_nation_rk int4 NOT NULL,
    launch_id        int,
    source_system varchar(50),
    proccesed_dttm date NULL DEFAULT now()
  );

  CREATE TABLE dds.l_customer_orders (
    l_customer_orders_rk SERIAL NOT NULL,
    h_customer_rk int4 NOT NULL,
    h_orders_rk int4 NOT NULL,
    launch_id        int,
    source_system varchar(50),
    proccesed_dttm date NULL DEFAULT now()
  );

  CREATE TABLE dds.l_orders_part_supplier (
    l_orders_part_supplier_rk SERIAL NOT NULL,
    h_orders_rk int4 NOT NULL,
    h_part_rk int4 NOT NULL,
    h_supplier_rk int4 NOT NULL,
    launch_id        int,
    source_system varchar(50),
    proccesed_dttm date NULL DEFAULT now()
  );

  CREATE TABLE dds.l_nation_region (
    l_nation_region_rk SERIAL NOT NULL,
    h_region_rk int4 NOT NULL,
    h_nation_rk int4 NOT NULL,
    launch_id        int,
    source_system varchar(50),
    proccesed_dttm date NULL DEFAULT now()
  );

  CREATE TABLE dds.l_nation_supplier (
    l_nation_supplier_rk SERIAL NOT NULL,
    h_supplier_rk int4 NOT NULL,
    h_nation_rk int4 NOT NULL,
    launch_id        int,
    source_system varchar(50),
    proccesed_dttm date NULL DEFAULT now()
  );

  CREATE TABLE dds.l_part_supplier (
    l_part_supplier_rk SERIAL NOT NULL,
    h_part_rk int4 NOT NULL,
    h_supplier_rk int4 NOT NULL,
    launch_id        int,
    source_system varchar(50),
    proccesed_dttm date NULL DEFAULT now()
  );

  CREATE TABLE dds.l_s_orders_part_supplier (
    l_orders_part_supplier_rk int4 NOT NULL,
    linenumber int4 NOT NULL,
    quantity numeric(15,2) NOT NULL,
    extendedprice numeric(15,2) NOT NULL,
    discount numeric(15,2) NOT NULL,
    tax numeric(15,2) NOT NULL,
    returnflag bpchar(1) NOT NULL,
    linestatus bpchar(1) NOT NULL,
    shipdate date NOT NULL,
    commitdate date NOT NULL,
    receiptdate date NOT NULL,
    shipinstruct bpchar(25) NOT NULL,
    shipmode bpchar(10) NOT NULL,
    comment varchar(44) NOT NULL,
    launch_id        int,
    valid_from date NULL DEFAULT now(),
    valid_to date,
    source_system varchar(50),
    proccesed_dttm date NULL DEFAULT now()
  );

  CREATE TABLE dds.l_s_part_supplier (
    l_part_supplier_rk int4 NOT NULL,
    availqty int4 NOT NULL,
    supplycost numeric(15,2) NOT NULL,
    comment varchar(199) NOT NULL,
    launch_id        int,
    valid_from date NULL DEFAULT now(),
    valid_to date,
    source_system varchar(50),
    proccesed_dttm date NULL DEFAULT now()
  );
''',
    'statistic_query': """
  SET search_path TO statistic;

  create table statistic (
        table_name     text
      , columname    text
      , cnt_nulls      int
      , cnt_all        int
      , load_date      date
  );
""",
    'log_query': """
  SET search_path TO statistic;

  create table log (
        source_launch_id    int
      , target_schema       text
      , target_table        text  
      , target_launch_id    int
      , processed_dttm      timestamp default now()
      , row_count           int
      , duration            interval
      , load_date           date
  );
"""
}

if __name__ == "__main__":

    with psycopg2.connect(config['constring_b']) as conn:

        cursor = conn.cursor()
        cursor.execute(config['sae_schema_query'])
        cursor.execute(config['sae_table_query'])
        cursor.execute(config['sal_schema_query'])
        cursor.execute(config['sal_table_query'])
        cursor.execute(config['dds_schema_query'])
        cursor.execute(config['dds_table_query'])

    with psycopg2.connect(config['constring_c']) as conn:

        cursor = conn.cursor()
        cursor.execute(config['statistic_schema_query'])
        cursor.execute(config['statistic_query'])
        cursor.execute(config['log_query'])
