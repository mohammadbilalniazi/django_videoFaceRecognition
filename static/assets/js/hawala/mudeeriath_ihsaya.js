
function mudeeriaths_ihsaya(mudeeriath_id="all",start_date="all",end_date="all",controll_status="all",nawa_sanad="all")
{            
    mudeeriath_element=document.getElementById("mudeeriath");
    mudeeriath_id=mudeeriath_element.value;
    start_date=document.getElementById("start_date_input").value;
    //console.log("start_date=",start_date);
    end_date=document.getElementById("end_date_input").value;
    nawa_sanad=document.getElementById("nawa_sanad").value;

    url="/api/mudeeriaths/"+mudeeriath_id+"/"+change_date(start_date)+"/"+change_date(end_date)+"/"+controll_status+"/"+nawa_sanad+"/";

    fetch(url,{
        method:"GET",
        header:{"X-Requested-With":"XMLHttpRequest",}
    }).then(response=>response.json()).then(data=>{ 
        const ihsaya_mudeeriath_hawalajath=document.querySelector("#ihsaya_mudeeriath_hawalajath");
        //if (mudeeriath_id=="all"){ 
        //mudeeriaths_for_ihasayaContainer.innerHTML='';
        //}
        ihsaya_mudeeriath_hawalajath.innerHTML="";
        
        // console.log("data error=",data)
        class Mudeeriaths
        {
            constructor(no,id,mudeeriath_name,mudeeriath_code,majmoa_hawala,majmoa_hawala_detail,majmoa_pending_hawala,majmoa_mustharadi_controller,majmoa_visa_controller,majmoa_mustharadi_thadyath,majmoa_thamam_mustharadi_hai_thadyath,majmoa_check_thadyath,majmoa_sarafa_joi,majmoa_pool_visa_shoda_af,majmoa_pool_visa_shoda_yuru,majmoa_pool_visa_shoda_dollar,majmoa_awayd) {
            this.no = no;
            this.id=id;
            this.mudeeriath_name = mudeeriath_name;
            this.mudeeriath_code=mudeeriath_code;
            this.majmoa_hawala=majmoa_hawala;
            this.majmoa_hawala_detail=majmoa_hawala_detail;
            this.majmoa_pending_hawala=majmoa_pending_hawala;
            this.majmoa_mustharadi_controller=majmoa_mustharadi_controller;
            this.majmoa_visa_controller=majmoa_visa_controller;
            this.majmoa_mustharadi_thadyath=majmoa_mustharadi_thadyath;
            this.majmoa_thamam_mustharadi_hai_thadyath=majmoa_thamam_mustharadi_hai_thadyath;
            this.majmoa_check_thadyath=majmoa_check_thadyath;
            this.majmoa_sarafa_joi=majmoa_sarafa_joi;
            this.majmoa_pool_visa_shoda_af=majmoa_pool_visa_shoda_af;
            this.majmoa_pool_visa_shoda_yuru=majmoa_pool_visa_shoda_yuru;
            this.majmoa_pool_visa_shoda_dollar=majmoa_pool_visa_shoda_dollar;
            this.majmoa_pool_visa_shoda_dollar=majmoa_pool_visa_shoda_dollar;
            this.majmoa_awayd=majmoa_awayd;
            }

            addHtml() {
                //userContainer.innerHTML=""
                if (mudeeriath_id=="all"){      // دفعه اولی که تمام مدیریت ها را ما میخواهیم لیست کنیم
                let html = `<option value="${this.id}">${this.mudeeriath_name}</option>`;    //beforeend                 
                // mudeeriaths_for_ihasayaContainer.insertAdjacentHTML('beforeend', html);
                }
                //$("#mudeeriaths").val(`${mudeeriath_id}`).change();
                let html2=`<tr>
                    <td>${this.id}</td><td>${this.mudeeriath_name}</td>
                    <td>${this.majmoa_hawala}</td>
                    <td>${this.majmoa_pending_hawala}</td>
                    <td>${this.majmoa_mustharadi_controller}</td>
                    <td>${this.majmoa_mustharadi_thadyath} ${this.majmoa_thamam_mustharadi_hai_thadyath}</td><td>${this.majmoa_check_thadyath}</td>
                    <td>${this.majmoa_sarafa_joi}</td><td>${this.majmoa_pool_visa_shoda_af}</td>
                    <td>${this.majmoa_awayd}</td>
                    
                    </tr>`;
                    ihsaya_mudeeriath_hawalajath.insertAdjacentHTML('beforeend',html2);

            }
        }
        let mudeeriaths_list = [];
        // console.log("data=",data)
        for(key in data){                                                                                                                                                                                                        
            mudeeriaths_list.push(new Mudeeriaths(key,data[key]['id'],
                                                     data[key]['mudeeriath_name'],
                                                     data[key]['mudeeriath_code'],
                                                     data[key]['majmoa_hawala'],
                                                     data[key]['majmoa_hawala_detail'],
                                                     data[key]['majmoa_pending_hawala'],
                                                     data[key]['majmoa_mustharadi_controller'],
                                                     data[key]['majmoa_visa_controller'],
                                                     data[key]['majmoa_mustharadi_thadyath'],
                                                     data[key]['majmoa_thamam_mustharadi_hai_thadyath'],
                                                     data[key]['majmoa_check_thadyath'],
                                                     data[key]['majmoa_sarafa_joi'],
                                                     data[key]['majmoa_pool_visa_shoda_af'],
                                                     data[key]['majmoa_pool_visa_shoda_yuru'],
                                                     data[key]['majmoa_pool_visa_shoda_dollar'],
                                                     data[key]['majmoa_awayd']))
        }
        mudeeriaths_list.forEach(mudeeriath=>mudeeriath.addHtml());

        $("#mudeeriaths").val(`${mudeeriath_element.value}`).change();
    }); 
//})
return ;
}
