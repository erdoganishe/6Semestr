function filterJSON(jsonData, value) {
    return jsonData.filter(({name}) => name === value);
}

var openFile = function(event) {
    var input = event.target;
   const filt = document.getElementById('filter-input').value
    var reader = new FileReader();
    reader.onload = function() {
        text = filterJSON(JSON.parse(reader.result.toString()), filt)
        var node = document.getElementById('output');
        node.innerText = JSON.stringify(text)
    };
    reader.readAsText(input.files[0]);
};