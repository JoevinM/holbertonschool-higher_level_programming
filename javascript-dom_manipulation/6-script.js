#!/usr/bin/node

  const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";

	fetch(url)
	.then(response => response.json())
	.then(data => {
		const nameCharacter = document.querySelector('#character');
		nameCharacter.textContent = data.name;
	})
