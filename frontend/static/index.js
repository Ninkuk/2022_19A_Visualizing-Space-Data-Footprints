let selected_image = [];

function submit_demo_images() {
    fetch('/submit_demo', {
        // Declare what type of data we're sending
        headers: {
          'Content-Type': 'application/json'
        },
    
        // Specify the method
        method: 'POST',
    
        // A JSON payload
        body: JSON.stringify(selected_image)
    }).then(function (response) { // At this point, Flask has received the data
        return response.text();
    }).then(function (file_content) {
        file_name = "Psyche_Footprints_Demo.csv"
        var myFile = new File([file_content], file_name, {type: "text/plain;charset=utf-8"});
        saveAs(myFile);
    });
}

function select_image(id, src) {
    if(selected_image.includes(src)) {
        document.getElementById(id).style.borderStyle = "none"
        selected_image = delete_value(selected_image, src)
        console.log("src selected!");
    } else {
        document.getElementById(id).style.borderStyle = "solid"
        selected_image.push(src)       
        console.log("selected_image", selected_image);
    }
}

function delete_value(arr, value) { 
    return arr.filter(function(ele){ 
        return ele != value; 
    });
}