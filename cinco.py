#!/usr/bin/env python
'''
ETL [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para manipular la base de datos de productos
'''

__author__ = "Johana Rangel"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import sqlite3


def create_schema():
    conn = sqlite3.connect('cinco.db')
    c = conn.cursor()

    # Ejecutar una query
    c.execute("""
                DROP TABLE IF EXISTS multiplo_cinco;
            """)

    # Ejecutar una query
    c.execute(""" 
            CREATE TABLE multiplo_cinco(
                [numero] INTEGER PRIMARY KEY AUTOINCREMENT,
                [multiplos] INTEGER NOT NULL
                
            );
            """)

    conn.commit()
    conn.close()


def insert_multiplo(resultado):
    conn = sqlite3.connect('cinco.db')
    c = conn.cursor()

    c.execute("""
        INSERT INTO multiplo_cinco (multiplos)
        VALUES (?);""", (resultado,))

    conn.commit()
    conn.close()
