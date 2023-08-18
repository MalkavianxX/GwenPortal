$(document).ready(function () {
    var a = new DataTable('#example',{
        responsive: !0,
        language: {
            paginate: {
                previous: "<i class='mdi mdi-chevron-left'>",
                next: "<i class='mdi mdi-chevron-right'>",

            },
            url: '//cdn.datatables.net/plug-ins/1.10.24/i18n/Spanish.json',

        },
        drawCallback: function() {
            $(".dataTables_paginate > .pagination").addClass("pagination-rounded")
        }
    });
   
  });
