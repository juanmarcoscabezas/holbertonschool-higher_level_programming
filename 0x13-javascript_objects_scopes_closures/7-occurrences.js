#!/usr/bin/node

function nbOccurences (list, searchElement) {
  let occurrences = 0;
  list.forEach(element => {
    if (element === searchElement) {
      occurrences++;
    }
  });
  return occurrences;
}

module.exports.nbOccurences = nbOccurences;
