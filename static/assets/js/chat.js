
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
    
    function send_message()
    {
        sender=document.getElementById("sender").value;
        message=document.getElementById("message").value;
        const csrftoken = getCookie('csrftoken');
        url="/admin/hawala/message/add/";
        message_obj={'message':message,'sender':sender};
        postForm={
            "message_obj":message_obj
            }
            console.log("postForm message=",JSON.stringify(postForm))
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
    

    message_submit_form=document.getElementById("message_submit_form");
    message_submit_form.addEventListener("submit",e=>{
        e.preventDefault();
        send_message();
        // alert("message_submit_form");
    })
