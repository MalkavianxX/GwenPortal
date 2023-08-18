function formatearFecha(fechaString) {
  const [dia, mes, anio] = fechaString.split('/');

  // Convertir el string a un objeto de tipo Date
  const fecha = new Date(`${anio}-${mes}-${dia}`);

  // Obtener el nombre del día de la semana
  const opcionesFecha = { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' };
  const formatoFecha = new Intl.DateTimeFormat('es', opcionesFecha);
  const fechaFormateada = formatoFecha.format(fecha);

  return fechaFormateada;
}
function formatearHora(fechaString) {
  const fecha = new Date(fechaString);
  const horas = fecha.getHours();
  const minutos = fecha.getMinutes();
  
  // Determinar si es AM o PM
  const periodo = horas >= 12 ? 'pm' : 'am';
  
  // Convertir las horas al formato de 12 horas
  const horas12 = horas % 12 === 0 ? 12 : horas % 12;
  
  // Agregar un cero inicial a los minutos si es necesario
  const minutosFormateados = minutos.toString().padStart(2, '0');
  
  return `${horas12}:${minutosFormateados} ${periodo}`;
}


function eventDataTransform() {
  // Initialize an array to store the Event objects.
  var eventDataList = getClasesServer();
  var events = [];

  // Loop through each eventData in the list.
  eventDataList.forEach((eventData) => {
    // Check if the event data is valid.
    if (!eventData.hasOwnProperty("title")) {
      return; // Skip this iteration if the eventData is invalid.
    }

    // Create an Event object using FullCalendar.createEvent
    var event = FullCalendar.createEvent({
      title: eventData.title,
      start: eventData.start,
      end: eventData.end,
      classNames: eventData.classNames,
      allDay: eventData.allDay,
      daysOfWeek: eventData.daysOfWeek,
      extendedProps: {
        nombreprofe: eventData.nombreprofe,
        linkprofile: eventData.linkprofile,
        linkclase: eventData.linkclase,
      },
    });

    // Add the Event object to the events array.
    events.push(event);
  });
  console.log(events);
  // Return the list of Event objects.
  return events;
}


!(function (l) {
  "use strict";
  function e() {
    (this.$body = l("body")),
      (this.$modal = new bootstrap.Modal(
        document.getElementById("event-modal"),
        { backdrop: "static" }
      )),
      (this.$modalshow = new bootstrap.Modal(
        document.getElementById("event-show"),
      )),
      (this.$calendar = l("#calendar")),
      (this.$formEvent = l("#form-event")),
      (this.$btnNewEvent = l("#btn-new-event")),
      (this.$btnDeleteEvent = l("#btn-delete-event")),
      (this.$btnSaveEvent = l("#btn-save-event")),
      (this.$modalTitle = l("#modal-title")),
      (this.$modalshowTitle = l("#modalshow-title")),
      (this.$calendarObj = null),
      (this.$selectedEvent = null),
      (this.$newEventData = null);
  }
  (e.prototype.onEventClick = function (e) {
      this.$modalshowTitle.text(),
      this.$modalshow.show(),
      (this.$selectedEvent = e.event),
      document.getElementById("event-show-title").innerText = this.$selectedEvent.title,
      document.getElementById("event-show-nombreprofe").innerText = this.$selectedEvent.extendedProps.nombreprofe,
      document.getElementById("event-show-fecha").innerText = formatearFecha(this.$selectedEvent.start.toLocaleDateString()) ,
      document.getElementById("event-show-horaInicio").innerText = formatearHora(this.$selectedEvent.startStr) ,
      document.getElementById("event-show-horaFin").innerText = formatearHora(this.$selectedEvent.endStr) ,
      console.log(this.$selectedEvent)
  }),
    (e.prototype.onSelect = function (e) {
      this.$formEvent[0].reset(),
        this.$formEvent.removeClass("was-validated"),
        (this.$selectedEvent = null),
        (this.$newEventData = e),
        this.$btnDeleteEvent.hide(),
        this.$modalTitle.text("Agregar nueva clase"),
        this.$modal.show(),
        this.$calendarObj.unselect();
    }),
    (e.prototype.init = function () {
      var e = new Date(l.now()),
        e =
          (new FullCalendar.Draggable(
            document.getElementById("external-events"),
            {
              itemSelector: ".external-event",
              eventData: function (e) {
                return {
                  title: e.innerText,
                  className: l(e).data("class"),
                  duration: { days: l(e).data("duration") },
                  start: new Date(l.now() + 338e6),
                  end: new Date(l.now() + 4056e5),
                  daysOfWeek: [1,2,3],
                };
              },
            }
          ),
            [

        
    
            ]),
        a = this;
      (a.$calendarObj = new FullCalendar.Calendar(a.$calendar[0], {
     
        slotDuration: "00:15:00",
        slotMinTime: "08:00:00",
        slotMaxTime: "19:00:00",
        themeSystem: "bootstrap",
        bootstrapFontAwesome: !1,
        buttonText: {
          today: "Hoy",
          month: "Mes",
          week: "Semana",
          day: "Día",
          prev: "Anterior",
          next: "Siguiente",
        },
        initialView: "dayGridMonth",
        locale: "es",
        timeZone: "America/Mexico_City",

        initialDate: new Date(document.getElementById("initial-date").value),
        eventSources: [

          // your event source
          {
            url: 'http://127.0.0.1:8000/horario/getClasesFormatJson/9/',
            method: 'POST',
   
            failure: function() {
              alert('there was an error while fetching events!');
            },
            color: 'yellow',   // a non-ajax option
            textColor: 'black' // a non-ajax option
          }
      
          // any other sources...
      
        ]
      ,
        
        handleWindowResize: !0,
        height: l(window).height() - 200,
        headerToolbar: {
          left: "prev,next today",
          center: "title",
          right: "dayGridMonth,timeGridWeek,timeGridDay,listMonth",
        },
        initialEvents: e,
        editable: !0,
        droppable: !0,
        selectable: !0,
        dateClick: function (e) {
          a.onSelect(e);
        },
        eventClick: function (e) {
          a.onEventClick(e);
        },
      })),
 
        a.$calendarObj.render(),
        a.$calendarObj.getEvents() ,
        a.$btnNewEvent.on("click", function (e) {
          a.onSelect({ date: new Date(), allDay: !0 });
        }),
        a.$formEvent.on("submit", function (e) {
          e.preventDefault();
          var t,
            n = a.$formEvent[0];
            var dataform;
            var checkboxes = document.querySelectorAll('input[type="checkbox"]');
          n.checkValidity()
            ? (a.$selectedEvent
              ? (a.$selectedEvent.setProp("title", l("#event-nombre").val()),
                a.$selectedEvent.setProp("start", l("#event-dateinit").val()),

                a.$selectedEvent.setProp("classNames", [
                  l("#event-category").val(),
                ]))
              : ((t = {
                title: l("#event-nombre").val(),
                start: l("#event-dateinit").val(),
                end: l("#event-dateend").val(),

                className: l("#event-category").val(),
              }),
                a.$calendarObj.addEvent(t)),
                
                dataform = {
                  nombre: document.getElementById("event-nombre").value,
                  materia: document.getElementById("event-materia").value,
                  horario: document.getElementById("event-horario").value,
                  hora_inicio: document.getElementById("event-dateinit").value, 
                  hora_fin: document.getElementById("event-dateend").value,
                  color: document.getElementById("event-color").value,
                  dias_seleccionados: [],  // Inicializar el arreglo para los días seleccionados

              },
              checkboxes.forEach(function(checkbox) {
                if (checkbox.checked) {
                  if (checkbox.checked && checkbox.value !== "on") {
                    dataform.dias_seleccionados.push(checkbox.value);
                }
                }
            }),console.log(dataform.hora_inicio,dataform.hora_fin),
              // Agregar los días seleccionados al objeto dataform
           
                l.ajax({
                  type: "POST",
                  contentType: "application/json",
                  url: "http://127.0.0.1:8000/horario/saveClase", // Reemplaza "/ruta/a/la/vista/django/" con la URL adecuada
                  data: JSON.stringify(dataform),
                  success: function (data) {
                    location.reload();
                  },
                  error: function (error) {
                    console.error("Error al enviar el evento a Django:", error);
                  }
                }),
              a.$modal.hide())
            : (e.stopPropagation(), n.classList.add("was-validated"));
        }),

        l(
          a.$btnDeleteEvent.on("click", function (e) {
            a.$selectedEvent &&
              (a.$selectedEvent.remove(),
                (a.$selectedEvent = null),
                a.$modal.hide());
          })
        );
    }),
    (l.CalendarApp = new e()),
    (l.CalendarApp.Constructor = e);
})(window.jQuery),
  (function () {
    "use strict";

    window.jQuery.CalendarApp.init();

  })();


  

  