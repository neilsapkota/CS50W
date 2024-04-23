function like_post(post_id) {
    fetch(`/like/${post_id}`, {
        method: "POST"
    })
    .then(response => response.json())
    .then(result => {

        if (result.stat == "Success") {
            var icn = `
            <button class="like-btn" onclick="like_post('${post_id}');">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="red" class="bi bi-heart-fill" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/>
                </svg>
                <label class="bi-heart" id="like-no-${post_id}">${result.likes}</label>   
            </button>`
            
            if (result.action == "u") { 
                icn = `
                <button class="like-btn" onclick="like_post('${post_id}');">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="red" class="bi bi-heart" viewBox="0 0 16 16">
                        <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
                    </svg>
                    <label class="bi-heart" id="like-no-${post_id}">${result.likes}</label>   
                </button>`
             }


            document.getElementById(`like-btn-${post_id}`).innerHTML = icn;
        }
    })
    false
}

function follow(user_id) {
    
    fetch(`/user/${user_id}/page/1`, {
    method: "POST"
    })
    .then(response => response.json())
    .then(result => {
    document.getElementById("follow-btn").innerHTML = `${result.stat}`;
    document.getElementById("follow-data").innerHTML = `Followers: ${result.followers} | Following: ${result.following}`;
    })
    
    false
}

function edit_request(post_id) {
    var data = document.getElementById(`post-text-${post_id}`);
    var data_copy = data.innerHTML;
    data.innerHTML = '';

    var txtArea = document.createElement('textarea');
    txtArea.value = data_copy;
    txtArea.style.width = '100%';
    txtArea.setAttribute('id', `edit-${post_id}`);
    data.appendChild(txtArea);
    data.appendChild(document.createElement("br"));

    var btn_sub = document.createElement('button');
    btn_sub.className = "btn btn-dark";
    btn_sub.innerHTML = "Submit";
    btn_sub.addEventListener('click', function () {
        if (document.getElementById(`edit-${post_id}`).value == '') {
            alert("This field can't be empty");
            return false;
        }
        fetch(`/edit/${post_id}`, {
            method: "POST",
            body: JSON.stringify({
                edited: document.getElementById(`edit-${post_id}`).value 
            })
        })
        .then(response => response.json())
        .then(result => {
            console.log(result);
            if (result.stat ==  "Success") {
                document.getElementById(`post-text-${post_id}`).innerHTML = result.content;
            } else {
                document.getElementById(`post-text-${post_id}`).innerHTML = data_copy;
                alert("You do not have permission to edit this post");
            }
        })
        
    }); 
    data.appendChild(btn_sub);

    var btn_can = document.createElement('button');
    btn_can.className = "btn btn-dark";
    btn_can.style.marginLeft = '5px';
    btn_can.innerHTML = "Cancel"; 
    btn_can.addEventListener('click', function () {
        document.getElementById(`post-text-${post_id}`).innerHTML = data_copy;
    });
    data.appendChild(btn_can);

    false

}
