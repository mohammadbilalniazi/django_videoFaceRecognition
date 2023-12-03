function ihsaya_majmoa_hawala(mudeeriath="all",start_date="all",end_date="all",controller_status="all",nawa_sanad="all")
{
    //console.log("called ihsaya_majmoa_hawala")
    mudeeriaths=document.getElementById("mudeeriath").value;
    start_date=document.getElementById("start_date_input").value;
    //console.log("start_date=",start_date);
    end_date=document.getElementById("end_date_input").value;
    nawa_sanad=document.getElementById("nawa_sanad").value;
    //console.log(mudeeriaths)
    if(mudeeriaths=="all"){
        url="/api/hawala/ihsaya/"+mudeeriaths+"/"+change_date(start_date)+"/"+change_date(end_date)+"/"+controller_status+"/"+nawa_sanad+"/";
    }
    else{
        url="/api/hawala/ihsaya/"+mudeeriaths+"/"+change_date(start_date)+"/"+change_date(end_date)+"/"+controller_status+"/"+nawa_sanad+"/";
    }
    fetch(url,{
        method:"GET",
        header:{"X-Requested-With":"XMLHttpRequest",}
    }).then(response=>response.json()).then(data=>{

        data=JSON.parse(data)
        // console.log("data=",data)
        class Mudeeriaths_Hawala_Ihsaya
        {
            constructor(mudeeriath,majmoa_hawala,majmoa_hawala_detail,majmoa_mustharadi_controller,majmoa_visa_controller,majmoa_mustharadi_thadyath,majmoa_thamam_mustharadi_hai_thadyath,majmoa_check_thadyath,majmoa_pending_hawala,majmoa_pool_visa_shoda_af,majmoa_pool_visa_shoda_yuru,majmoa_pool_visa_shoda_dollar,awayd_amount,majmoa_sarfajoi) {
            this.mudeeriath=mudeeriath;
            this.majmoa_hawala=majmoa_hawala;
            this.majmoa_hawala_detail=majmoa_hawala_detail
            this.majmoa_mustharadi_thadyath = majmoa_mustharadi_thadyath;
            this.majmoa_thamam_mustharadi_hai_thadyath=majmoa_thamam_mustharadi_hai_thadyath
            this.majmoa_check_thadyath=majmoa_check_thadyath;
            this.majmoa_pending_hawala=majmoa_pending_hawala;
            this.majmoa_mustharadi_controller=majmoa_mustharadi_controller;
            this.majmoa_pool_visa_shoda_af=majmoa_pool_visa_shoda_af;
            this.majmoa_visa_controller=majmoa_visa_controller;
            this.majmoa_pool_visa_shoda_yuru=majmoa_pool_visa_shoda_yuru;
            this.majmoa_pool_visa_shoda_dollar=majmoa_pool_visa_shoda_dollar;
            this.awayd_amount=awayd_amount;
            this.majmoa_sarfajoi=majmoa_sarfajoi;
            }

            addHtml() {
                let html = `<td>${this.mudeeriath}</td> <td>${this.majmoa_hawala}</td> <td>${this.majmoa_hawala_detail}</td><td>${this.majmoa_mustharadi_controller}</td> 
                <td>${this.majmoa_visa_controller}</td><td>${this.majmoa_mustharadi_thadyath}</td>
                <td>${this.majmoa_check_thadyath}</td><td>${this.majmoa_pending_hawala} </td><td>${this.majmoa_sarfajoi}</td>
                    <td>${this.majmoa_pool_visa_shoda_af}   dollar ${this.majmoa_pool_visa_shoda_dollar}</td>
                <td>${this.majmoa_pool_visa_shoda_yuru}</td><td>${this.awayd_amount}</td>`;    //beforeend                 
                    //mudeeriaths_ihasayaContainer.insertAdjacentHTML('beforeend', html);
            }
        }
        
        let mudeeriaths_list = [];
        //console.log("length ",Object.keys(data).length)
        
        mudeeriaths_list.push(new Mudeeriaths_Hawala_Ihsaya(data['mudeeriath'],data['majmoa_hawala'],data['majmoa_hawala_detail'],data['majmoa_mustharadi_controller'],data['majmoa_visa_controller'],data['majmoa_mustharadi_thadyath'],data['majmoa_thamam_mustharadi_hai_thadyath'],data['majmoa_check_thadyath'],data['majmoa_pending_hawala'],data['majmoa_pool_visa_shoda_af'],data['majmoa_pool_visa_shoda_yuru'],data['majmoa_pool_visa_shoda_dollar'],data['awayd_amount'],data['majmoa_sarfajoi']))
        
        mudeeriaths_list.forEach(mudeeriath=>mudeeriath.addHtml());
            
        //##########################graph################################
        var yValues=[data.majmoa_mustharadi_controller,data.majmoa_visa_controller]                                      
        var xValues = ["musthardi_controll","check_controll"];
        
        var barColors = ["red", "lightgreen"];    
        new Chart("controller_chart", {
        type: "pie",
        data: {
            labels: xValues,
            datasets: [{
            backgroundColor: barColors,
            data: yValues
            }]
        },
        options: {
            legend: {display: false},
            responsive: true,
            maintainAspectRatio: false,
            title: {
            display: true,
            text: "کنترولر "
            }
        }

        })

        
        var xValues = ["pool_visa_yuru", "pool_visa_af","pool_visa_dollar"];
        //var yValues = [55, 49, 44, 24, 15];
        var yValues=[data.majmoa_pool_visa_shoda_yuru,data.majmoa_pool_visa_shoda_af,data.majmoa_pool_visa_shoda_dollar]
        
        var barColors = ["red", "lightgreen","blue"];    
        new Chart("money_chart", {
        type: "bar",
        data: {
            labels: xValues,
            datasets: [{
            backgroundColor: barColors,
            data: yValues
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            legend: {
                position: 'top',
                labels: {
                    font: {
                        size: 20,
                    }
                }
            },
            title: {
            display: true,
            text: " پول",
            font: {
                    size: 25
                }
            },

            scales: {
                xAxes: [{
                        ticks: {
                        fontSize: 20
                        }
                        }],
                yXes:[{
                    ticks:{
                    fontSize:20
                    }
                }],

                x: {
                    ticks: {
                        font: {
                            size: 20,
                        }
                    }
                }
                
                }

        }
        });

        var xValues3 = [ "awayd_amount","majmoa_sarfajoi"];
        //var yValues = [55, 49, 44, 24, 15];
        var yValues3=[data.awayd_amount,data.majmoa_sarfajoi]

        var barColors3 = ["lightblue","lightgreen"];    
        new Chart("awayd_sarfajoi_chart", {
        type: "bar",
        data: {
            labels: xValues3,
            datasets: [{
            backgroundColor: barColors3,
            data: yValues3
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            legend: {
                position: 'top',
                labels: {
                    font: {
                        size: 20,
                    }
                }
            },
            title: {
            display: true,
            text: "عواید | صرفه جوی",
            font: {
                    size: 25
                }
            },

            scales: {
                xAxes: [{
                        ticks: {
                        fontSize: 20
                        }
                        }],
                yXes:[{
                    ticks:{
                    fontSize:20
                    }
                }],

                x: {
                    ticks: {
                        font: {
                            size: 20,
                        }
                    }
                }
                
                }

        }
        });

                var yValues2=[data.majmoa_mustharadi_thadyath,data.majmoa_check_thadyath,data.majmoa_pending_hawala]                                      
                var xValues2 = ["musthardi_thadyath", "check_thadyath", "pending_thadyath"];
                var barColors2 = ["red", "lightgreen","lightyellow"];    
                new Chart("thadyath_chart", {
                type: "pie",
                data: {
                    labels: xValues2,
                    datasets: [{
                    backgroundColor: barColors2,
                    data: yValues2
                    }]
                },
                options: {
                    legend: {display: false},
                    responsive: true,
                    maintainAspectRatio: false,
                    title: {
                    display: true,
                    text: "تادیات"
                    }
                }

        })

    })
    return 
}