document.getElementById('toggle-sidebar').addEventListener('click', function() {
    var sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('collapsed-sidebar');
});


// hora-chile.js
function obtenerHoraChile() {
    fetch('https://worldtimeapi.org/api/timezone/America/Santiago')
        .then(response => response.json())
        .then(data => {
            const hora = new Date(data.datetime);
            document.getElementById('hora-chile').innerText = hora.toLocaleTimeString();
        })
        .catch(error => console.error(error));
}

// Llama a la función cada segundo (1000 milisegundos)
setInterval(obtenerHoraChile, 10);

// Llama a la función al cargar la página para mostrar la hora inmediatamente
obtenerHoraChile();

