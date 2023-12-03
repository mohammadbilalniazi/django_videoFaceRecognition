function getCookie(name) {
    let cookieValue = "all";
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function make_keys()
{
            var ids = document.querySelectorAll('[id]');

            var arr = Array.prototype.map.call( ids, function( el, i ) {
                return el.id;
            });

            // console.log("arr=",arr)
            const csrftoken = getCookie('csrftoken');
            console.log("make_keys############")
            //const formData = new FormData();
            //console.log(report_date)
            //csrf=document.getElementsByName("csrfmiddlewaretoken").value;
            //console.log("user_id.length=",user_id.length)
        // postForm={}
            //postForm=[]
            list_form_data=[]//#################yazrzi format
            let k=0;
            for(let i=0; i<arr.length; i++){
            obj_dict_form={'key':arr[i],'language':'pashto'};
            list_form_data.push(obj_dict_form);
            k=i;
            }

            url="/insert_language_detail/";

            
        
        // end_date=change_date(end_date)
        // start_date=change_date(start_date) 
        // report_date=change_date(report_date[0].value)

        postForm={
            "language_insert":list_form_data
            }
            console.log("list_form_data=",JSON.stringify(postForm))
            axios({
                method:"POST",
                url:url,
                data:JSON.stringify(postForm),
                headers:{"content-type":"application/json","X-CSRFToken":getCookie('csrftoken')}
            }).then(function(response){
                console.log(response);
            })
 return ;                     

}



// import "https://unpkg.com/axios/dist/axios.min.js";

function change_language(language){
    console.log("language ",language);
}

function select_language(){

    url="/select_language/";
    // alert("select_language()")
    axios({method:"get",url:url}).then(function(response){
        console.log(JSON.parse(response.data['select_language']))
        data=JSON.parse(response.data['select_language'])
        for(index in data){
                // console.log("row ",JSON.parse(response.data['select_language'][key]));
                id=data[index][0]
                value=data[index][1]
                element=document.getElementById(id);
                if(element){
                    try{
                        element.textContent=value;
                        }
                        catch(err){
                            console.log(err)
                    }
                }
               
        }
    })

}


function list_saved_languages(){
    url="/list_saved_languages/";
    axios({
        method:"get",
        url:url
    }).then(function(response){
        data=JSON.parse(response.data['list_saved_languages'])
        console.log(data);
        
        for(index in data){
                // console.log("row ",JSON.parse(response.data['select_language'][key]));
                language=data[index][0]
                description=data[index][1]
                temp="<option>"+language+"</option>";
                console.log(temp)
        }

        // try{
        //     document.getElementById("language").innerHTML=options;
        //     }
        //     catch(err){
        //         console.log(err)
        //     }
    })
}


