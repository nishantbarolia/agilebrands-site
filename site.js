(function(){
  // Roles (homepage)
  var roles=document.querySelectorAll('.role');
  roles.forEach(function(b){b.addEventListener('click',function(){
    var on=b.getAttribute('aria-pressed')==='true';
    roles.forEach(function(x){x.setAttribute('aria-pressed','false')});
    document.querySelectorAll('.rpanel').forEach(function(p){p.classList.remove('on')});
    if(!on){b.setAttribute('aria-pressed','true');document.getElementById(b.dataset.panel).classList.add('on')}
  })});

  // Waitlist modal
  var modal=document.getElementById('waitlist');if(!modal)return;
  var dlg=modal.querySelector('.dlg'),form=modal.querySelector('form'),sel=form.querySelector('select[name=course]'),title=modal.querySelector('#wl-title'),err=modal.querySelector('.err'),last=null;
  function open(course,label){last=document.activeElement;dlg.classList.remove('done');err.style.display='none';form.reset();
    if(course&&sel){sel.value=course}title.textContent=label||'Join the waitlist';modal.classList.add('on');setTimeout(function(){form.querySelector('input[name=name]').focus()},30)}
  function close(){modal.classList.remove('on');if(last)last.focus()}
  document.querySelectorAll('[data-waitlist]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();open(a.dataset.waitlist,a.dataset.label)})});
  modal.querySelectorAll('[data-close]').forEach(function(b){b.addEventListener('click',close)});
  modal.addEventListener('click',function(e){if(e.target===modal)close()});
  modal.addEventListener('keydown',function(e){if(e.key==='Escape')close()});
  form.addEventListener('submit',function(e){e.preventDefault();
    var btn=form.querySelector('button[type=submit]');btn.disabled=true;btn.textContent='Sending…';err.style.display='none';
    var d={};new FormData(form).forEach(function(v,k){d[k]=v});
    d._subject='Waitlist: '+(d.course||'Agile Brands')+' · '+d.name;d._template='table';
    fetch('https://formsubmit.co/ajax/learning@agilebrands.in',{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(d)})
      .then(function(r){if(!r.ok)throw 0;return r.json()})
      .then(function(){dlg.classList.add('done');modal.querySelector('.ok button').focus()})
      .catch(function(){err.style.display='block'})
      .finally(function(){btn.disabled=false;btn.textContent='Join the waitlist'});
  });
})();
