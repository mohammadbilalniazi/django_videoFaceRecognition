console.log("hello")

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
reloadBtn.addEventListener("click", e => {
    window.location.reload();
})

if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
        video.srcObject = stream;
        // video.height
        // console.log("stream.getTracks()", stream.getTracks()[0].getSettings())
        const { height, width } = stream.getTracks()[0].getSettings();
        console.log("strea.getVideoTracks() ", stream.getVideoTracks())
        captureBtn.addEventListener("click", e => {
            captureBtn.classList.add('not-visible');
            const track = stream.getVideoTracks()[0];
            const imageCapture = new ImageCapture(track);
            console.log("new ImageCapture(track)=", imageCapture)
            imageCapture.takePhoto().then(blob => {
                console.log("image_capture.takePhoto blob ", blob);
                const img = new Image(parseInt(width / 3), parseInt(height / 3));
                img.src = URL.createObjectURL(blob);
                image_div.innerHTML = "";
                image_div.append(img);
                // video.classList.add('not-visible');
                const reader = new FileReader();
                reader.readAsDataURL(blob);
                reader.onloadend = () => {
                    const base64data = reader.result;
                    console.log("base64 ", base64data);
                    const formData = new FormData();
                    formData.append("csrfmiddlewaretoken", csrftoken);
                    formData.append("photo", base64data);
                    fetch('/classify/', { method: "POST", body: formData }).then((response) => response.json()).then((data) => {
                        message.innerHTML = "";
                        message.className = "";

                        if (data.ok) {
                            console.log("data ", data)
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
                            console.log("false")
                            message.classList.add('alert', 'alert-danger');
                            message.innerHTML = data.message;
                        }
                    })
                }
            })
        })
    })
}