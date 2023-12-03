
                function change_date(string_date)
                {
                    var momentDate=moment(string_date);
                    //return momentDate.calendar();
                    date=momentDate.format("YYYY-MM-DD");
                    if (moment(string_date, 'YYYY-MM-DD').isValid()) {
                    //console.log("valid ",string_date)
                        return date;
                    }
                    else {
                        //console.log("invalid ",string_date)
                        return string_date;
                    }
                }
                function controller_data(mudeeriath="all",start_date="all",end_date="all",controller_status="all",nawa_sanad="all")
                { 

                    mudeeriath_element=document.getElementById("mudeeriath");
                    mudeeriath=mudeeriath_element.value;     
                    
                    start_date=document.getElementById("id_date_controll").value;
                    end_date=document.getElementById("id_date_controll").value;
                    // end_date=document.getElementById("id_date_hawala").value;
                    // end_date=start_date;
                    // start_date=String.raw`${start_date.toString()}`;
                    
                    // end_date=String.raw`${start_date.toString()}`;
                    // mudeeriath=String.raw`${mudeeriath.toString()}`; 
                    // url="/api/controller_ihsaya/"+mudeeriath.toString()+"/"+start_date.toString()+"/"+end_date.toString()+"/"+controller_status+"/"+nawa_sanad+"/";
                    // let test="انکشافدهات";
                    // url=`/api/controller_ihsaya/${mudeeriath.toString()}/${start_date}/${end_date.toString()}/${controller_status}/${nawa_sanad}/`;
                    
                    // url=`/api/controller_ihsaya/${mudeeriath}/${start_date}/${end_date.toString()}/${controller_status}/${nawa_sanad}/`;
                    // console.log("start_date ",start_date," end_date ",end_date," ",url)
                    // url="/api/controller_ihsaya/"+mudeeriath+"/"+change_date(start_date)+"/"+change_date(end_date)+"/"+controller_status+"/"+nawa_sanad+"/";
                    url="/api/controller_ihsaya/"+mudeeriath+"/"+change_date(start_date)+"/"+change_date(end_date)+"/"+controller_status+"/"+nawa_sanad+"/";
                    
                    fetch(url,{
                        method:"GET",
                        header:{"X-Requested-With":"XMLHttpRequest",}
                    }).then(response=>response.json()).then(data=>{
                        const controller_container = document.querySelector('#controller');
                        controller_container.innerHTML="";
                        
                        //fields=['controller','majmoa_hawala','majmoa_mustharadi_controller','majmoa_mustharadi_thadyath','majmoa_sarafa_joi','majmoa_pool_visa_shoda_af
                        // console.log("*******************************")
                        // console.log("inside controller ihsaya ",data)
                        class Controller
                        {
                            constructor(id,first_name,email,mudeeriath,mudeeriath_name,majmoa_hawala,majmoa_mustharadi_controller,majmoa_mustharadi_thadyath,majmoa_pending_hawala,majmoa_check_thadyath,majmoa_awayd,majmoa_sarafa_joi,majmoa_pool_visa_shoda_af) {
                            this.id = id;
                            this.first_name = first_name;
                            this.email = email;
                            this.mudeeriath=mudeeriath;                            
                            this.mudeeriath_name=mudeeriath_name;
                            this.majmoa_hawala=majmoa_hawala;
                            this.majmoa_mustharadi_controller=majmoa_mustharadi_controller;
                            this.majmoa_mustharadi_thadyath=majmoa_mustharadi_thadyath;
                            this.majmoa_check_thadyath=majmoa_check_thadyath;
                            this.majmoa_pending_hawala=majmoa_pending_hawala;
                            this.majmoa_awayd=majmoa_awayd;
                            this.majmoa_sarafa_joi=majmoa_sarafa_joi;
                            this.majmoa_pool_visa_shoda_af=majmoa_pool_visa_shoda_af;
                            }

                            addHtml() {
                               const html=`<option value=${this.email}>${this.first_name}</option>`;

                                controller_container.insertAdjacentHTML('beforeend', html);
                            }
                        }
                        let Controller_Ihsaya_list = [];
                        for(key in data){
                            Controller_Ihsaya_list.push(new Controller(data[key]['id'],data[key]['first_name'],data[key]['email'],data[key]['mudeeriath'],data[key]['mudeeriath_name'],data[key]['majmoa_hawala'],data[key]['majmoa_mustharadi_controller'],data[key]['majmoa_mustharadi_thadyath'],data[key]['majmoa_pending_hawala'],data[key]['majmoa_check_thadyath'],data[key]['majmoa_awayd'],data[key]['majmoa_sarafa_joi'],data[key]['majmoa_pool_visa_shoda_af']))
                        }
                        Controller_Ihsaya_list.forEach(Controller=>Controller.addHtml())
                    });
                    return
                }