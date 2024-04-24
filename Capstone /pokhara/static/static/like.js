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
