
$(document).ready(function(){

    // Table
    let table = new Tabulator("#tablulator", {
        selectable:true,
        layout:"fitColumns"
    });


    // Get data
    let all_data = null;
    $.ajax({
        'async': false,
        'type': 'GET',
        'url': '/api/students/get/all',
        'success': function (data) {
            all_data = data;
        }
    });

    let columns = [
        {formatter:"rowSelection", titleFormatter:"rowSelection", headerSort:false, cellClick:function(e, cell){
            cell.getRow().toggleSelect();
        }, width:45, resizable:false},
        {title:"Avatar", field:"avatar_path", resizable:false, headerSort:false, formatter:function(cell, formatterParams, onRendered){
            avatar_path = cell.getValue();

            html = `<div class="avatar"><img src=${avatar_path}/></div>`

            return html
        }},
        {title:"First Name", field:"first_name", formatter:"plaintext"},
        {title:"Last Name", field:"last_name", formatter:"plaintext"},
        {title:"Email", field:"email_address", formatter:"plaintext"},
        {title:"Phone Number", field:"phone_number", formatter:"plaintext"},
        {title:"Last Visit", field:"", formatter:"plaintext"}
    ];

    let columnData = [];
    
    // Object.entries(tabledata[0]).forEach(([key, value]) => {
    //     // console.log(`${key} ${value}`);
    //     columnData.push({title: key, field:key});
    // });

    table.setColumns(columns);
    table.setData(all_data);




});