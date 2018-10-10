async function getData(url) {
    return fetch(url)
        .then(response => response.json())
        // .then(json => console.log(json))
        .catch(error => console.log(error));
}

async function populate() {
    let [nums] = await Promise.all([
        getData('https://numbersapi.com/4')
    ]);

    // console.log(posts);
    // console.log(users);
    let postsDiv = document.querySelector('#nums');

    for (let num of nums) {
        let numId = num.id;
        let numTitle = num.title;
        let numBody = num.body;
        // console.log(postTitle);

        let numDiv = document.createElement('div');
        postDiv.classList.add('container', 'border', 'border-dark', 'rounded', 'mt-3');
        
    }
}
