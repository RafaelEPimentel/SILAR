$(document).ready(function(){
  $("#addPoint").click(function(){
      console.log("pep")
      var new_add = '<div id="cardcontainer" class="card ml-5 mt-5" style="width: 18rem;">\n' +
          '                <img src="https://images.vexels.com/media/users/3/183658/isolated/preview/9670fc23c81911292547373aa512893f-number-one-lettering-silhouette-by-vexels.png" class="card-img-top" alt="...">\n' +
          '                <div class="card-body">\n' +
          '                    <h5 class="card-title">First Spot</h5>\n' +
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
          '                </div>\n' +
          '            </div>';
      $("#cardcontainer").after(new_add);
  });
});