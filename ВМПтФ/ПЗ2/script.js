

// 1) Fetch data from remote API
async function getBeasts() {
    try {
      const response = await fetch(
        'https://raw.githubusercontent.com/erdoganishe/6Semestr/f1b4782bfe02e7e23872a0fbe7f79c1ddddf5c23/%D0%92%D0%9C%D0%9F%D1%82%D0%A4/%D0%9F%D0%972/beasts.json',
        {
          method: 'GET',
        },
      );
  
      if (!response.ok) {
        throw new Error(`Error! status: ${response.status}`);
      }
  
      const data = await response.json();
      console.log(data);
      return data;
    } catch (error) {
      console.log(error);
    }
  }

  getBeasts().then(data => {
    console.log(data);
  
    const list = document.getElementById("list")
  
    data.forEach(beast => {
      const li = document.createElement('li');
      li.innerHTML = beast.name + "   " + beast.type;
      const image = document.createElement('img');
      image.src = beast.photo;
      image.style.width = '100px';
      image.style.height = '100px';
      li.appendChild(image);
      li.style.fontSize = '22px';
      
     
  
      list.appendChild(li);
    });

  });

