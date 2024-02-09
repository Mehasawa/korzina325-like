//const csrf_token = "{{ csrf_token }}"
let fin = document.getElementById('fin')
let fin2 = document.getElementById('fin2')
let forma = document.getElementById('forma1')
let formahid = document.getElementById('forma')
// let pythonbut = document.getElementById('myformbut')
// console.log(1)
// console.log(fin2)
// console.log(fin)


fin.onclick = f1
fin2.onclick = f2

function f1(){
    console.log(2)
    formahid.hidden = false

}

function f2(){
    console.log('privet')
    let adres = document.getElementById('id_adres').value
    let name = document.getElementById('id_name').value
    let tel = document.getElementById('id_tel').value
    var re = /^[+][\d]{10}\d$/

    var valid = re.test(tel)

    if (adres&&name&&tel&&valid)
  {
      console.log(true)
        let url = '/cart/pobeda/'
        $.ajax(url,{
            method:'POST',
            data:{k1:adres, k2:name, k3:tel},
            success: function (response){
                console.log(response.mes)
                window.location.href = response.link
            },
            error: function (response){
                console.log(response)
                console.log(this.error)
                console.log(url)
            },

        })
    }
    else {
        alert('ne zapolneno')
    }
}


function f11(event,id){
    event.preventDefault()
    // alert(this)
    console.log(event.target)
    console.log(id)
    img = event.target
    img1=img.getElementsByClassName('serdze')
    console.log(img1)
    let color=''
    // img1.src='img/sred.png'
    if (img.src.includes('/static/img/swhite.png')){
        img.setAttribute('src','/static/img/sred.png')
        color='red'
    }
    else{
        img.setAttribute('src','/static/img/swhite.png')
        color = 'white'
    }
    let url = '/toizbran/'
        $.ajax(url,{
            method:'POST',
            data:{k1:id, k2:color},
            success: function (response){
                console.log(response.mes)
                // window.location.href = response.link
            },
            error: function (response){
                console.log(response)
                console.log(this.error)
                console.log(url)
            },

        })
    // id1=document.getElementById('id1')
    // id1.setAttribute('src','/static/img/sred.png')


}