conn = new Mongo();
db = conn.getDB("SoccerLeague");

for (i = 0; i < 100; i++) 
{
	var a = {"name":"Buffalo Bills", "Conference":"American", "YearEstablished:":1965};
}

db.Teams.save(a);

