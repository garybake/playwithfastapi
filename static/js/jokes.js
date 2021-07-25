$(document).ready(function() {

    // On joke submit button process label list
    $("#jokeLabelForm" ).submit(function( event ) {
        event.preventDefault();
        var txtVals = $("#floatingTextarea2").val().split("\n");
        txtVals.forEach(processLabel);
    });

    // On download button create a csv file
    $("#downloadcsv" ).click(function() {
        event.preventDefault();
        download_table_as_csv('output_table')
    });
});

function processLabel(qryLabel) {
    /**
     * Query an joke and add result to the table
     *
     * @param {String} qryLabel - label to query
     * @return {void}
     */
    if (qryLabel != '') {
        var encodedQry = encodeURIComponent(qryLabel);
        var url = '/api/v1/jokes?joke_type='.concat(encodedQry);
        $.get(url, function( data ) {
            addJokeToTable(data[0])
        });
    }
}

function addJokeToTable(joke) {
    /**
     * Adds a single joke to the joke table
     *
     * @param {Obj} joke - joke object to add to table
     * @return {void}
     */
     console.log(joke);
    $("#output_table").find('tbody')
    .append($('<tr>')
        .append($('<td>').text(joke.id))
        .append($('<td>').text(joke.type))
        .append($('<td>').text(joke.setup))
        .append($('<td>').text(joke.punchline))
        .append($('<td>').text(joke.status))
    );
}


function download_table_as_csv(table_id, separator = ',') {
    /**
     * Generates a csv file of the joke table and downloads to the user
     *
     * @param {String} table_id - HTML id of the table
     * @param {String} separator - Character to use to separate items in the csv
     * @return {void}
     */

    var rows = document.querySelectorAll('table#' + table_id + ' tr');
    // Construct csv
    var csv = [];
    for (var i = 0; i < rows.length; i++) {
        var row = [], cols = rows[i].querySelectorAll('td, th');
        for (var j = 0; j < cols.length; j++) {
            // Clean innertext to remove multiple spaces and jumpline (break csv)
            var data = cols[j].innerText.replace(/(\r\n|\n|\r)/gm, '').replace(/(\s\s)/gm, ' ')
            // Escape double-quote with double-double-quote (see https://stackoverflow.com/questions/17808511/properly-escape-a-double-quote-in-csv)
            data = data.replace(/"/g, '""');
            // Push escaped string
            row.push('"' + data + '"');
        }
        csv.push(row.join(separator));
    }

    if (csv.length < 2) {
        alert('Cannot export empty table')
        return;
    }

    var csv_string = csv.join('\n');
    // Download it
    var filename = 'export_' + table_id + '_' + new Date().toLocaleDateString() + '.csv';
    var link = document.createElement('a');
    link.style.display = 'none';
    link.setAttribute('target', '_blank');
    link.setAttribute('href', 'data:text/csv;charset=utf-8,' + encodeURIComponent(csv_string));
    link.setAttribute('download', filename);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}