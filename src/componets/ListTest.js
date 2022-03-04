import React from 'react';

const ListTest = (props) => {
    const animals = props.animals;
    const listItems = animals.map(animal => (<li key={animal.id}>{animal.name}</li>));
    return (
        <ul>{listItems}</ul>
    )
  }

export default ListTest;