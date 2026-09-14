\set ON_ERROR_STOP on
-- Supplied standalone experiment; connection-local generated data.
CREATE TEMP TABLE measurements AS
SELECT g AS id,g % 1000 AS batch FROM generate_series(1,50000) AS g;
ANALYZE measurements;
EXPLAIN (ANALYZE,BUFFERS) SELECT * FROM measurements WHERE batch=42;
CREATE INDEX measurements_batch_idx ON measurements(batch);
ANALYZE measurements;
EXPLAIN (ANALYZE,BUFFERS) SELECT * FROM measurements WHERE batch=42;
SELECT count(*) FROM measurements WHERE batch=42;
