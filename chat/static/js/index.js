
// document.querySelector('#news-form').addEventListener('submit', e => {
//     console.log('here')
//     var form = document.querySelector('#news-form')
//     var title = document.querySelector('.title');
//     var text = document.querySelector('.news');
//     window.setTimeout(5000);
//     console.log('here');
//     // if (!title.value || !text.value) {
//     //     const paste = document.querySelector('.container');
//     //     paste.insertAdjacentHTML('beforebegin', 
//     //     `<h3 style="color='red'>Потрібно заповнити всі необхідні поля</h3>`);
//     //     if (!title.value) 
//     //         title.classList.add("rd");
//     //         window.setTimeout(5000);
//     //     if (!text.value) 
//     //         title.classList.add("rd");
        
//     // } else {
//     //     form.action('/blog/save/')
//     //     form.method('POST')
//     //     form.submit()
//     // }
// })

function checkform() {
    var form = document.querySelector('#news-form')
    var title = document.querySelector('.title');
    var text = document.querySelector('.news');
    if(!title.value || !text.value) {
        document.querySelector('.container').insertAdjacentHTML('afterbegin', `<p style="color: red">Потрібно заповнити всі необхідні поля</p>`);

        if (!title.value) 
            title.classList.add("rd");
        if (!text.value)  
            text.classList.add("rd");
        return false;
    } else 
        document.news-form.submit();
}

document.querySelector('.title').addEventListener('click', e => {
    document.querySelector('.title').classList.remove('rd');
})

document.querySelector('.news').addEventListener('click', e => {
    document.querySelector('.news').classList.remove('rd');
})

