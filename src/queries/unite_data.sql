
select *
from rank_streamed_artists as ra
left join spotify_info as sp
on sp.name=ra.artist
left join past_concerts as pa
on sp.name=pa.artist
left join upcoming_concerts as up
on sp.name=up.artist
