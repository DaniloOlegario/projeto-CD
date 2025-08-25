const API_URL = 'http://127.0.0.1:8000';
const truckGrid = document.getElementById('truck-grid');
const statusMessage = document.getElementById('status-message');
const loadingIndicator = document.getElementById('loading');
const lojaFilterInput = document.getElementById('loja-filter');
const filterCompleteButton = document.getElementById('filter-complete');
const filterIncompleteButton = document.getElementById('filter-incomplete');
const clearButton = document.getElementById('clear-button');
const refreshButton = document.getElementById('refresh-button');

// Variável para armazenar o status de filtro atual
let currentStatusFilter = null;

// Função para exibir mensagens com tempo limite (não alterada)
function showMessage(message, isError = false) {
    statusMessage.textContent = message;
    statusMessage.style.color = isError ? '#dc3545' : '#28a745';
    setTimeout(() => {
        statusMessage.textContent = '';
    }, 5000);
}

// Função para renderizar os caminhões na grade (não alterada)
function renderTrucks(trucks) {
    truckGrid.innerHTML = '';
    if (trucks.length === 0) {
        truckGrid.innerHTML = '<p>Nenhum caminhão encontrado.</p>';
        return;
    }
    const lojas = {};
    trucks.forEach(truck => {
        const loja = truck.loja || 'Sem Loja';
        if (!lojas[loja]) {
            lojas[loja] = [];
        }
        lojas[loja].push(truck);
    });

    for (const loja in lojas) {
        const lojaContainer = document.createElement('div');
        lojaContainer.classList.add('loja-container');
        lojaContainer.innerHTML = `<h2>${loja}</h2>
                                   <div class="loja-trucks-grid"></div>`;

        const lojaTrucksGrid = lojaContainer.querySelector('.loja-trucks-grid');
        lojas[loja].forEach(truck => {
            const truckCard = document.createElement('div');
            let statusClass = truck.status.replace(/\s/g, '');
            let emoji = '🚛';
            if (truck.porcentagem_carregamento >= 100) {
                emoji = '🚚';
            } else if (truck.porcentagem_carregamento > 0) {
                emoji = '🚚';
            }

            truckCard.classList.add('truck-card', statusClass);

            let statusDisplay = truck.status;
            if (truck.porcentagem_carregamento >= 100) {
                statusDisplay += ' ✅';
            }

            truckCard.innerHTML = `
                <div class="truck-emoji">${emoji}</div>
                <h3>${truck.placa}</h3>
                <p><strong>Status:</strong> ${statusDisplay}</p>
                <p><strong>Paletes:</strong> ${truck.paletes_carregados}/${truck.capacidade_maxima}</p>
                <div class="progress-bar-container">
                    <div class="progress-bar" style="width: ${truck.porcentagem_carregamento}%; background-color: ${truck.cor_status};"></div>
                </div>
                <p><strong>Progresso:</strong> ${truck.porcentagem_carregamento}%</p>
                <div class="cd-info">
                    <strong>Loja:</strong> ${truck.loja}
                </div>
            `;
            lojaTrucksGrid.appendChild(truckCard);
        });
        truckGrid.appendChild(lojaContainer);
    }
}

// Funções de comunicação com a API
async function fetchTrucks() {
    loadingIndicator.style.display = 'block';
    await new Promise(resolve => setTimeout(resolve, 2000));
    try {
        // Cria a URL de forma dinâmica
        const url = new URL(`${API_URL}/caminhoes/`);
        const loja = lojaFilterInput.value;

        if (loja) {
            url.searchParams.append('loja', loja);
        }
        if (currentStatusFilter) {
            // Adiciona o novo parâmetro 'status_filter' na URL
            url.searchParams.append('status_filter', currentStatusFilter);
        }

        const response = await fetch(url.toString());
        const data = await response.json();

        if (!response.ok) {
            renderTrucks([]);
        } else {
            renderTrucks(data);
        }
    } catch (error) {
        showMessage('Erro ao buscar caminhões da API. Verifique se o servidor está rodando.', true);
        renderTrucks([]);
    } finally {
        loadingIndicator.style.display = 'none';
    }
}

// Event Listeners para os botões de filtro e atualização
filterCompleteButton.addEventListener('click', () => {
    currentStatusFilter = 'completo'; // Define o filtro como 'completo'
    fetchTrucks(); // Chama a busca
});

filterIncompleteButton.addEventListener('click', () => {
    currentStatusFilter = 'incompleto'; // Define o filtro como 'incompleto'
    fetchTrucks(); // Chama a busca
});

clearButton.addEventListener('click', () => {
    lojaFilterInput.value = '';
    currentStatusFilter = null; // Limpa o filtro de status
    fetchTrucks();
});

refreshButton.addEventListener('click', () => {
    fetchTrucks();
});

// Inicializa a página
document.addEventListener('DOMContentLoaded', () => {
    fetchTrucks();
});