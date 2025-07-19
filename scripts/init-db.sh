#!/bin/bash

sqlite3 db/f1-dashboardd.db <<EOF

CREATE TABLE IF NOT EXIST race_results (

);