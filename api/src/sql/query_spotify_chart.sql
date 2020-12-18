SELECT 
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
FROM 
	C214.spotify_chart
WHERE
	C214.spotify_chart.date >= %s AND C214.spotify_chart.date <= %s;