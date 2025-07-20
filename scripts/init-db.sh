#!/bin/bash

echo "Starting init-db.sh"

sqlite3 db/f1-dashboard.db <<EOF

CREATE TABLE IF NOT EXISTS race_results (
    DriverNumber INTEGER, 
    Abbreviation TEXT,
    DriverId TEXT,
    TeamName TEXT,
    TeamColor TEXT,
    TeamId TEXT,
    FullName TEXT,
    CountryCode TEXT,
    Position REAL,
    ClassifiedPosition TEXT,
    GridPosition REAL,
    Time INTEGER,
    Status TEXT,
    Points REAL,
    Laps REAL,
    Event TEXT,
    PRIMARY KEY (DriverId, Event)
);
EOF

echo "Finished Running!"