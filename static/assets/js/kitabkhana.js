function kitabkhana_function(nawa_file = "all", shumara = "all", start_date = "all", end_date = "end_date") {
    start_date = document.getElementById("start_date_input").value;
    end_date = document.getElementById("end_date_input").value;
    kitabkhana = document.getElementById("kitabkhana");
    url = '/api/kitabkhana/' + nawa_file + '/' + shumara + '/' + start_date + '/' + end_date + '/';
    //console.log("#####kithabkhana#####",start_date,end_date," nawa_file=",nawa_file)
    fetch(url, {
        method: "GET",
    }).then(response => response.json()).then(data => {
        //console.log(data);
        //console.log("data['file]",data[0]['file']);
        rows = "";
        for (key in data) {
            row = ` 
                                <tr>
                                    <td><i class="far fa-file-pdf text-primary h2"></i></td>
                                    <td>
                                        <h6 class="mt-0">${data[key]['file']}</h6>
                                    </td>
                                    <td>
                                        <h6 class="mt-0">${data[key]['nawa_file']}</h6>
                                    </td>
                                    <td>
                                        <h6 class="mt-0">${data[key]['shumara']}</h6>
                                    </td>
                                    <td>
                                        <h6 class="mt-0">${data[key]['user']}</h6>
                                    </td>
                                    <td>
                                        <h6 class="mt-0">${data[key]['to_whome']}</h6>
                                    </td>
                                    <td>
                                        <h6 class="mt-0">${data[key]['description']}</h6>
                                    </td>
                                    <td>
                                        <h6 class="mt-0">${data[key]['date']}</h6>
                                    </td>
                                    <td>
                                        <a href="${data[key]['file']}" download class="btn btn-primary btn-sm">
                                            <i class="fas fa-download"></i>
                                        </a>
                                    </td>
                                </tr>`;
            rows = rows + row;
        }
        // console.log(rows);
        kitabkhana.innerHTML = rows;

    }).catch(e => {
        console.log(e);
    })
}