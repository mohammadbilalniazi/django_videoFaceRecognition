function mudeeriaths_hawalas(mudeeriath_id = "all", start_date = "all", end_date = "all", controller_status = "all", hawala_no = "all") {

    if (mudeeriath_id == "all") {
        url = "/api/hawalas/";
    }
    else {
        url = "/api/hawalas/" + mudeeriath_id + "/" + start_date + "/" + end_date + "/" + controller_status + "/" + hawala_no + "/"
    }

    fetch(url, {
        method: "GET",
        header: { "X-Requested-With": "XMLHttpRequest" }
    }).then(response => response.json()).then(data => {
        const hawalasContainer = document.querySelector('#hawalas');

        const thadyath_controll_report = document.querySelector('#thadyath_controll_report');
        hawalasContainer.innerHTML = "";
        thadyath_controll_report.innerHTML = "";
        //console.log("###################hawalas#########");
        console.log("##############hawalas data=",data);
        for (key in data) {
            html2 = `
                        <tr>
                            <th scope="row">${data[key]['mudeeriath']}</th>
                            <td>${data[key]['hawala_detail_set'][0]['controller']} </td>
                            <td> ${data[key]['hawala_detail_set'][0]['date_controll']}</td>
                          
                            <td> ${data[key]['hawala_detail_set'][0]['amount']}</td>
                            <td>${data[key]['hawala_no']}</td>
                            <td>${data[key]['nawa_sanad']} </td>
                            <td>
                                <div class="progress" style="height: 5px;">`;
            if (data[key]['final_result'] == 0)
                offset = `<div class="progress-bar bg-danger" role="progressbar" style="width: 89%;" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>`;
            else if (data[key]['final_result'] == 1) {
                offset = `<div class="progress-bar bg-success" role="progressbar" style="width: 25%;" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>`;
            }
            else if (data[key]['final_result'] == 2) {
                offset = `<div class="progress-bar bg-warning" role="progressbar" style="width: 64%;" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>`;
            }


            offset2 = `     </div>
                            </td>
                        </tr>
                        `;
            html2 = html2 + offset + offset2
            //console.log("html2=",html2)
            hawalasContainer.insertAdjacentHTML('beforeend', html2);
        }


        for (key in data) {
            html1 = `
                        <tr>
                            <th scope="row">${key}</th>
                            <td>${data[key]['generated_code_controller']} </td> <td>${data[key]['hawala_no']}</td><td>${data[key]['hawala_detail_set'][0]['date_hawala']}</td>`;
            if (data[key]['hawala_detail_set'][0]['is_rejected']) {
                offset1 = `<td></td><td>مسترد شده</td>`;
            }
            else {
                offset1 = `<td>ویزه شده</td><td> </td>`;
            }

            if (data[key]['thadyath_set'].length > 0) {
                if (data[key]['thadyath_set'][0]['check_thadyath_set'].length > 0) {
                    offset2 = `<td>veri_rejection ${data[key]['thadyath_set'][0]['verification_thadyath_set'][0]['is_rejected']} </td><td>approval rejection ${data[key]['hawala_detail_set'][0]['thadyath_set'][0]['approval_thadyath_set'][0]['is_rejected']} </td><td>check rejection ${data[key]['hawala_detail_set'][0]['thadyath_set'][0]['check_thadyath_set'][0]['is_rejected']}</td>`;
                }
                else if (data[key]['thadyath_set'][0]['approval_thadyath_set'].length > 0) {
                    offset2 = `<td>veri_rejection ${data[key]['thadyath_set'][0]['verification_thadyath_set'][0]['is_rejected']} </td><td>approval rejection${data[key]['hawala_detail_set'][0]['thadyath_set'][0]['approval_thadyath_set'][0]['is_rejected']} </td><td>check rejection No</td>`;
                }
                else {
                    offset2 = `<td>veri_rejection ${data[key]['thadyath_set'][0]['verification_thadyath_set'][0]['is_rejected']} </td><td>approval rejection No</td><td>check rejection No</td>`;
                }
            }
            else {
                offset2 = `<td>rejection No</td><td>rejection No </td><td>rejection No </td>`;
            }

            offset3 = `<td><div class="progress" style="height: 5px;">`;

            if (data[key]['final_result'] == 0) {
                offset4 = `<div class="progress-bar bg-danger" role="progressbar" style="width: 89%;" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>`;
            }
            else if (data[key]['final_result'] == 1) {
                offset4 = `<div class="progress-bar bg-success" role="progressbar" style="width: 25%;" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>`;
            }
            else if (data[key]['final_result'] == 2) {
                offset4 = `<div class="progress-bar bg-warning" role="progressbar" style="width: 64%;" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>`;
            }


            offset5 = `     </div>
                            </td>

                            <td>تفصیل</td>
                        </tr>
                        `;
            html2 = html1 + offset1 + offset2 + offset3 + offset4 + offset5
            //console.log("html2=",html2)
            thadyath_controll_report.insertAdjacentHTML('beforeend', html2);
        }
    });
    //})
    return
}





function mudeeriaths_list(mudeeriath_id = "all", start_date = "all", end_date = "all", controll_status = "all") {

    console.log("called mudeeriaths_ihasaya mudeeriath.value", mudeeriath_id)
    mudeeriath_element = document.getElementById("mudeeriaths");
    console.log("mudeeriath_element=", mudeeriath_element.value);
    mudeeriath_id = mudeeriath_element.value;
    if (mudeeriath_id == "all") {
        url = "/api/mudeeriaths";
    }
    else {
        url = "/api/mudeeriaths/" + mudeeriath_id + "/" + start_date + "/" + end_date + "/" + controll_status + "/";
    }
    //url="/api/mudeeriaths";
    fetch(url, {
        method: "GET",
        header: { "X-Requested-With": "XMLHttpRequest", }
    }).then(response => response.json()).then(data => {
        const mudeeriaths_for_ihasayaContainer = document.querySelector('#mudeeriaths');
        const ihsaya_mudeeriath_hawalajath = document.querySelector("#ihsaya_mudeeriath_hawalajath");
        if (mudeeriath_id == "all") {
            mudeeriaths_for_ihasayaContainer.innerHTML = '';
        }
        ihsaya_mudeeriath_hawalajath.innerHTML = "";
        // console.log(data)
        class Mudeeriaths {
            constructor(no, id, mudeeriath_name, mudeeriath_code, majmoa_hawala, majmoa_hawala_detail, majmoa_pending_hawala, majmoa_mustharadi_controller, majmoa_visa_controller, majmoa_mustharadi_thadyath, majmoa_check_thadyath, majmoa_sarafa_joi, majmoa_pool_visa_shoda_af, majmoa_pool_visa_shoda_yuru, majmoa_awayd) {
                this.no = no;
                this.id = id;
                this.mudeeriath_name = mudeeriath_name;
                this.mudeeriath_code = mudeeriath_code;
                this.majmoa_hawala = majmoa_hawala;
                this.majmoa_hawala_detail = majmoa_hawala_detail;
                this.majmoa_pending_hawala = majmoa_pending_hawala;
                this.majmoa_mustharadi_controller = majmoa_mustharadi_controller;
                this.majmoa_visa_controller = majmoa_visa_controller;
                this.majmoa_mustharadi_thadyath = majmoa_mustharadi_thadyath;
                this.majmoa_check_thadyath = majmoa_check_thadyath;
                this.majmoa_sarafa_joi = majmoa_sarafa_joi;
                this.majmoa_pool_visa_shoda_af = majmoa_pool_visa_shoda_af;
                this.majmoa_pool_visa_shoda_yuru = majmoa_pool_visa_shoda_yuru;
                this.majmoa_awayd = majmoa_awayd;
            }

            addHtml() {
                //userContainer.innerHTML=""
                if (mudeeriath_id == "all") {      // دفعه اولی که تمام مدیریت ها را ما میخواهیم لیست کنیم
                    let html = `<option value="${this.id}">${this.mudeeriath_name}</option>`;    //beforeend                 
                    mudeeriaths_for_ihasayaContainer.insertAdjacentHTML('beforeend', html);
                }
                //$("#mudeeriaths").val(`${mudeeriath_id}`).change();
                let html2 = `<tr>
                        <td>${this.id}</td><td>${this.mudeeriath_name}</td>
                        <td>${this.mudeeriath_code}</td><td>${this.majmoa_hawala}</td>
                        <td>${this.majmoa_hawala_detail}</td><td>${this.majmoa_pending_hawala}</td>
                        <td>${this.majmoa_mustharadi_controller}</td>
                        <td>${this.majmoa_mustharadi_thadyath}</td><td>${this.majmoa_check_thadyath}</td>
                        <td>${this.majmoa_sarafa_joi}</td><td>${this.majmoa_pool_visa_shoda_af}</td>
                        <td>${this.majmoa_pool_visa_shoda_yuru}</td><td>${this.majmoa_awayd}</td>
                        
                        </tr>`;
            }
        }
        let mudeeriaths_list = [];

        for (key in data) {
            mudeeriaths_list.push(new Mudeeriaths(key, data[key]['id'], data[key]['mudeeriath_name'], data[key]['mudeeriath_code'], data[key]['majmoa_hawala'], data[key]['majmoa_hawala_detail'], data[key]['majmoa_pending_hawala'], data[key]['majmoa_mustharadi_controller'], data[key]['majmoa_visa_controller'], data[key]['majmoa_mustharadi_thadyath'], data[key]['majmoa_check_thadyath'], data[key]['majmoa_sarafa_joi'], data[key]['majmoa_pool_visa_shoda_af'], data[key]['majmoa_pool_visa_shoda_yuru'], data[key]['majmoa_awayd']))
        }
        mudeeriaths_list.forEach(mudeeriath => mudeeriath.addHtml());
        //console.log("mudeeriath_element.value=",mudeeriath_element.value)
    });
    //})
    return
}
//mudeeriaths_list()




function mudeeriaths_ihasaya(mudeeriath_id = "all", start_date = "all", end_date = "all", controll_status = "all") {

    console.log("called mudeeriaths_ihasaya mudeeriath.value", mudeeriath_id)
    try{
        mudeeriath_element = document.getElementById("mudeeriath");
    }
    catch(e)
    {
        mudeeriath_element = document.getElementById("mudeeriaths");
    }
    mudeeriath_id = mudeeriath_element.value;
    console.log("mudeeriath_element=", mudeeriath_element.value);
    nawa_sanad=document.getElementById("nawa_sanad").value;
    url = "/api/mudeeriaths/" + mudeeriath_id + "/" + start_date + "/" + end_date + "/" + controll_status + "/"+nawa_sanad+"/";
   
    //url="/api/mudeeriaths";
    fetch(url, {
        method: "GET",
        header: { "X-Requested-With": "XMLHttpRequest", }
    }).then(response => response.json()).then(data => {
        const mudeeriaths_for_ihasayaContainer = document.querySelector('#mudeeriaths');
        const ihsaya_mudeeriath_hawalajath = document.querySelector("#ihsaya_mudeeriath_hawalajath");
        ihsaya_mudeeriath_hawalajath.innerHTML = "";
        // console.log(data)
        class Mudeeriaths {
            constructor(no, id, mudeeriath_name, mudeeriath_code, majmoa_hawala, majmoa_hawala_detail, majmoa_pending_hawala, majmoa_mustharadi_controller, majmoa_visa_controller, majmoa_mustharadi_thadyath, majmoa_check_thadyath, majmoa_sarafa_joi, majmoa_pool_visa_shoda_af, majmoa_pool_visa_shoda_yuru, majmoa_awayd) {
                this.no = no;
                this.id = id;
                this.mudeeriath_name = mudeeriath_name;
                this.mudeeriath_code = mudeeriath_code;
                this.majmoa_hawala = majmoa_hawala;
                this.majmoa_hawala_detail = majmoa_hawala_detail;
                this.majmoa_pending_hawala = majmoa_pending_hawala;
                this.majmoa_mustharadi_controller = majmoa_mustharadi_controller;
                this.majmoa_visa_controller = majmoa_visa_controller;
                this.majmoa_mustharadi_thadyath = majmoa_mustharadi_thadyath;
                this.majmoa_check_thadyath = majmoa_check_thadyath;
                this.majmoa_sarafa_joi = majmoa_sarafa_joi;
                this.majmoa_pool_visa_shoda_af = majmoa_pool_visa_shoda_af;
                this.majmoa_pool_visa_shoda_yuru = majmoa_pool_visa_shoda_yuru;
                this.majmoa_awayd = majmoa_awayd;
            }

            addHtml() {
                //userContainer.innerHTML=""
                if (mudeeriath_id == "all") {      // دفعه اولی که تمام مدیریت ها را ما میخواهیم لیست کنیم
                    let html = `<option value="${this.id}">${this.mudeeriath_name}</option>`;    //beforeend                 
                    // mudeeriaths_for_ihasayaContainer.insertAdjacentHTML('beforeend', html);
                }
                //$("#mudeeriaths").val(`${mudeeriath_id}`).change();
                let html2 = `<tr>
                        <td>${this.id}</td><td>${this.mudeeriath_name}</td>
                        <td>${this.mudeeriath_code}</td><td>${this.majmoa_hawala}</td>
                        <td>${this.majmoa_hawala_detail}</td><td>${this.majmoa_pending_hawala}</td>
                        <td>${this.majmoa_mustharadi_controller}</td><td>${this.majmoa_visa_controller}</td>
                        <td>${this.majmoa_mustharadi_thadyath}</td><td>${this.majmoa_check_thadyath}</td>
                        <td>${this.majmoa_sarafa_joi}</td><td>${this.majmoa_pool_visa_shoda_af}</td>
                        <td>${this.majmoa_pool_visa_shoda_yuru}</td><td>${this.majmoa_awayd}</td>
                        
                        </tr>`;
                ihsaya_mudeeriath_hawalajath.insertAdjacentHTML('beforeend', html2);

            }
        }
        let mudeeriaths_list = [];

        for (key in data) {
            mudeeriaths_list.push(new Mudeeriaths(key, data[key]['id'], data[key]['mudeeriath_name'], data[key]['mudeeriath_code'], data[key]['majmoa_hawala'], data[key]['majmoa_hawala_detail'], data[key]['majmoa_pending_hawala'], data[key]['majmoa_mustharadi_controller'], data[key]['majmoa_visa_controller'], data[key]['majmoa_mustharadi_thadyath'], data[key]['majmoa_check_thadyath'], data[key]['majmoa_sarafa_joi'], data[key]['majmoa_pool_visa_shoda_af'], data[key]['majmoa_pool_visa_shoda_yuru'], data[key]['majmoa_awayd']))
        }
        mudeeriaths_list.forEach(mudeeriath => mudeeriath.addHtml());
        //mudeeriath_id=document.getElementById("mudeeriaths");
        // console.log("test1 mudeeriath_id=", mudeeriath_id.value)
        $("#mudeeriaths").val(`${mudeeriath_element.value}`).change();
        //console.log("mudeeriath_element.value=",mudeeriath_element.value)
    });
    //})
    return
}






