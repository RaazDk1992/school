const root="/proxy/";
function getHi(path){
    axios.get(root+path)
    .then(response =>{

        console.log(response);
    })
    .catch(error=>{
        console.log(error);
    })
}