#!/usr/bin/node

  const url = "https://swapi-api.hbtn.io/api/films/?format=json";

	fetch(url)
	.then(response => response.json())
	.then(data => {
		const list_Movies = document.querySelector('#list_movies');
		data.results.forEach(film => {
		const li = document.createElement('li');
		li.textContent = film.title;
		list_Movies.appendChild(li);
		});
	})
