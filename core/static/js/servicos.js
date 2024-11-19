function botao2(el) {
    var display = document.getElementById(el).style.display;
    if(display == "none"){
        document.getElementById(el).style.display = 'block';        
    }                    
    else{
        document.getElementById(el).style.display = 'none';
    }

    const botao2 = document.querySelector('.botao2');

    botao2.addEventListener('click', () => {
      const conteudo = document.getElementById('conteudo');
      const footer = document.querySelector('footer');
      botao2.parentNode.removeChild(botao2);
      footer.parentNode.insertBefore(botao2, footer);
      botao2.innerHTML = '<div class="pb">Ver menos</div>';
    });

}   