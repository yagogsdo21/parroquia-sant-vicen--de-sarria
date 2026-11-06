(function(){
  var burger=document.querySelector('.burger'),nav=document.querySelector('nav.main');
  if(burger&&nav){
    burger.addEventListener('click',function(){
      var o=nav.classList.toggle('open');burger.classList.toggle('open',o);burger.setAttribute('aria-expanded',o);
      document.body.style.overflow=o?'hidden':'';
    });
    document.querySelectorAll('nav.main .has-sub>a').forEach(function(a){
      a.addEventListener('click',function(e){
        if(window.innerWidth<=1060){e.preventDefault();a.parentElement.classList.toggle('open');}
      });
    });
    document.querySelectorAll('nav.main .sub a, nav.main>ul>li:not(.has-sub)>a').forEach(function(a){
      a.addEventListener('click',function(){nav.classList.remove('open');burger.classList.remove('open');document.body.style.overflow='';});
    });
  }
  var els=document.querySelectorAll('.reveal');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12});
    els.forEach(function(el){io.observe(el);});
  }else{els.forEach(function(el){el.classList.add('in');});}
})();
