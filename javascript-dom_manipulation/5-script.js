#!/usr/bin/node

const header = document.querySelector('header');
const updateHeader = document.querySelector('#update_header');

updateHeader.addEventListener('click', (event) => {
  header.innerHTML = 'New Header!!!';
});
