const routes = {
    '/': showHomePage,
    '/film': showFilmPage,
    '/television': showTelevisionPage,
    '/books': showBookPage,
    '/videogames': showVideoGamePage
}

function showHomePage() {

}

function showFilmPage() {

}

function showTelevisionPage() {

}

function showBookPage() {

}

function showVideoGamePage() {

}

window.addEventListener('popstate', () => {
    const currentRoute = window.location.pathname;
    if (routes[currentRoute]) {
        routes[currentRoute]();
    } else {
        showHomePage();
    }
})