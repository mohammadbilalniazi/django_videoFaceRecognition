
                    function mudeeriaths_hawalas(mudeeriath_id="all",start_date="all",end_date="all",controller_status="all",hawala_no="all",nawa_sanad="all")
                    {
                            mudeeriath_id=document.getElementById("mudeeriath").value;
                            //final_result=document.getElementById("final_result").value;
                            start_date=document.getElementById("start_date_input").value;
                            //console.log("mudeeriaths=",mudeeriaths);
                            end_date=document.getElementById("end_date_input").value; 
                            nawa_sanad=document.getElementById("nawa_sanad").value;
                            final_result="all";
                            url="/api/hawalas/"+mudeeriath_id+"/"+change_date(start_date)+"/"+change_date(end_date)+"/"+controller_status+"/"+final_result+"/"+hawala_no+"/"+nawa_sanad+"/";

                            fetch(url,{
                                method:"GET",
                                header:{"X-Requested-With":"XMLHttpRequest"}
                            }).then(response=>response.json()).then(data=>{ 
                                const hawalasContainer = document.querySelector('#hawalas');   
                                const thadyath_controll_report = document.querySelector('#thadyath_controll_report');
                                hawalasContainer.innerHTML="";
                                thadyath_controll_report.innerHTML="";
                                // console.log("###################hawalas#########");
                                console.log("thadyath_controll_report data=",data);
                                for(key in data){

                                    html2=`
                                            <tr>
                                                <th scope="row">${data[key]['mudeeriath']}</th>
                                                <td>${data[key]['hawala_detail_set'][0]['controller']} </td>
                                                <td> ${data[key]['hawala_detail_set'][0]['date_controll']}</td>
                                              
                                                <td> ${data[key]['hawala_detail_set'][0]['amount']}</td>
                                                <td>${data[key]['hawala_no']}</td>
                                                <td>${data[key]['nawa_sanad']} </td>
                                                <td>
                                                    <div class="progress" style="height:20px">`;
                                        if (data[key]['final_result']==0)
                                        offset=`<div class="progress-bar bg-danger"  role="progressbar" style="width: 89%;" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>`;
                                        else if (data[key]['final_result']==1){
                                        offset=`<div class="progress-bar bg-success"  role="progressbar" style="width: 89%;" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>`;
                                        } 
                                        else if (data[key]['final_result']==2){
                                        offset=`<div class="progress-bar bg-warning"  role="progressbar" style="width: 89%;" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>`;
                                        } 
                                        else if (data[key]['final_result']==3){
                                            offset=`<div class="progress-bar bg-error" role="progressbar" style="width: 89%;" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>`;
                                        }                
                                        
                                        
                                        offset2=`     </div>
                                                </td> <td><a href="/hawala/hawala/${data[key]['id']}" class="btn btn-info" role="button"> تفصیل </a></td>
                                            </tr>
                                            `;
                                        html2=html2+offset+offset2;
                                        //console.log("html2=",html2)
                                    hawalasContainer.insertAdjacentHTML('beforeend',html2);
                                }

                              //  console.log("########test data ",data)
                              var k=1;
                                for(key in data){
                                   for(ev_key in data[key]['thadyath_set'])
                                   {                                           
                                        html1=`
                                                <tr>
                                                    <th scope="row">${k}</th>
                                                    <td>${data[key]['generated_code_controller']} </td> <td>${data[key]['hawala_no']}</td><td>${data[key]['hawala_detail_set'][0]['date_hawala']}</td>`;
                                            if(data[key]['hawala_detail_set'].length>1)
                                            {                        
                                                var last_is_rejected=data[key]['hawala_detail_set'][1]['is_rejected'];
                                            }
                                            else{
                                                var last_is_rejected=data[key]['hawala_detail_set'][0]['is_rejected'];
                                            }
                                            // if(data[key]['hawala_detail_set'][0]['is_rejected']){
                                            if(last_is_rejected){
                                                offset1=`<td></td><td><span style='background-color:red' id='mustharadi_controll_label'>مسترد کنترول ${data[key]['hawala_detail_set'][0]['is_rejected']} ${data[key]['hawala_detail_set'].length}</span></td>`;
                                            }
                                            else{
                                                offset1=`<td><span style='background-color:green' id='visa_controll_label'>ویزه کنترول  </span></td><td> </td>`;
                                            }

                                            if(data[key]['thadyath_set'].length>0){
                                           // console.log("data[key]['thadyath_set'].length=",data[key]['thadyath_set'].length)
                                          //  console.log("data[key]['thadyath_set']=",data[key]['thadyath_set'])
                                            offset2=`<td>${data[key]['thadyath_set'][ev_key]['invoicenumber']} </td><td>  ${data[key]['thadyath_set'][ev_key]['approveddate']}</td><td>   ${data[key]['thadyath_set'][ev_key]['chequedate']}</td>`;
                                                
                                            }
                                            else{
                                                offset2=`<td>  No invoicenumber </td><td>  No approval date</td><td>no check date</td>`;
                                            }
                                            
                                            //offset2=`<td>${data[key]['hawala_detail_set'][0]['final_result']} </td>`;

                                            offset3= `<td><div class="progress" style="height:20px">`;
                                                            
                                            if (data[key]['final_result']==0){
                                            offset4=`<div class="progress-bar bg-danger"  role="progressbar" style="width: 89%;" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>`;
                                            }
                                            else if (data[key]['final_result']==1){
                                            offset4=`<div class="progress-bar bg-success" role="progressbar" style="width: 89%;" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>`;
                                            } 
                                            else if (data[key]['final_result']==2){
                                            offset4=`<div class="progress-bar bg-warning" role="progressbar" style="width: 89%;" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>`;
                                            }  
                                            else if (data[key]['final_result']==3){
                                                offset4=`<div class="progress-bar bg-error" role="progressbar" style="width: 89%;" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>`;
                                            }                
                                            
                                            
                                            offset5=`     </div>
                                                    </td>

                                                    <td><a href="/hawala/hawala/${data[key]['id']}" class="btn btn-info" role="button"> تفصیل </a></td>
                                                </tr>
                                                `;
                                            html2=html1+offset1+offset2+offset3+offset4+offset5
                                            //console.log("html2=",html2)
                                            thadyath_controll_report.insertAdjacentHTML('beforeend',html2);
                                        k=k+1;
                                    }
                                }
                              
                            });
                    //})
                    return 
                }