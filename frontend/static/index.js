let selected_image = [];

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