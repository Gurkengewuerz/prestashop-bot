$(document).ready(function () {
    var type = "shop";

    function formatDate(date) {
        var engMonth = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12"
        };
        dateArray = date.toString().split(" ");
        return dateArray[2] + "." + engMonth[dateArray[1]] + "." + dateArray[3] + " " + dateArray[4];
    }

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
                        "<td>" + item.id + "</td>" +
                        "<td>" + item.shop_name + "</td>" +
                        "<td>" + item.url + "</td>" +
                        "<td>" + item.api_key + "</td>" +
                        "<td><ul>" + payStats + "</ul></td>" +
                        "<td>" + item.delivstat + "</td>" +
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
                $.each(data, function (i, item) {
                    var disabled = item.rendet_timestamp == null ? "success" : "danger";
                    $("#licenceData").append(
                        "<tr class ='" + disabled + "'>" +
                        "<td>" + item.id + "</td>" +
                        "<td>" + item.licence + "</td>" +
                        "<td>" + item.product_reference + "</td>" +
                        "<td>" + formatDate(new Date(item.created_timestamp * 1000)) + "</td>" +
                        "<td>" + (item.rendet_timestamp == null ? "nicht vergeben" : formatDate(new Date(item.rendet_timestamp * 1000))) + "</td>" +
                        "</tr>"
                    );
                });
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

    $("#addLicence").click(function () {
        $('#addLicenceModal').modal("toggle");
    });

});
