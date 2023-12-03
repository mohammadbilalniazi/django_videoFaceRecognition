function thadyath_hawalas(mudeeriath_id="all",start_date="all",end_date="all",controller_status="all",hawala_no="all")
{
    mudeeriaths=document.getElementById("mudeeriath").value;
    ev_status=document.getElementById("ev_status").value;
    e_voucher=document.getElementById("e_voucher").value;
    start_date=document.getElementById("start_date_input").value;
    nawa_sanad=document.getElementById("nawa_sanad").value;
    console.log("e_voucher=",e_voucher);
    end_date=document.getElementById("end_date_input").value; 
        
    hawala_no=document.getElementById("hawala_no").value;
    if(hawala_no=="" || hawala_no==""){
        hawala_no="all"
    }
    if(e_voucher=="" || e_voucher==""){
        e_voucher="all"
    }
    url="/api/thadyaths/"+mudeeriaths+"/"+start_date+"/"+end_date+"/"+controller_status+"/"+ev_status+"/"+hawala_no+"/"+nawa_sanad+"/"+e_voucher;
    fetch(url,{
        method:"GET",
        header:{"X-Requested-With":"XMLHttpRequest"}
    }).then(response=>response.json()).then(data=>{ 
        const tbody_thafsil = document.querySelector('#tbody_thafsil');    
        tbody_thafsil.innerHTML="";
        // console.log("hawala data=",data);
        for(key in data)
        {
            for(thadyath_key in data[key]['thadyath_set'])
            {
                html2=`
                    <tr>
                    
                    <td>${data[key]['mudeeriath']} </td>
                    
                    <td>${data[key]['location']} </td>
                    
                    <td>${data[key]['nawyath_sanad']} </td>
                    
                    <td>${data[key]['year_hawala']} </td>
                    
                    <td>${data[key]['hawala_no']}</td>
                        <th scope="row">${data[key]['generated_code_controller']}</th>`;
                    


                    htmlnew2=`<td> ${data[key]['thadyath_set'][thadyath_key]['generated_code_thadyath']}</td>
                        <td> ${data[key]['thadyath_set'][thadyath_key]['e_voucher']}</td>
                        <td> ${data[key]['thadyath_set'][thadyath_key]['invoicenumber']}</td>
                        <td> ${data[key]['thadyath_set'][thadyath_key]['chequenumber']}</td>
                        <td>
                            <div class="progress" style="height: 5px;">`;
                if (data[key]['final_result']==0)
                offset=`<div class="progress-bar bg-danger" role="progressbar" style="width: 89%;" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>`;
                else if (data[key]['final_result']==1){
                offset=`<div class="progress-bar bg-success" role="progressbar" style="width: 25%;" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>`;
                } 
                else if (data[key]['final_result']==2){
                offset=`<div class="progress-bar bg-warning" role="progressbar" style="width: 64%;" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>`;
                }
                else if (data[key]['final_result']==3){
                    offset=`<div class="progress-bar bg-warning" role="progressbar" style="width: 64%;" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>`;
                }                    
                offset2=`     </div>
                        </td>
                    
                    `;

                offset3=` <td class="field-actions">`;
                offset6= ` <a href="/hawala/hawala/${data[key]['id']}"  class="btn btn-info"  role="button"> تفصیل </a> 
                </td> </tr>`;
                html2=html2+htmlnew2+offset+offset2+offset3+offset6;
                tbody_thafsil.insertAdjacentHTML('beforeend',html2);
            }
        }   
    });
    return ;
}
