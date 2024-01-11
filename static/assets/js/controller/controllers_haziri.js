function controllers_haziri() {
    mudeeriaths = document.getElementById("mudeeriath");
    start_date_input = document.getElementById("start_date_input");
    mudeeriath_id = mudeeriaths.value;
    start_date_input = start_date_input.value;
    console.log("mudeeriaths.value=", mudeeriath_id);

    url = "/haziri/controller/haziri/" + mudeeriath_id + "/" + change_date(start_date_input) + "/";
    fetch(url, {
            method: "GET",
            header: { "X-Requested-With": "XMLHttpRequest" },
        })
        .then((response) => response.json())
        .then((data) => {
            const monthly_haziri = document.querySelector("#monthly_haziri");
            monthly_haziri.innerHTML = "";
            for (key in data) {
                no = key + 1;
                let html1 = `<tr role="row" class="even">
                <th class="field-id">${no}</th>
                <td class="field-first_name">${data[key]["first_name"]}</td>                
                <td class="field-first_name">${data[key]["father_name"]}</td>    
                <td class="field-basth">${data[key]["basth"]}</td>
                <td class="field-wazeefa">${data[key]["wazeefa"]}</td>
                <td class="field-first_name">${data[key]["mudeeriath_name"]}</td>   
                    <td class="field-last_name"><input type="hidden" class="user" disabled style="font-weight:bolder" value="${data[key]["user"]}" name="user"></td>
                    <td class="field-id_card"><input type="hidden"  name="mudeeriath" disabled style="font-weight:bolder" class="mudeeriath" value="${data[key]["mudeeriath"]}"></td>
                    <td class="field-pdo"><input type="number" class="total_present" value="${data[key]["total_present"]}" name="total_present"><input type="hidden"  class="month" value="${data[key]["month"]}" name="month"></td>
                    <td class="field-pdo"><input type="number"  class="total_absent" value="${data[key]["total_absent"]}" name="total_absent"></td>
                    <td class="field-pdo"><input type="number"  class="total_leave"  value="${data[key]["total_leave"]}" name="total_leave"></td> 
                    <td class="field-pdo"><input type="number" class="total_tafrihi" value="${data[key]["total_tafrihi"]}" name="total_tafrihi">
                    <td class="field-pdo"><input type="number"  class="total_zaroori" value="${data[key]["total_zaroori"]}" name="total_zaroori"></td>
                    <td class="field-pdo"><input type="number"  class="total_marizi"  value="${data[key]["total_marizi"]}" name="total_marizi"></td> 
                    <td class="field-pdo"><input type="number"  class="total_waladi"  value="${data[key]["total_waladi"]}" name="total_waladi"></td> 
                    <td class="field-pdo"><input type="number"  class="total_hajj"  value="${data[key]["total_hajj"]}" name="total_hajj"></td> 
                    <td><input type="text" name="kaifyath_haziri" class="kaifyath_haziri" style="font-weight:bolder"  value="${data[key]["kaifyath_haziri"]}"></td>
                    <td><input type="hidden" name="report_date" class="report_date" disabled  value="${data[key]["report_date"]}"></td>`;


                if (data[key]["is_haziri_uploaded"] == true) {
                    var html2 = `<td> <span class="alert alert-success" style="padding:0.7rem 1.0rem;font-size:100%;background-color:rgb(130 227 130)">${data[key]["is_haziri_uploaded"]}</span></td>`;
                } else {
                    var html2 = `<td  ><span class="alert alert-danger"  style="padding:0.7rem 1.0rem;font-size:100%">${data[key]["is_haziri_uploaded"]}</span></td>`;
                }

                monthly_haziri.insertAdjacentHTML(
                    "beforeend",
                    html1 + html2
                );
                monthly_haziri_status = document.getElementById("monthly_haziri_status");
                haziri_status = document.getElementById("haziri_status");
                haziri_status.value = data[key]['haziri_status'];
                monthly_haziri_status.value = data[key]['monthly_haziri_status'];
            }
        });
    return;
}

mudeeriaths = document.getElementById("mudeeriath");
start_date_input = document.getElementById("start_date_input");
end_date_input = document.getElementById("end_date_input");

mudeeriaths.addEventListener("change", (e) => {
    controllers_haziri();
});