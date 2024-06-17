

(function(win,doc){
    'use strict';

    // Verifica se o usuário realmente deseja apagar o registro
    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel'); // Pega todos os botões com a classe btnDel
        for(let i=0; i<btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){ // Adiciona um evento de clique em cada botão
                if(confirm('Deseja mesmo apagar este registro?')){ // Se o usuário clicar em OK, o registro é apagado
                    return true;
                }else{ // Se o usuário clicar em cancelar, o registro não é apagado
                    event.preventDefault();
                }
            });
        }
    }


    // Ajax do Form
    if(doc.querySelector('#form')){
        let form = doc.querySelector('#form');
        function sendForm(event){
            event.preventDefault();
            let data = new FormData(form);
            let ajax = new XMLHttpRequest();
            let token = doc.querySelectorAll('input')[0].value;
            ajax.open('POST', form.action);
            ajax.setRequestHeader('X-CSRF-TOKEN', token);
            ajax.onreadystatechange = function(){
                if(ajax.status === 200 && ajax.readyState === 4){
                    let result = doc.querySelector('#result');
                    result.innerHTML = 'Cadastrado com sucesso!';
                    result.classList.add('alert');
                    result.classList.add('alert-success');
                } 
            }
            ajax.send(data);
            form.reset();
        }
        form.addEventListener('submit', sendForm, false);

    }
})(window,document);