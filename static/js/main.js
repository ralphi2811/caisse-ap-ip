document.addEventListener('DOMContentLoaded', () => {
    // Initialisation du terminal
    const serverTerm = new Terminal({
        cursorBlink: true,
        theme: {
            background: '#000000',
            foreground: '#ffffff'
        },
        fontSize: 14,
        rows: 30
    });

    serverTerm.open(document.getElementById('serverTerminal'));

    // Connexion WebSocket
    const socket = io();

    // Gestion des sorties du serveur
    socket.on('server_output', (data) => {
        serverTerm.writeln(data.data);
    });

    // Gestion du mode échec
    const failureMode = document.getElementById('failureMode');
    const failureTypeContainer = document.getElementById('failureTypeContainer');

    failureMode.addEventListener('change', (e) => {
        failureTypeContainer.style.display = e.target.checked ? 'block' : 'none';
    });

    // Soumission du formulaire serveur
    document.getElementById('serverForm').addEventListener('submit', (e) => {
        e.preventDefault();
        serverTerm.clear();

        const data = {
            port: parseInt(document.getElementById('serverPort').value),
            payment_type: document.getElementById('paymentType').value,
            duration: parseInt(document.getElementById('duration').value)
        };

        if (failureMode.checked) {
            data.failure = true;
            data.failure_type = document.getElementById('failureType').value;
        }

        socket.emit('start_server', data);
    });
});
