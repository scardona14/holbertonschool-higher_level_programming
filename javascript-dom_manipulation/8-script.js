$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (data, textStatus) => {
    if (textStatus === 'success') {
        for (const i of data.results) {
          $('UL#list_movies').append('<li>>${i.title}</li>');
      }
    }
});