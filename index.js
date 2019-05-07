var volume = document.querySelector('.volume');
var xhr = new XMLHttpRequest();



volume.onchange = () => {
	xhr.open('GET', '/volume/'+volume.value, true);

	xhr.onreadystatechange = () => {
		if (xhr.readyState == 4){
			console.log(xhr.status);
		}
	}
	xhr.send();
}