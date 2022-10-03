function caldescuentos(){
    document.getElementById("tabla").innerHTML="";
    let precio=Number(document.getElementById("id_precio").value)
    let cuota=Number(document.getElementById("id_cuotas").value)
    let fechainicio=(document.getElementById("id_fechainicio").value)
    let fechas = [];
    let fechaActual = Date.parse(fechainicio);
    let mes_actual = moment(fechaActual);
    mes_actual.add(1, 'day');
    ca=precio/cuota;
    total=ca*cuota
    capicuota=ca.toFixed(2);
    if(precio>0){
        for(i=1;i<=cuota;i++){
            precio=precio-ca;
            saldocuota=precio.toFixed(2);
            fechas[i] = mes_actual.format('DD-MM-YYYY');
            mes_actual.add(1, 'month');
            document.getElementById("tabla").innerHTML=document.getElementById("tabla").innerHTML+
                    `<tr>
                        <td> ${i}</td>
                        <td>${fechas[i]}</td>
                        <td> ${capicuota}</td>
                        <td> ${saldocuota}</td>
                    </tr>`;
        }
        n1=total.toFixed(2);
        document.getElementById("totalpagos").innerHTML=n1;

        let tinteres=document.getElementById("id_valorcuota");
        tinteres.value= capicuota


    }else{
        alert("Falta ingresar Información");
    }
}
document.addEventListener("DOMContentLoaded", e => {
   console.log("Pagina cargada")

     document.getElementById('id_empresa').value=1
    document.getElementById("tabla").innerHTML="";
    let precio=Number(document.getElementById("id_precio").value)
    let cuota=Number(document.getElementById("id_cuotas").value)
    let fechainicio=(document.getElementById("id_fechainicio").value)
    let fechas = [];
    let fechaActual = Date.parse(fechainicio);
    let mes_actual = moment(fechaActual);
    mes_actual.add(1, 'day');
    ca=precio/cuota;
    total=ca*cuota
    capicuota=ca.toFixed(2);
    if(precio>0){
        for(i=1;i<=cuota;i++){
            precio=precio-ca;
            saldocuota=precio.toFixed(2);
            fechas[i] = mes_actual.format('DD-MM-YYYY');
            mes_actual.add(1, 'month');
            document.getElementById("tabla").innerHTML=document.getElementById("tabla").innerHTML+
                    `<tr>
                        <td> ${i}</td>
                        <td>${fechas[i]}</td>
                        <td> ${capicuota}</td>
                        <td> ${saldocuota}</td>
                    </tr>`;
        }
        n1=total.toFixed(2);
        document.getElementById("totalpagos").innerHTML=n1;

        let tinteres=document.getElementById("id_valorcuota");
        tinteres.value= capicuota
    }
});
