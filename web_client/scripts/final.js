
var table = new Table();
var toAdd = {};

document.getElementById("searchbutton").onclick = function()
{
	buildTable(document.getElementById("search").value);
}

document.getElementById("addbutton").onclick = function()
{
	var row, key, val;
	row = document.createElement('tr');
	key = document.createElement('td');
	key.className = "mdl-data-table__cell--non-numeric";
	val = document.createElement('td');
	val.className = "mdl-data-table__cell--non-numeric";

	row.appendChild(key);
	row.appendChild(val);
	key.innerHTML = document.getElementById("key").value;
	val.innerHTML = document.getElementById("value").value;

	toAdd[key.innerHTML] = val.innerHTML;
	document.getElementById('add-table-body').appendChild(row);
}

document.getElementById("submitbutton").onclick = function()
{
	var pid = document.getElementById("name").value;

	var xhr = new XMLHttpRequest();
	xhr.open("PUT", "http://student04.cse.nd.edu:51020/planets/" + pid , true);
	xhr.onreadystatechange = function(){
		if(xhr.readyState == 4 && xhr.status == 200){
			if(JSON.parse(xhr.responseText)['result'] == 'error')
			{
				console.log("Error adding planet");
			}
		}
	}

	document.getElementById('add-table-body').innerHTML = "";
	xhr.send(JSON.stringify(toAdd));

	toAdd = {}

}

function buildTable(pid)
{
	var xhr = new XMLHttpRequest();
	xhr.open("GET", "http://student04.cse.nd.edu:51020/planets/" + pid , true);
	xhr.onreadystatechange = function(){
		if(xhr.readyState == 4 && xhr.status == 200){

			var result = JSON.parse(xhr.responseText);
			if(result['result'] == 'success')
			{
				table.createTable(result,pid);
			}
			else
			{
				table.createTable({'error':'not found'} , pid)
			}
		}
	}
	xhr.send(null);
}

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
				var c = new Card(buildTable);
				c.createCard(dict);
				c.addToDocument();
			}
		}
	}
	xhr.send(null);
}



//tr
//td class = "mdl-data-table__cell--non-numeric"> Key
//td Val
addPlanets()
