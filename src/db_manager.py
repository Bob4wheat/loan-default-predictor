import os
import time
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine

# Paths (run from repo root)
CSV_FILE_PATH = Path("data/raw/accepted_2007_to_2018Q4.csv")
DB_PATH = Path("data/database/loan_data.db")
CHUNK_SIZE = 50_000


def load_data_to_sql():
    if not CSV_FILE_PATH.exists():
        print(f"Error: Could not find {CSV_FILE_PATH}. Please check the path.")
        return

    # Ensure the database directory exists before connecting.
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    engine = create_engine(f"sqlite:///{DB_PATH}")

    print("Starting data ingestion. This might take a few minutes...")
    start_time = time.time()

    # Read the CSV in chunks. low_memory=False prevents mixed-type inference warnings
    chunk_iterator = pd.read_csv(CSV_FILE_PATH, chunksize=CHUNK_SIZE, low_memory=False)

    for i, chunk in enumerate(chunk_iterator):
        if_exists_behavior = "replace" if i == 0 else "append"
        chunk.to_sql(name="loans", con=engine, if_exists=if_exists_behavior, index=False)
        print(f"Inserted chunk {i + 1} ({(i + 1) * CHUNK_SIZE} rows processed)")

    end_time = time.time()
    print(f"\nSuccess! Data ingestion complete in {round(end_time - start_time, 2)} seconds.")


if __name__ == "__main__":
    load_data_to_sql()