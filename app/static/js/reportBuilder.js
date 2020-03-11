var tabledata = null

var retrievedFilters = function () {
    var tmp = null;
    $.ajax({
        'async': false,
        'type': 'GET',
        'url': '/api/report/filters',
        'success': function (data) {
            tmp = data;
        }
    });
    return tmp;
}();


var table = new Tabulator("#tablulator", {
    height:"311px",
    index:'id'
});

var operators = [
    {type: 'eq', optgroup: 'custom', nb_inputs:1, apply_to: ['number']},
    {type: 'neq', optgroup: 'custom', nb_inputs:1, apply_to: ['number']},
    {type: 'gt', optgroup: 'custom', nb_inputs:1, apply_to: ['number']},
    {type: 'ge', optgroup: 'custom', nb_inputs:1, apply_to: ['number']},
    {type: 'lt', optgroup: 'custom', nb_inputs:1, apply_to: ['number']},
    {type: 'le', optgroup: 'custom', nb_inputs:1, apply_to: ['number']},
    
    // { type: 'begins_with', optgroup: 'basic' },
    // { type: 'not_begins_with', optgroup: 'basic' },
    // { type: 'contains', optgroup: 'basic' },
    // { type: 'not_contains', optgroup: 'basic' },
    // { type: 'ends_with', optgroup: 'basic' },
    // { type: 'not_ends_with', optgroup: 'basic' }

    { type: 'startswith', optgroup: 'custom', nb_inputs:1, apply_to: ['string'] },
    { type: 'not_startswith', optgroup: 'custom', nb_inputs:1, apply_to: ['string'] },
    { type: 'contains', optgroup: 'custom', nb_inputs:1, apply_to: ['string'] },
    { type: 'not_contains', optgroup: 'custom', nb_inputs:1, apply_to: ['string'] },
    { type: 'endswith', optgroup: 'custom', nb_inputs:1, apply_to: ['string'] },
    { type: 'not_endswith', optgroup: 'custom', nb_inputs:1, apply_to: ['string'] }

    // stringOps = ['startswith', 'not_startswith', 'contains', 'not_contains', 'endswith', 'not_endswith']

    
];

// var operators_remap = {
//     equal: '=',
//     not_equal: '!=',
//     greater: '>',
//     greater_or_equal: '>=',
//     less: '<',
//     less_or_equal: '<='
// };

var operators_remap = {
    eq: '=',
    neq: '!=',
    gt: '>',
    ge: '>=',
    lt: '<',
    le: '<='
};


$('#query_builder').queryBuilder({

    operators: operators,

    // Change how the operators are displayed
    lang: {
        operators: operators_remap
    },



    // Populate the selectable filters
    filters: retrievedFilters 
    
});

// $('#get_rules').on('click', function() {
buttons.on("action:runReport", function( event ) {
    var result = $('#query_builder').queryBuilder('getRules');
    
    // Print rules to console
    if (!$.isEmptyObject(result)) {
    //   alert(JSON.stringify(result, null, 2));
        console.log(JSON.stringify(result, null, 2))
    

        // Submit rules to system
        $.ajax({
            'async': false,
            'type': 'POST',
            'url': '/api/report/rules',
            'contentType': "application/json; charset=utf-8",
            'data': JSON.stringify(result, null, 2),
            'success': function (data) {
                // var w = window.open('/report/display', 'Report Output');
                // w.document.write(data)
                var tabledata = JSON.parse(data);
                var columnData = [];
                // console.log(tabledata)
                Object.entries(tabledata[0]).forEach(([key, value]) => {
                    // console.log(`${key} ${value}`);
                    columnData.push({title: key, field:key});
                });

                console.log(columnData);


                // alert(data);
                // var table = new Tabulator("#tablulator", {
                //         height:"311px",
                //         data: tabledata,
                //         index:'id',
                //         columns: columnData
                //     });
                table.setColumns(columnData);
                table.setData(tabledata);
            },
            'failure': function(errMsg) {
                // alert(errMsg)
            }
        });

    }
  });


  var testFilter = [{
        id: 'name',
        label: 'Name',
        type: 'string'
      }, 
      {
        id: 'category',
        label: 'Category',
        type: 'integer',
        input: 'select',
        values: {
          1: 'Books',
          2: 'Movies',
          3: 'Music',
          4: 'Tools',
          5: 'Goodies',
          6: 'Clothes'
        },
        operators: ['equal', 'not_equal', 'in', 'not_in', 'is_null', 'is_not_null']
      }, 
      {
        id: 'in_stock',
        label: 'In stock',
        type: 'integer',
        input: 'radio',
        values: {
          1: 'Yes',
          0: 'No'
        },
        operators: ['equal']
      }, 
      {
        id: 'price',
        label: 'Price',
        type: 'double',
        validation: {
          min: 0,
          step: 0.01
        }
      }, {
        id: 'id',
        label: 'Identifier',
        type: 'string',
        placeholder: '____-____-____',
        operators: ['equal', 'not_equal'],
        validation: {
          format: /^.{4}-.{4}-.{4}$/
        }
      }];