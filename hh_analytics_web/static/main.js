window.onload = function () {
    fetch("/api/v1/results").then(response => response.json()).then(data => {
        const statsSelect = document.getElementById("statsSelect");
        for (const result of data.files) {
            const optionText = document.createElement("option");
            optionText.value = result;
            optionText.text = new Date(parseInt(result) * 1000).toString();
            statsSelect.appendChild(optionText);
        }
    });

    fetch("/api/v1/last").then(response => response.json()).then(data => {
        const textSelect = document.getElementById("searchTextSelect");
        const techSelect = document.getElementById("techSelect");

        for (const vacancy of data.vacancies) {
            const optionText = document.createElement("option");
            optionText.value = vacancy;
            optionText.text = vacancy;
            textSelect.appendChild(optionText);
        }

        for (const technology of data.technologies) {
            const optionText = document.createElement("option");
            optionText.value = technology;
            optionText.text = technology;
            techSelect.appendChild(optionText);
        }
    });
}

let getVacanciesLoading = false;
function getVacancies() {
    const resultDiv = document.getElementById("results");
    const statsDiv = document.getElementById("stats");

    const statsSelectInput = document.getElementById("statsSelect");
    if (statsSelectInput.value !== "none") {
        fetch(`/api/v1/results/${statsSelectInput.value}`)
            .then(response => response.json())
            .then(data => {
                resultDiv.innerHTML = "";
                statsDiv.innerHTML = "";
                if (data.error) {
                    resultDiv.innerHTML = `<p style="color:red;">Error: ${data.error.message}</p>`;
                    return;
                }
                const statsData = document.createElement("div");
                statsData.innerHTML = `<br><br>Запрос: ${data.result.vacancy_title} (технология: ${data.result.stats.technology})<br>Проанализировано всего вакансий: ${data.result.stats.total_vacancies}<br>Из них связанных с вашей технологией: ${data.result.stats.tech_vacancies} (${data.result.stats.tech_percentage}%)`;
                statsDiv.appendChild(statsData);
                const vacancyDiv = document.createElement("div");
                vacancyDiv.className = "vacancy";
                vacancyDiv.innerHTML = `<h3>resultID = ${data.time.raw}</h3>`;
                resultDiv.appendChild(vacancyDiv);
                data.result.vacancies.forEach(vacancy => {
                    const vacancyDiv = document.createElement("div");
                    vacancyDiv.className = "vacancy";
                    vacancyDiv.innerHTML = `
                        <h3>${vacancy.name}</h3>
                        <p><strong>Company:</strong> ${vacancy.employer.name}</p>
                        <p><strong>Location:</strong> ${vacancy.area.name}</p>
                        <p><strong>Salary:</strong> ${vacancy.salary ? vacancy.salary.from + " - " + vacancy.salary.to + " " + vacancy.salary.currency : "Not specified"}</p>
                        <a href="${vacancy.alternate_url}" target="_blank">View Vacancy</a>
                        <hr>
                    `;
                    resultDiv.appendChild(vacancyDiv);
                });
            })
            .catch(error => {
                resultDiv.innerHTML = `<p style="color:red;">Error fetching vacancies: ${error}</p>`;
            });
        return;
    }

    const textInput = document.getElementById("searchText");
    const textSelectInput = document.getElementById("searchTextSelect");
    if (textSelectInput.value !== "none") textInput.value = "";
    const text = textInput.value || textSelectInput.value;

    if (!text || text == "none") {
        resultDiv.innerHTML = `<p style="color:red;">Нет поискового запроса</p>`;
        return;
    }

    const techInput = document.getElementById("techText");
    const techSelectInput = document.getElementById("techSelect");
    if (techSelectInput.value !== "none") techInput.value = "";
    const tech = techInput.value || techSelectInput.value;

    if (!tech || tech == "none") {
        resultDiv.innerHTML = `<p style="color:red;">Не указана технология</p>`;
        return;
    }

    const countInput = document.getElementById("count");
    const count = countInput.value;

    if (count < 1 || count > 100) {
        resultDiv.innerHTML = `<p style="color:red;">Количество не может превышать 100</p>`;
        return;
    }

    if (!getVacanciesLoading) {
        statsDiv.innerHTML = "";
        resultDiv.innerHTML = `<br>Загрузка...<br><br><img src="/loadingfish.gif" />`;
    }

    fetch(`/api/v1/vacancies?${new URLSearchParams({ text, tech, count })}`)
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = "";
            if (data.error) {
                resultDiv.innerHTML = `<p style="color:red;">Error: ${data.error.message}</p>`;
                return;
            }
            const statsData = document.createElement("div");
            statsData.innerHTML = `<br><br>Запрос: ${data.vacancy_title} (технология: ${data.stats.technology})<br>Проанализировано всего вакансий: ${data.stats.total_vacancies}<br>Из них связанных с вашей технологией: ${data.stats.tech_vacancies} (${data.stats.tech_percentage}%)`;
            statsDiv.appendChild(statsData);
            const vacancyDiv = document.createElement("div");
            vacancyDiv.className = "vacancy";
            vacancyDiv.innerHTML = `<h3>resultID = ${data.resultID}</h3>`;
            resultDiv.appendChild(vacancyDiv);
            data.vacancies.forEach(vacancy => {
                const vacancyDiv = document.createElement("div");
                vacancyDiv.className = "vacancy";
                vacancyDiv.innerHTML = `
                    <h3>${vacancy.name}</h3>
                    <p><strong>Company:</strong> ${vacancy.employer.name}</p>
                    <p><strong>Location:</strong> ${vacancy.area.name}</p>
                    <p><strong>Salary:</strong> ${vacancy.salary ? vacancy.salary.from + " - " + vacancy.salary.to + " " + vacancy.salary.currency : "Not specified"}</p>
                    <a href="${vacancy.alternate_url}" target="_blank">View Vacancy</a>
                    <hr>
                `;
                resultDiv.appendChild(vacancyDiv);
            });
        })
        .catch(error => {
            resultDiv.innerHTML = `<p style="color:red;">Error fetching vacancies: ${error}</p>`;
        });
}