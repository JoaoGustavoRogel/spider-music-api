INSERT INTO tracks (
    track_id,
    track_name,
    track_url,
    disc_number,
    duration_ms,
    artist_id,
    track_number,
    popularity,
    album_id
) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);