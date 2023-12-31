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
const video = document.getElementById("video-element");
const image_div = document.getElementById("img_div");
const captureBtn = document.getElementById("capture-btn");
const reloadBtn = document.getElementById("reload-btn");

const message = document.getElementById("message");

if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
        console.log("stream ", stream);
        video.srcObject = stream;
        const { width, height } = stream.getTracks();
        captureBtn.addEventListener("click", e => {
            const track = stream.getVideoTracks()[0];
            const imageCapture = new ImageCapture(track);

            imageCapture.takePhoto().then((blob) => {
                const img = new Image(parseInt(width / 2), parseInt(height / 2));
                img.src = URL.createObjectURL(blob);
                image_div.innerHTML = "";
                image_div.appendChild(img);

                const reader = new FileReader();
                reader.readAsDataURL(blob);
                reader.onloadend = () => {
                    const base64data = reader.result;
                    const formData = new FormData();
                    formData.append("csrfmiddlewaretoken", csrftoken)
                    formData.append("photo", base64data);
                    axios({
                        method: "POST",
                        url: "/classify/",
                        data: formData,
                    }).then((response) => {
                        console.log('response ', response);
                        message.innerHTML = "";
                        message.className = "";
                        let data = response.data;
                        if (data.ok) {
                            message.classList.add('alert', 'alert-success');
                            let message_data = `<table>
                            <tbody>
                            <tr><th>${data.message}</th></tr>
                            <tr><th>Name</th><td>${data.data.username}</td></tr>
                            <tr><th>User Id</th><td>${data.data.id}</td></tr>
                            </tbody>
                            </table>`;
                            message.insertAdjacentHTML('beforeend', message_data);
                        } else {
                            message.classList.add('alert', 'alert-danger');
                            message.innerHTML = data.message;
                        }
                        setTimeout(() => {
                            message.innerHTML = "";
                            message.className = "";
                        }, 2000);
                    });
                }
            })

        })

    })
}