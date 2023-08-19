function setLoading(loading) {
    const btn = document.querySelector('button');
    if (loading) {
        btn.textContent = "Gerando...";
        btn.disabled = true;
    } else {
        btn.textContent = "Gerar Script";
        btn.disabled = false;
    }
}

function generateScript() {
    setLoading(true);
    const platform = document.getElementById('platform').value;
    const pixel_id = document.getElementById('pixel_id').value;
    const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
    const events = Array.from(checkboxes).map(checkbox => checkbox.value);
    const resultDiv = document.getElementById('result');

    // Limpar os scripts gerados anteriormente
    resultDiv.textContent = "";

    let completedRequests = 0;

    events.forEach(event => {
        $.ajax({
            url: "/generate_script",
            method: "POST",
            contentType: "application/json;charset=UTF-8",
            data: JSON.stringify({platform, pixel_id, event}),
            success: function (data) {
                resultDiv.textContent += data.script + "\n\n";
                completedRequests++;

                if (completedRequests === events.length) {
                    setLoading(false);
                }
            },
            error: function (xhr, status, error) {
                console.error("Erro ao gerar script:", error);
                alert("Ocorreu um erro ao gerar o script. Por favor, tente novamente.");
                setLoading(false);
            }
        });
    });
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf-token]').attr('content'))
        }
    }
});
