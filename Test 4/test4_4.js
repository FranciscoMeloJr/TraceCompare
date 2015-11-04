//Simulating the Example 4.4
conn = new Mongo();
db = conn.getDB("SoccerLeague");

var d1, n1, a;
var d2, n2;

print ("Begin time:" + new Date().getTime());
for (j = 0; j < 5; j++) 
{
	var start = new Date().getTime();
	for (i = 0; i < 10000; i++) 
	{
		
		var a = {"name":"Buffalo Bills", "Conference":"American", "YearEstablished:":1965, "Number":i};
		db.Teams.save(a);
	}
	var end = new Date().getTime();
	print("Total time:" + (end - start));
	print("Mean time:" +(end - start)/i);

	db.dropDatabase();
}