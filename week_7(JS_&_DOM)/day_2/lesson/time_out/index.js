function showBanner(){
  const bannerElement = document.querySelector('#banner');
  bannerElement.removeAttribute('style');
}

setTimeout(showBanner, 10000);