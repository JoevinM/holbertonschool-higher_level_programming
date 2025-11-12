#!/usr/bin/node

const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';

fetch(url)
  .then(response => response.json())
  .then(data => {
    const translationHello = document.querySelector('#hello');
    translationHello.textContent = data.hello;
  });
