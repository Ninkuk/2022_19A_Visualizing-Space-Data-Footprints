let selected_image = [];
let contentElement = document.getElementsByClassName("image-grid")[1];

function submit_demo_images() {
    if(selected_image.length == 0) {
        alert("Please select an image")
        return
    }
    
    fetch('/submit_demo', {
        headers: {
          'Content-Type': 'application/json'
        },
    
        method: 'POST',
    
        // This is the content we're sending to Python
        body: JSON.stringify(selected_image)
    }).then(function (response) { // At this point, Flask has received the data
        return response.text();
    }).then(function (file_content) {
        file_name = "Psyche_Footprints_Demo.csv"
        var myFile = new File([file_content], file_name, {type: "text/plain;charset=utf-8"});
        saveAs(myFile);
    });
}

/**
 * File upload methods from Yairopro
 * https://stackoverflow.com/users/4170935/yairopro
*/
async function upload_images(){
    let files = await file_selector("image/*", true);
    contentElement.innerHTML = files.map(file => `<img src="${URL.createObjectURL(file)}" >`).join('');
}

// ---- function definition ----
function file_selector(contentType, multiple){
    return new Promise(resolve => {
        let input = document.createElement('input');
        input.type = 'file';
        input.multiple = multiple;
        input.accept = contentType;

        input.onchange = _ => {
            let files = Array.from(input.files);
            if (multiple)
                resolve(files);
            else
                resolve(files[0]);
        };

        input.click();
    });
}

// ---- Yairopro's code end ----

function select_image(id, src) {
    if(selected_image.includes(src)) {
        document.getElementById(id).style.borderStyle = "none"
        selected_image = delete_value(selected_image, src)
    } else {
        document.getElementById(id).style.borderStyle = "solid"
        selected_image.push(src)       
    }
}

function delete_value(array, value_to_remove) { 
    return array.filter(function(element){ 
        return element != value_to_remove; 
    });
}