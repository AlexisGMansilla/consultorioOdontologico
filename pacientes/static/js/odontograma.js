let dienteSeleccionado = null;

// Obtener el pacienteId desde el atributo data del contenedor principal
const odontogramaContainer = document.querySelector(".odontograma-container");
const pacienteId = odontogramaContainer?.getAttribute("data-paciente-id");

if (!pacienteId) {
    console.error("No se pudo obtener el ID del paciente. Asegúrate de que el atributo data-paciente-id esté configurado.");
} else {
    console.log(`Paciente ID obtenido: ${pacienteId}`);
}

// Cargar el odontograma desde el servidor al cargar la página
document.addEventListener("DOMContentLoaded", () => {
    console.log("Intentando cargar el odontograma...");
    const url = `/pacientes/cargar-odontograma/${pacienteId}/`; // Usar el pacienteId obtenido
    fetch(url)
        .then((response) => {
            if (!response.ok) {
                throw new Error(`Error al cargar el odontograma desde el servidor. Código: ${response.status}`);
            }
            console.log("Odontograma cargado correctamente.");
            return response.json();
        })
        .then((estados) => {
            console.log("Estados recibidos del servidor:", estados);
            Object.keys(estados).forEach((dienteId) => {
                const diente = document.getElementById(`diente-${dienteId}`);
                if (diente) {
                    diente.dataset.estado = JSON.stringify(estados[dienteId]);

                    // Aplicar colores a las caras
                    const colorMap = {
                        Sano: "#2ecc71",
                        Caries: "#e74c3c",
                        Restaurado: "#f39c12",
                        Ausente: "#7f8c8d",
                    };
                    const estadosDiente = estados[dienteId];
                    diente.querySelector(".cara.arriba").style.backgroundColor = colorMap[estadosDiente.arriba];
                    diente.querySelector(".cara.derecha").style.backgroundColor = colorMap[estadosDiente.derecha];
                    diente.querySelector(".cara.izquierda").style.backgroundColor = colorMap[estadosDiente.izquierda];
                    diente.querySelector(".cara.abajo").style.backgroundColor = colorMap[estadosDiente.abajo];
                    diente.querySelector(".cara.central").style.backgroundColor = colorMap[estadosDiente.central];
                } else {
                    console.warn(`Diente con ID ${dienteId} no encontrado en el DOM.`);
                }
            });
        })
        .catch((error) => {
            console.error("Error al cargar el odontograma:", error);
        });
});

// Abrir el modal con datos del diente seleccionado
function abrirModal(dienteId) {
    const diente = document.getElementById(`diente-${dienteId}`);
    if (diente) {
        const estados = JSON.parse(diente.dataset.estado || "{}");

        // Asignar valores a los selectores
        document.getElementById("estado-arriba").value = estados.arriba || "Sano";
        document.getElementById("estado-derecha").value = estados.derecha || "Sano";
        document.getElementById("estado-izquierda").value = estados.izquierda || "Sano";
        document.getElementById("estado-abajo").value = estados.abajo || "Sano";
        document.getElementById("estado-central").value = estados.central || "Sano";

        // Mostrar el número del diente en el modal
        document.getElementById("diente-numero").innerText = `#${dienteId}`;

        // Mostrar el modal
        document.getElementById("modal-diente").style.display = "flex";
        dienteSeleccionado = dienteId;
    }
}


// Cerrar el modal
function cerrarModal() {
    console.log("Cerrando modal...");
    document.getElementById("modal-diente").style.display = "none";
    dienteSeleccionado = null; // Reiniciar el diente seleccionado
    console.log("Modal cerrado.");
}

function guardarCambios() {
    if (!dienteSeleccionado) {
        console.warn("No hay ningún diente seleccionado. No se puede guardar.");
        return;
    }

    // Recopilar los estados de las caras
    const estados = {
        arriba: document.getElementById("estado-arriba").value,
        derecha: document.getElementById("estado-derecha").value,
        izquierda: document.getElementById("estado-izquierda").value,
        abajo: document.getElementById("estado-abajo").value,
        central: document.getElementById("estado-central").value,
    };

    console.log(`Guardando cambios para el diente ${dienteSeleccionado}:`, estados);

    const url = `/pacientes/guardar-odontograma/${pacienteId}/`; // Asegúrate de que pacienteId esté definido
    const datos = { [dienteSeleccionado]: estados };

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify(datos),
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error(`Error al guardar en el servidor. Código: ${response.status}`);
            }
            console.log("Cambios guardados en el servidor con éxito.");
            return response.json();
        })
        .then((data) => {
            console.log(data.message);

            // Actualizar los colores en el frontend
            const diente = document.getElementById(`diente-${dienteSeleccionado}`);
            if (diente) {
                diente.dataset.estado = JSON.stringify(estados);

                const colorMap = {
                    Sano: "#2ecc71",
                    Caries: "#e74c3c",
                    Restaurado: "#f39c12",
                    Ausente: "#7f8c8d",
                };

                diente.querySelector(".cara.arriba").style.backgroundColor = colorMap[estados.arriba];
                diente.querySelector(".cara.derecha").style.backgroundColor = colorMap[estados.derecha];
                diente.querySelector(".cara.izquierda").style.backgroundColor = colorMap[estados.izquierda];
                diente.querySelector(".cara.abajo").style.backgroundColor = colorMap[estados.abajo];
                diente.querySelector(".cara.central").style.backgroundColor = colorMap[estados.central];
                console.log("Colores actualizados en el frontend.");
            }

            cerrarModal();
        })
        .catch((error) => {
            console.error("Error al guardar en el servidor:", error);
        });
}


// Obtener el CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Asignar eventos a botones del modal
document.getElementById("btn-guardar").addEventListener("click", guardarCambios);
document.getElementById("btn-cerrar").addEventListener("click", cerrarModal);
