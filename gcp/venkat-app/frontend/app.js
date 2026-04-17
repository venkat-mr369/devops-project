const API_URL = "http://35.185.57.29:80"; // your VM public IP

function saveData() {
  const name = document.getElementById("name").value;
  const city = document.getElementById("city").value;

  fetch(`${API_URL}/add`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ name, city })
  }).then(() => loadData());
}

function loadData() {
  fetch(`${API_URL}/get`)
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById("result");
      list.innerHTML = "";
      data.forEach(row => {
        const li = document.createElement("li");
        li.innerText = `${row.name} - ${row.city}`;
        list.appendChild(li);
      });
    });
}

window.onload = loadData;