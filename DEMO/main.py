import sqlite3
import random
from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI(title="Hotel Reservas API")
DB_PATH = "reservas.db"


def init_db():
    """Crea la tabla e inserta 500 reservas ficticias."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS reservas")
    cur.execute("""
        CREATE TABLE reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            huesped TEXT NOT NULL,
            habitacion INTEGER NOT NULL,
            noches INTEGER NOT NULL,
            estado TEXT NOT NULL
        )
    """)

    estados = ["activa", "cancelada", "completada"]
    nombres = [
        "Ana García", "Carlos López", "María Fernández", "Jorge Martín",
        "Laura Sánchez", "Pedro Ruiz", "Lucía Díaz", "Andrés Torres",
        "Elena Moreno", "David Jiménez", "Sofía Romero", "Pablo Navarro",
        "Carmen Álvarez", "Raúl Molina", "Isabel Ortega", "Miguel Serrano",
        "Patricia Domínguez", "Fernando Muñoz", "Beatriz Castro", "Javier Gil"
    ]

    registros = []
    for _ in range(500):
        registros.append((
            random.choice(nombres),
            random.randint(100, 450),
            random.randint(1, 14),
            random.choice(estados),
        ))

    cur.executemany(
        "INSERT INTO reservas (huesped, habitacion, noches, estado) VALUES (?, ?, ?, ?)",
        registros,
    )
    conn.commit()
    conn.close()


# Inicializar la BD al arrancar
init_db()


# ──────────────────────────────────────────────
# BUG INTENCIONADO: el parámetro 'estado' se recibe
# pero la consulta SQL NUNCA lo usa para filtrar.
# Siempre devuelve SELECT * FROM reservas sin WHERE.
# ──────────────────────────────────────────────
@app.get("/reservas")
def listar_reservas(estado: Optional[str] = Query(None)):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # La query ignora 'estado' completamente
    cur.execute("SELECT * FROM reservas")

    filas = [dict(row) for row in cur.fetchall()]
    conn.close()
    return filas
