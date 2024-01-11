function controllers_haziri() {

    mudeeriaths = document.getElementById("mudeeriath");
    start_date_input = document.getElementById("start_date_input");
    // end_date_input = document.getElementById("end_date_input");

    mudeeriath_id = mudeeriaths.value;
    start_date_input = start_date_input.value;
    // end_date_input = end_date_input.value;
    console.log("mudeeriaths.value=", mudeeriath_id);

    url = "/haziri/controller/haziri/" + mudeeriath_id + "/" + change_date(start_date_input) + "/";
    fetch(url, {
            method: "GET",
            header: { "X-Requested-With": "XMLHttpRequest" },
        })
        .then((response) => response.json())
        .then((data) => {
            const monthly_haziri =
                document.querySelector("#monthly_haziri");
            // console.log("data=",data);
            monthly_haziri.innerHTML = "";
            // console.log(data)
            class ControllerHaziri {
                constructor(
                    no,
                    basth,
                    first_name,
                    father_name,
                    mudeeriath_name,
                    id,
                    is_haziri_uploaded,
                    kaifyath_haziri,
                    mudeeriath,
                    report_date,
                    user,
                    user_name,
                    wazeefa,
                    month,
                    total_present,
                    total_absent,
                    total_leave,
                    total_tafrihi, total_zaroori, total_marizi, total_waladi, total_hajj
                ) {
                    this.no = no;
                    this.id = id;
                    this.first_name = first_name;
                    this.father_name = father_name;
                    this.mudeeriath_name = mudeeriath_name;
                    this.user = user;
                    this.user_name = user_name;
                    this.mudeeriath = mudeeriath;
                    this.wazeefa = wazeefa;
                    this.basth = basth;
                    this.report_date = report_date;
                    this.is_haziri_uploaded = is_haziri_uploaded;
                    this.kaifyath_haziri = kaifyath_haziri;
                    this.month = month;
                    this.total_leave = total_leave;
                    this.total_absent = total_absent;
                    this.total_present = total_present;
                    this.total_tafrihi = total_tafrihi;
                    this.total_zaroori = total_zaroori;
                    this.total_marizi = total_marizi;
                    this.total_waladi = total_waladi;
                    this.total_hajj = total_hajj;
                }

                addHtml() {
                    let html1 = `<tr role="row" class="even">
                      <th class="field-id">${this.no}</th>
                      <td class="field-first_name">${this.first_name}</td>                
                      <td class="field-first_name">${this.father_name}</td>    
                      <td class="field-basth">${this.basth}</td>
                      <td class="field-wazeefa">${this.wazeefa}</td>
                      <td class="field-first_name">${this.mudeeriath_name}</td>   
                          <td class="field-last_name"><input type="hidden" class="user" disabled style="font-weight:bolder" value="${this.user}" name="user"></td>
                          <td class="field-id_card"><input type="hidden"  name="mudeeriath" disabled style="font-weight:bolder" class="mudeeriath" value="${this.mudeeriath}"></td>
                          <td class="field-pdo"><input type="number" class="total_present" value="${this.total_present}" name="total_present"><input type="hidden"  class="month" value="${this.month}" name="month"></td>
                          <td class="field-pdo"><input type="number"  class="total_absent" value="${this.total_absent}" name="total_absent"></td>
                          <td class="field-pdo"><input type="number"  class="total_leave"  value="${this.total_leave}" name="total_leave"></td> 
                          <td class="field-pdo"><input type="number" class="total_tafrihi" value="${this.total_tafrihi}" name="total_tafrihi">
                          <td class="field-pdo"><input type="number"  class="total_zaroori" value="${this.total_zaroori}" name="total_zaroori"></td>
                          <td class="field-pdo"><input type="number"  class="total_marizi"  value="${this.total_marizi}" name="total_marizi"></td> 
                          <td class="field-pdo"><input type="number"  class="total_waladi"  value="${this.total_waladi}" name="total_waladi"></td> 
                          <td class="field-pdo"><input type="number"  class="total_hajj"  value="${this.total_hajj}" name="total_hajj"></td> 
                          <td><input type="text" name="kaifyath_haziri" class="kaifyath_haziri" style="font-weight:bolder"  value="${this.kaifyath_haziri}"></td>
                          <td><input type="hidden" name="report_date" class="report_date" disabled  value="${this.report_date}"></td>`;


                    if (this.is_haziri_uploaded == true) {
                        //   console.log("true");
                        // mudeeriaths.style.backgroundColor="#28a745";
                        var html2 = `<td> <span class="alert alert-success" style="padding:0.7rem 1.0rem;font-size:100%;background-color:rgb(130 227 130)">${this.is_haziri_uploaded}</span></td>`;
                    } else {
                        //   console.log("false");
                        // mudeeriaths.style.backgroundColor="#f24734";
                        var html2 = `<td  ><span class="alert alert-danger"  style="padding:0.7rem 1.0rem;font-size:100%">${this.is_haziri_uploaded}</span></td>`;
                    }

                    // mudeeriaths.style.color="white";
                    let html3 = `<td>status</td></tr>`;
                    monthly_haziri.insertAdjacentHTML(
                        "beforeend",
                        html1 + html2
                    );
                }
            }

            let mudeeriaths_list = [];
            for (key in data) {
                no = key + 1;
                mudeeriaths_list.push(
                    new ControllerHaziri(
                        key,
                        data[key]["basth"],
                        data[key]["first_name"],
                        data[key]["father_name"],

                        data[key]["mudeeriath_name"],
                        data[key]["id"],
                        data[key]["is_haziri_uploaded"],
                        data[key]["kaifyath_haziri"],
                        data[key]["mudeeriath_id"],
                        data[key]["report_date"],
                        data[key]["user"],
                        data[key]["user_name"],
                        data[key]["wazeefa"],
                        data[key]["month"],
                        data[key]["total_present"],
                        data[key]["total_absent"],
                        data[key]["total_leave"],
                        data[key]["total_tafrihi"],
                        data[key]["total_zaroori"],
                        data[key]["total_marizi"],
                        data[key]["total_waladi"],
                        data[key]["total_hajj"]
                    )
                );


                monthly_haziri_status = document.getElementById("monthly_haziri_status");
                haziri_status = document.getElementById("haziri_status");
                haziri_status.value = data[key]['haziri_status'];
                monthly_haziri_status.value = data[key]['monthly_haziri_status'];
            }
            mudeeriaths_list.forEach((mudeeriath) =>
                mudeeriath.addHtml()
            );
        });
    //})
    return;
}

mudeeriaths = document.getElementById("mudeeriath");
start_date_input = document.getElementById("start_date_input");
end_date_input = document.getElementById("end_date_input");

mudeeriaths.addEventListener("change", (e) => {
    controllers_haziri();
});