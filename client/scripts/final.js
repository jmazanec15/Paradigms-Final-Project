

function addPlanets()
{
	var xhr = new XMLHttpRequest();
	xhr.open("GET", "http://student04.cse.nd.edu:51020/planets/",true);
	xhr.onreadystatechange = function(){
		if(xhr.readyState == 4 && xhr.status == 200){
			var result = JSON.parse(xhr.responseText);
			for(key in result['planets'])
			{
				var dict = {};
				dict[key] = result['planets'][key];
				var c = new Card();
				c.createCard(dict);
				c.addToDocument();
			}
		}
	}
	xhr.send(null);
}


addPlanets()
