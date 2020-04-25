$(function() {

    getData = (data) => {
       $.each(data, (i, d) => {
           const headline = $("<h2></h2>");
           headline.text(d);
           $("body").append(headline)
           
       })
    }
    $.ajax({
        url: "news.json",
        dataType: 'json',
        success: getData,
        error: err => console.log(err)
      });

});