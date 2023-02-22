function removeCourse(course_id){
 
    url='/dashboard/remove_course/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
            'id':course_id
        })
        })
        .then((response)=>{
        response.json().then((data) => {
            if(data.message == 'success'){
                document.getElementById(course_id).style.display = "none"
            }
            else{
                console.log(data.message)
            }
        })
    })
}
function removeModul(modul_id){
 
    url='/dashboard/remove_modul/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
            'id':modul_id
        })
        })
        .then((response)=>{
        response.json().then((data) => {
            if(data.message == 'success'){
                document.getElementById(modul_id).style.display = "none"
            }
            else{
                console.log(data.message)
            }
        })
    })
}

function block_status(student_id){
 
    url='/dashboard/blockuser/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
            'id':student_id
        })
        })
        .then((response)=>{
        response.json().then((data) => {
            id = 'status'+student_id
            if (!data.status){
                elem = document.getElementById(id)
                elem.classList.remove('badge-outline-danger')
                elem.classList.add('badge-outline-success')
                elem.innerHTML = 'Unblocked'
                
            }
            else{
                elem = document.getElementById(id)
                elem.classList.remove('badge-outline-success')
                elem.classList.add('badge-outline-danger')
                elem.innerHTML = 'Blocked'
            }
        })
    })
}

function removeUser(user_id){
 
    url='/dashboard/remove_student/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
            'id':user_id
        })
        })
        .then((response)=>{
        response.json().then((data) => {
            if(data.message == 'success'){
                document.getElementById(user_id).style.display = "none"
            }
            else{
                console.log(data.message)
            }
        })
    })
}

function change_status(id){
    url=`/dashboard/status/`
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
            'id':id
        })
        })
        .then((response)=>{
        response.json().then((data) => {
            id = 'status'+id
            if (data.status){
                elem = document.getElementById(id)
                elem.classList.remove('badge-outline-danger')
                elem.classList.add('badge-outline-success')
                elem.innerHTML = 'Active'

            }
            else{
                elem = document.getElementById(id)
                elem.classList.remove('badge-outline-success')
                elem.classList.add('badge-outline-danger')
                elem.innerHTML = 'In Active'
            }
        })
    })
}
function sugession(id){
    url=`/dashboard/sugession_status/`
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
            'id':id
        })
        })
        .then((response)=>{
        response.json().then((data) => {
            id = 'status'+id
            if (data.status){
                elem = document.getElementById(id)
                elem.classList.remove('badge-outline-danger')
                elem.classList.add('badge-outline-success')
                elem.innerHTML = 'Fixed'

            }
            else{
                elem = document.getElementById(id)
                elem.classList.remove('badge-outline-success')
                elem.classList.add('badge-outline-danger')
                elem.innerHTML = 'Not Fixed'
            }
        })
    })
}

function removenews(id){
    url=`/dashboard/remove_news/`
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
            'id':id
        })
        })
        .then((response)=>{
        response.json().then((data) => {
            document.getElementById(id).style.display = 'none'
        })
    })
}

function removeRegister(reg_id){
    url=`/dashboard/remove_register/`
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
            'id':reg_id
        })
        })
        .then((response)=>{
        response.json().then((data) => {
            document.getElementById(reg_id).style.display = 'none'
        })
    })
}
function removeAdmin(reg_id){
    url=`/dashboard/remove_admin/`
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
            'id':reg_id
        })
        })
        .then((response)=>{
        response.json().then((data) => {
            document.getElementById(reg_id).style.display = 'none'
        })
    })
}

function removeGroup(gr_id){
    url=`/dashboard/remove_group/`
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
            'id':gr_id
        })
        })
        .then((response)=>{
        response.json().then((data) => {
            document.getElementById(gr_id).style.display = 'none'
        })
    })
}