INSERT INTO artists (
    artist_id,
    artist_name,
    artist_url,
    track_number,
    disc_number,
    popularity,
    followers
) VALUES(%s, %s, %s, %s, %s, %s, %s);
