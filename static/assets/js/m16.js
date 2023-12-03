
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


const csrftoken = getCookie('csrftoken');


// //const m16_form = document.querySelector("#m16_form");
// const search_form = document.getElementById("search_form");
// //console.log(m16_form)
// search_form.addEventListener("click", e => {
//     e.preventDefault();
//     alert("test");
//     msixteen = document.getElementById('msixteen').value;
//     orgniz = document.getElementById("orgniz").value;
//     fiscalyear = document.getElementById("fiscalyear").value;
//     location = document.getElementById("location").value;
//     budgettype = document.getElementById("budgettype").value;
//     // console.log("################msixteen=", msixteen)
//     alert(msixteen);

// })
// search_form.addEventListener("click", (e) => {
//     e.preventDefault()
//     console.log("test m16");
//     msixteen = document.getElementById('msixteen').value;
//     orgniz = document.getElementById("orgniz").value;
//     fiscalyear = document.getElementById("fiscalyear").value;
//     location = document.getElementById("location").value;
//     budgettype = document.getElementById("budgettype").value;
//     //console.log("################msixteen=",msixteen)
//     const formData = new FormData();
//     url = "m16/status/";
//     form = {
//         "msixteen": msixteen,
//         "orgniz": orgniz,
//         "fiscalyear": fiscalyear,
//         "location": location,
//         "budgettype": budgettype
//     }
//     console.log("form=", form)
//     //console.log(postForm)
//     fetch(url, {
//         method: 'POST',
//         body: JSON.stringify(form),
//         headers: {
//             'content-type': 'application/json',
//             'X-CSRFToken': getCookie('csrftoken')
//         },
//     })
//         .then(response => {
//             console.log("response.status=", response.status);
//             success = document.getElementById("success");
//             success.innerHTML = response.json();
//         })
//         .then(data => {
//             console.log("data=", data);
//         })
//         .catch((error) => {
//             console.log('Error:', error);
//         });
//     return false;
//     // }
// })


function controller_freebalance()
{
    url="/m16/controller_freebalance/";
    axios({
        method:"GET",
        url:url
    }).then(function(response){
        console.log(response);
    })
}


