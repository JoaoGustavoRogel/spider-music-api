INSERT INTO albums (
    album_id,
    album_name,
    album_url,
    total_tracks,
    release_date,
    artist_id,
    popularity,
    label
) VALUES(%s, %s, %s, %s, %s, %s, %s, %s);