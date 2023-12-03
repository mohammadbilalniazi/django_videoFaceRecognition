function thafseel_function(value)
{
    //console.log("hawala_no=",value);
    controller_status="all";
    hawala_no=value;
    mudeeriath_id=document.getElementById("mudeeriath").value;
    final_result=document.getElementById("final_result").value;
    start_date=document.getElementById("start_date_input").value;
    //console.log("mudeeriaths=",mudeeriaths);
    end_date=document.getElementById("end_date_input").value; 
    nawa_sanad=document.getElementById("nawa_sanad").value;
    hawala_no2=document.getElementById("hawala_no").value;
    //console.log("hawala_no ",hawala_no2," hawala_no from thafseel ",value)
    if(mudeeriath_id=="all"){
        alert("Please Select Specific Mudeeriath");
        return ;
    }
    url="/api/hawalas/"+mudeeriath_id+"/"+start_date+"/"+end_date+"/"+controller_status+"/"+final_result+"/"+hawala_no+"/"+nawa_sanad+"/";
    //onsole.log("url thafseel_function=",url)    
    fetch(url,{
        method:"GET"
    }).then(response=>response.json()).then(
    data=>
    {
        console.log(data);
        result_list1=document.getElementById("result_list");
        show_thafseel=document.getElementById("show_thafseel")
        html1="";
        html2="";
        html3="";
        html4="";
        html5="";
        html6="";
        html7="";
        verf_ht1="";
        verf_ht2="";
        verf_ht3="";
        approval_ht1="";
        approval_ht2="";
        approval_ht3="";
        check_ht1="";
        temp_htmls="";

        thadyath_html="";
        result_list1.innerHTML="";
        result_list=document.createElement("table");
        // result_list.id="hawala_api_table"
        
        result_list1.appendChild(result_list)
        all_temp_htmls=""
        for(hawala_key in data)
        {   
            console.log("hawala_key=",hawala_key," data[hawala_key]=",data[hawala_key])

            for(detail_key in data[hawala_key]['hawala_detail_set'])
            {
                console.log("data[hawala_key]['hawala_detail_set'] ",data[hawala_key]['hawala_detail_set']," detail_key ",detail_key);
                temp_ev=''
                for(ev_key in data[hawala_key]['thadyath_set']){
                    
                    temp_ev_1=`<tr> <th colspan='6' style="font-size:20px;text-align:center">${data[hawala_key]['thadyath_set'][ev_key]['e_voucher']}</th><tr>`;
                    temp_ev=temp_ev+temp_ev_1;
                }

                    html1=`<tr> <th colspan='6' style="font-size:30px;text-align:center">Controller</th><tr>`;
                    html1=html1+temp_ev;
                    html2=`<tr><th>Id</th><th>date</th><th>Controller Code</th><th>M16#</th><th>Year</th><th>Period</th></tr>`;
                    html3=`<tr><td>${data[hawala_key]['id']}</td><td>${data[hawala_key]['hawala_detail_set'][detail_key]['date_hawala']}</td><td>${data[hawala_key]['generated_code_controller']}</td><td>${data[hawala_key]['hawala_no']}</td><td>${data[hawala_key]['year_hawala']}</td><td>${data[hawala_key]['year_hawala']}</td></tr>`;

                    html4=`<tr><th colspan='2'>Created By Controller</th><th colspan='2'>Ministry</th><th colspan='2'>Unit</th>`;
                    html5=`<tr><td colspan='2'>${data[hawala_key]['hawala_detail_set'][detail_key]['controller']}</td><td colspan='2'>${data[hawala_key]['mudeeriath']}</td><td colspan='2'>${data[hawala_key]['hawala_detail_set'][detail_key]['mudeeriath']}</td></tr>`;

                    html6=`<tr><th>Op/Dev</th><th colspan="2">Payment Type</th><th>Received By</th><th colspan="2">Received Date </th>`;
                    html7=`<tr><td>${data[hawala_key]['nawyath_sanad']}</td><td colspan="2"></td><td></td><td colspan="2"></td></tr>`;
                            
                    console.log("data[hawala_key]['thadyath_set'] ",data[hawala_key]['thadyath_set']) 
                    for(thadyath_key in data[hawala_key]['thadyath_set']) 
                    {        
                        thadyath_html=`<tr>
                             <th>invoicenumber</th><th>${data[hawala_key][thadyath_set][thadyath_key]['invoicenumber']}<th>
                            <th>creation_thadyath_set</th><th>${data[hawala_key][thadyath_set][thadyath_key]['creation_thadyath_set']}<th>
                            <th>ev_status</th><th>${data[hawala_key][thadyath_set][thadyath_key]['ev_status']}<th>
                            <th>approveddate</th><th>${data[hawala_key][thadyath_set][thadyath_key]['approveddate']}<th>
                            <th>chequedate</th><th>${data[hawala_key][thadyath_set][thadyath_key]['chequedate']}<th>    
                         </tr>`;   
                        
                            temp_htmls=html2+html3+html4+html5+html6+html7+thadyath_html;
                            all_temp_htmls=all_temp_htmls+temp_htmls
               
                    }//thadyath set
             
            }//hawaladetail
        }// key_data     
        result_list.appendChild(html1+all_temp_htmls);
    }/* response */).catch(e=>{
         // console.log(e)
    })     
}// function