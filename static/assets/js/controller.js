

 function ihasaya_controllers(mudeeriath="all",start_date="all",end_date="all",controller_status="all",nawa_sanad="all"){     
    //
    //console.log(" called ihasaya_controllers ")
    mudeeriath_element=document.getElementById("mudeeriath");
    mudeeriath=mudeeriath_element.value;
    start_date=document.getElementById("start_date_input").value;
            //console.log("start_date=",start_date);
    end_date=document.getElementById("end_date_input").value;
    nawa_sanad=document.getElementById("nawa_sanad").value;

    url="/api/controller_ihsaya/"+mudeeriath+"/"+change_date(start_date)+"/"+change_date(end_date)+"/"+controller_status+"/"+nawa_sanad+"/";
    //console.log("mudeeriath_id ",mudeeriath," start_date ",start_date)
    console.log(url)
    
    fetch(url,{
        method:"GET",
        header:{"X-Requested-With":"XMLHttpRequest",}
    }).then(response=>response.json()).then(data=>{
        const mudeeriaths_ihasayaContainer = document.querySelector('#ihsaya_controllers');
        mudeeriaths_ihasayaContainer.innerHTML="";
        //fields=['controller','majmoa_hawala','majmoa_mustharadi_controller','majmoa_mustharadi_thadyath','majmoa_sarafa_joi','majmoa_pool_visa_shoda_af']
        class Controller_Ihsaya
        {
            constructor(id,first_name,mudeeriath,mudeeriath_name,majmoa_hawala,majmoa_mustharadi_controller,majmoa_mustharadi_thadyath,majmoa_thamam_mustharadi_hai_thadyath,majmoa_pending_hawala,majmoa_check_thadyath,majmoa_awayd,majmoa_sarafa_joi,majmoa_pool_visa_shoda_af,majmoa_haziri,majmoa_ghair_haziri) {
            this.id = id;
            this.first_name = first_name;
            this.mudeeriath=mudeeriath;
            
            this.mudeeriath_name=mudeeriath_name;
            this.majmoa_hawala=majmoa_hawala;
            this.majmoa_mustharadi_controller=majmoa_mustharadi_controller;
            this.majmoa_mustharadi_thadyath=majmoa_mustharadi_thadyath;
            this.majmoa_thamam_mustharadi_hai_thadyath=majmoa_thamam_mustharadi_hai_thadyath;
            this.majmoa_check_thadyath=majmoa_check_thadyath;
            this.majmoa_pending_hawala=majmoa_pending_hawala;
            this.majmoa_awayd=majmoa_awayd;
            this.majmoa_sarafa_joi=majmoa_sarafa_joi;
            this.majmoa_pool_visa_shoda_af=majmoa_pool_visa_shoda_af;
            this.majmoa_haziri=majmoa_haziri;
            this.majmoa_ghair_haziri=majmoa_ghair_haziri;
            }

            addHtml() {
                if (this.majmoa_pool_visa_shoda_af=="all"){
                    this.majmoa_pool_visa_shoda_af
                }
                let html=`<tr>
                                        <td scope="row">${this.first_name}</th>
                                        <td>${this.mudeeriath} ${this.mudeeriath_name}</td>
                                        <td>${this.majmoa_hawala} </td>
                                        <td> ${this.majmoa_mustharadi_controller} </td>
                                        <td>${this.majmoa_mustharadi_thadyath} ${this.majmoa_thamam_mustharadi_hai_thadyath}</td>
                                        
                                        <td>${this.majmoa_pending_hawala}</td>

                                        <td>${this.majmoa_check_thadyath}</td>

                                        <td>${this.majmoa_sarafa_joi} </td>
                                        <td>
                                            ${this.majmoa_pool_visa_shoda_af}
                                        </td>
                                        
                                        <td>${this.majmoa_awayd}</td>
                                        <td>${this.majmoa_haziri}</td>
                                        <td>${this.majmoa_ghair_haziri}</td>

                        </tr>`;  

                mudeeriaths_ihasayaContainer.insertAdjacentHTML('beforeend', html);
            }
        }
        //$("#mudeeriaths").val(`${mudeeriath}`).change();
        let Controller_Ihsaya_list = [];
        for(key in data){
            // console.log("data[key]['majmoa_mustharadi_controller']=",data[key]['majmoa_mustharadi_controller'])
            Controller_Ihsaya_list.push(new Controller_Ihsaya(data[key]['id'],
                                                              data[key]['first_name'],
                                                              data[key]['mudeeriath'],
                                                              data[key]['mudeeriath_name'],
                                                              data[key]['majmoa_hawala'],
                                                              data[key]['majmoa_mustharadi_controller'],
                                                              data[key]['majmoa_mustharadi_thadyath'],
                                                              data[key]['majmoa_thamam_mustharadi_hai_thadyath'],
                                                              data[key]['majmoa_pending_hawala'],
                                                              data[key]['majmoa_check_thadyath'],
                                                              data[key]['majmoa_awayd'],
                                                              data[key]['majmoa_sarafa_joi'],
                                                              data[key]['majmoa_pool_visa_shoda_af'],
                                                              data[key]['majmoa_haziri'],
                                                              data[key]['majmoa_ghair_haziri']))
        }
        Controller_Ihsaya_list.forEach(Controller_Ihsaya=>Controller_Ihsaya.addHtml())
    // setTimeout(() => {
        //    logged_users.forEach(user=>user.clearHtml())      
        //}, 1000)   
    });
    return
}

