function gen_table(){
    document.getElementById("tab").innerHTML="";
    let capital=Number(document.getElementById("id_capital").value)
    let cuota=Number(document.getElementById("id_cuotas").value)
    let interes=Number(document.getElementById("id_interes").value)
    let fechas = [];
    let fechaActual = Date.now();
    let mes_actual = moment(fechaActual);
    mes_actual.add(1, 'month');
    ca=capital/cuota;
    capicuota=ca.toFixed(2);
    interes2=((capital*interes)/100)/cuota;
    intecuota=interes2.toFixed(2);
    total=ca+interes2;
    totalcuota=total.toFixed(2);
    t_p=total*cuota;
    if(capital>0){
        for(i=1;i<=cuota;i++){
            t_p=t_p-totalcuota;
            saldocuota=t_p.toFixed(2);
            fechas[i] = mes_actual.format('MM-DD-YYYY');
            mes_actual.add(1, 'month');
            document.getElementById("tab").innerHTML=document.getElementById("tab").innerHTML+
                    `<tr>
                        <td> ${i}</td>
                        <td>${fechas[i]}</td>
                        <td> ${capicuota}</td>
                        <td> ${intecuota}</td>
                        <td> ${totalcuota}</td>
                        <td> ${saldocuota}</td>
                    </tr>`;
        }
        n1=capital.toFixed(2);
        t_i=interes2*cuota;
        d4=t_i.toFixed(2);
        t_p=total*cuota;
        d5=t_p.toFixed(2);
        document.getElementById("totalcapital").innerHTML=n1;
        document.getElementById("totalinteres").innerHTML=d4;
        document.getElementById("totalpagar").innerHTML=d5;

        let tinteres=document.getElementById("id_totalinteres");
        tinteres.value= d4
        let ttotal=document.getElementById("id_total");
        ttotal.value= d5


    }else{
        alert("Falta ingresar Información");
    }
}
document.addEventListener("DOMContentLoaded", e => {
   console.log("Pagina cargada")

     document.getElementById('id_empresa').value=1

   //delegacion de eventos: el objeto que origina el evento coincide con el metodo matches() ejcuta el codigo
});



