$(document).ready(function () {
    var type = "shop";

    function loadShop() {
        $.ajax({
            url: '/api/get/shop',
            async: true,
            dataType: "json",
            success: function (data) {
                console.log(data);
                $("#shopData tbody > tr").remove();
                $.each(data, function (i, item) {
                    console.log(item);
                    var payStats = "";
                    item.paystat.forEach(function (val) {
                       payStats += "<li>" + val + "</li>";
                    });
                    $("#shopData").append(
                        "<tr>" +
                            "<td>"+item.id+"</td>" +
                            "<td>"+item.shop_name+"</td>" +
                            "<td>"+item.url+"</td>" +
                            "<td>"+item.api_key+"</td>" +
                            "<td><ul>"+ payStats + "</ul></td>" +
                            "<td>"+item.delivstat+"</td>" +
                        "</tr>"
                    );
                    console.log(item.id);
                });
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.log(textStatus, errorThrown);
            }
        });
    }

    function loadLicence() {
        $.ajax({
            url: '/api/get/licence',
            async: true,
            dataType: "json",
            success: function (data) {
                console.log(data);
                $("#licenceData tbody > tr").remove();
                $("#licenceData").append( // TODO: WORK
                        "<tr>" +
                            "<td>"+item.id+"</td>" +
                            "<td>"+item.shop_name+"</td>" +
                            "<td>"+item.url+"</td>" +
                            "<td>"+item.api_key+"</td>" +
                            "<td><ul>"+ payStats + "</ul></td>" +
                            "<td>"+item.delivstat+"</td>" +
                        "</tr>"
                    );
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.log(textStatus, errorThrown);
            }
        });
    }


    function refresh() {
        if (type == "shop") {
            $("#shop").show();
            $("#licence").hide();
            loadShop();
            console.log("Show Sop")
        } else {
            $("#shop").hide();
            $("#licence").show();
            loadLicence();
            console.log("Show Licence");
        }
    }

    refresh();

    $("#showShop").click(function () {
        type = "shop";
        refresh();
    });

    $("#showLicence").click(function () {
        type = "licence";
        refresh();
    });
});
