INSERT INTO spotify_chart (
    position,
    track_name,
    artist_name,
    streams,
    url,
    track_id,
    chart_type,
    date,
    period,
    region
) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
