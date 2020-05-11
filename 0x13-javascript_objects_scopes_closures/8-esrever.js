#!/usr/bin/node

function esrever (list) {
  const newList = [];
  list.forEach(element => {
    newList.unshift(element);
  });
  return newList;
}

module.exports.esrever = esrever;
