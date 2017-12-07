function Card(tableFunc){
	this.createCard = function(dict)
	{
		this.element = document.createElement("div")
		this.element.className = "mdl-cell mdl-cell--3-col graybox"
		this.card = document.createElement("div")
		this.card.className ="planet-card mdl-card mdl-shadow--2dp"
		this.title = document.createElement("div")
		this.title.className ="mdl-card__title"
		this.titleText = document.createElement("h2")
		this.titleText.className = "mdl-card__title-text"

		this.supportingText = document.createElement("div")
		this.supportingText.className = "mdl-card__supporting-text"

		this.actions = document.createElement("div")
		this.actions.className = "mdl-card__actions mdl-card--border"


		var key = Object.keys(dict)[0];


		this.button = document.createElement("a")
		this.button.className = "mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect"
		this.button.onclick =  function(){			
			tableFunc(key);
			document.getElementById('tab2').click();
			
		};

		
		this.titleText.innerHTML = key;

		
		this.supportingText.innerHTML = "Radius: "+ dict[key]["radius"] + "<br />";
		this.supportingText.innerHTML += "Mass: " + dict[key]["mass"] + "<br />";

		this.button.innerHTML = "More Info";

		this.element.appendChild(this.card)
		this.card.appendChild(this.title)
		this.title.appendChild(this.titleText)
		this.card.appendChild(this.supportingText)
		this.card.appendChild(this.actions)
		this.actions.appendChild(this.button)
	}

	this.addToDocument = function()
	{
		document.getElementById("card-grid").appendChild(this.element)
	}
}

//tr
//td class = "mdl-data-table__cell--non-numeric"> Key
//td Val
function Table(){

	
	this.createTable = function(dict, pid)
	{
		document.getElementById('planet-table-body').innerHTML = "";
		this.row = document.createElement('tr');
		this.key = document.createElement('td');
		this.key.className = "mdl-data-table__cell--non-numeric";
		this.val = document.createElement('td');
		this.val.className = "mdl-data-table__cell--non-numeric";

		this.row.appendChild(this.key);
		this.row.appendChild(this.val);
		this.key.innerHTML = "name";
		this.val.innerHTML = pid;

		document.getElementById('planet-table-body').appendChild(this.row);
		for(key in dict)
		{
			if(key == 'result')
			{
				continue;
			}
			this.row = document.createElement('tr');
			this.key = document.createElement('td');
			this.key.className = "mdl-data-table__cell--non-numeric";
			this.val = document.createElement('td');
			this.val.className = "mdl-data-table__cell--non-numeric";

			this.row.appendChild(this.key);
			this.row.appendChild(this.val);
			this.key.innerHTML = key;
			this.val.innerHTML = dict[key];

			document.getElementById('planet-table-body').appendChild(this.row);
		}
	}
}