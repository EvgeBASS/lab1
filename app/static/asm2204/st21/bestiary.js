const url = window.location.href;

function onEditNote(id, type) {
    const title = document.getElementById(`title${id}_${type}`)
    const description = document.getElementById(`description${id}_${type}`)
    const price = document.getElementById(`price${id}_${type}`)
    const submit = document.getElementById(`submit${id}_${type}`)

    if (title) {
        title.disabled = false;
    }

    if (description) {
        description.disabled = false;
    }

    if (price) {
        price.disabled = false;
    }

    if (submit) {
        submit.style.display = ""
        submit.disabled = false
    }
}

function onTypeChanged() {
    const select = document.getElementById('addFormType')
    const price = document.getElementById('addFormPriceField')

    if (select.value === 'NOTE') {
        price.style.display = "none"
    }

    if (select.value === 'CREATURE') {
        price.style.display = ""
    }
}

function addNote(e) {
    e.preventDefault()

    const form = document.getElementById("addForm")

    	let note = {
        id: form.elements[0].value,
        type: form.elements[1].value,
		title: form.elements[2].value,
		description: form.elements[3].value,
	};

    if (form.elements[1].value === "CREATURE") {
        note.price = form.elements[4].value.split('$')[0]
    }

    fetch(`${url}`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json;charset=utf-8'
		},
		body: JSON.stringify(note)
		})
        .then(response => response.json())
        .catch(
            (error) => alert(error.message)
        )
        .then(response => {
            document.documentElement.innerHTML = response.html

            alert(response.message)
        });
}

function editNote(e, id, type) {
    e.preventDefault()

    const form = document.getElementById(`${id}_${type}`)

	let note = {
        id: form.elements[0].value,
        type: form.elements[1].value,
		title: form.elements[2].value,
		description: form.elements[3].value,
	};

    if (form.elements[4]) {
        note.price = form.elements[4].value.split('$')[0]
    }

    fetch(`${url}?id=${id}`, {
		method: 'PUT',
		headers: {
			'Content-Type': 'application/json;charset=utf-8'
		},
		body: JSON.stringify(note)
		})
        .then(response => response.json())
        .catch(
            (error) => alert(error.message)
        )
        .then(response => {
            document.documentElement.innerHTML = response.html

            alert(response.message)
        });
}

function deleteNote(id, type) {
    fetch(`${url}?id=${id}&type=${type}`, {
		method: 'DELETE',
		})
        .then(response => response.json())
        .catch(
            (error) => alert(error.message)
        )
        .then(response => {
            document.documentElement.innerHTML = response.html

            alert(response.message)
        });
}

function loadFromFile() {
        fetch(`${url}load_from_file`, {
		method: 'GET',
		})
        .then(response => response.json())
        .catch(
            (error) => alert(error.message)
        )
        .then(response => {
            document.documentElement.innerHTML = response.html

            alert(response.message)
        });
}