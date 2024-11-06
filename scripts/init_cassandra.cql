CREATE KEYSPACE IF NOT EXISTS analytics WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

CREATE TABLE IF NOT EXISTS analytics.events (
    user_id text,
    event text,
    PRIMARY KEY (user_id, event)
);
