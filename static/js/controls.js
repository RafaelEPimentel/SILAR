$(document).ready(function(){
  $("#addPoint").click(function(){
      console.log("pep")
      var new_add = '<div id="cardcontainer" class="card ml-5 mt-5" style="width: 18rem;">\n' +
          '                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Target_Corporation_logo_%28vector%29.svg/1200px-Target_Corporation_logo_%28vector%29.svg.png" class="card-img-top" alt="...">\n' +
          '                <div class="card-body">\n' +
          '                    <h5 class="card-title">Point</h5>\n' +
          '                    <div class="input-group mb-3">\n' +
          '                    <span class="input-group-text" id="basic-addon1">X</span>\n' +
          '                    <input name="x[]" type="number" class="form-control" placeholder="X Coordinates" aria-label="X" aria-describedby="basic-addon1">\n' +
          '                    </div>\n' +
          '                    <div class="input-group mb-3">\n' +
          '                    <span class="input-group-text" id="basic-addon1">Y</span>\n' +
          '                    <input name="y[]" type="number" class="form-control" placeholder="Y Coordinates" aria-label="Y" aria-describedby="basic-addon1">\n' +
          '                    </div>\n' +
          '                    <div class="input-group mb-3">\n' +
          '                    <span class="input-group-text" id="basic-addon1">Z</span>\n' +
          '                    <input name="z[]" type="number" class="form-control" placeholder="Z Coordinates" aria-label="Z" aria-describedby="basic-addon1">\n' +
          '                    </div>\n' +
          '                    <div class="input-group mb-3">\n' +
          '                    <span class="input-group-text" id="basic-addon1">Time</span>\n' +
          '                    <input name="time[]" type="number" class="form-control" placeholder="Time at point" aria-label="Time" aria-describedby="basic-addon1">\n' +
          '                    </div>\n' +
          '                    <div class="input-group mb-3">\n' +
          '                    <span class="input-group-text" id="basic-addon1">Z Speed Up</span>\n' +
          '                    <input name="zspeed[]" type="number" class="form-control" placeholder="Z Speed Up" aria-label="zspeed" aria-describedby="basic-addon1">\n' +
          '                    </div>\n' +
          '                    <div class="input-group mb-3">\n' +
          '                    <span class="input-group-text" id="basic-addon1">Z Speed Down</span>\n' +
          '                    <input name="zspeeddown[]" type="number" class="form-control" placeholder="Z Speed Down" aria-label="zspeeddown" aria-describedby="basic-addon1">\n' +
          '                    </div>\n' +
          '                </div>\n' +
          '            </div>';
      $("#cardcontainer").after(new_add);
  });
  setInterval(function(){
      $.ajax({
            url : '/getglobals',
            success: function(data) {
                $('#informationcontainer').html(
                    '<div class="alert alert-warning alert-dismissible fade show" role="alert">\n' +
                    '  <strong>Cycle: </strong>\n' + data['currentcycle'] +
                    '  <strong>X: </strong>\n' + data['x'] +
                    '  <strong>Y: </strong>\n' + data['y'] +
                    '  <strong>Z: </strong>\n' + data['z'] +
                    '  <button type="button" class="close" data-dismiss="alert" aria-label="Close">\n' +
                    '    <span aria-hidden="true">&times;</span>\n' +
                    '  </button>\n' +
                    '</div>'
                )



            }
        });},1000)
});

