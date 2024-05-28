IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'user')
BEGIN
  CREATE TABLE [user] (
    id VARCHAR(50) PRIMARY KEY,
    name TEXT
  );
END;


IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'playlist')
BEGIN
  CREATE TABLE [playlist] (
    id VARCHAR(50) PRIMARY KEY,
    user_id TEXT,
    name TEXT
  );
END;


IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'track')
BEGIN
  CREATE TABLE [track] (
    id VARCHAR(50) PRIMARY KEY,
    playlist_id TEXT,
    artist_id TEXT,
    album_id TEXT,
    name TEXT
  );
END;

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'album')
BEGIN
  CREATE TABLE [album] (
    id VARCHAR(50) PRIMARY KEY,
    name TEXT
  );
END;

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'artist')
BEGIN
  CREATE TABLE [artist] (
    id VARCHAR(50) PRIMARY KEY,
    name TEXT
  );
END;

