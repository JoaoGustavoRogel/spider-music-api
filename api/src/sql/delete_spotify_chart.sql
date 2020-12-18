DELETE FROM C214.spotify_chart 
WHERE
	C214.spotify_chart.date >= %s AND
	C214.spotify_chart.date <= %s;