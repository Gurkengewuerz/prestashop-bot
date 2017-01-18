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
                        "<td>" +
                        "<a href='#' class='toggle-lic' for-id='" + item.licence + "'><span class='glyphicon glyphicon-eye-close' aria-hidden='true'></span></a>" +
                        "<a href='#' class='remove' for-id='" + item.licence + "'><span class='glyphicon glyphicon-trash' for-id='" + item.licence + "' aria-hidden='true'></span></a>" +
                        "</td>" +
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

    $("#newLicenceBtn").click(function (e) {
        e.preventDefault();
        var lic = $("#newLicenceText").val();
        var reference = $("#referenceText").val();
        if (!lic.trim()) return;
        $.ajax({
            url: "/api/add/licence/" + encodeURIComponent(lic) + "/" + encodeURIComponent(reference),
            async: true,
            dataType: "json",
            success: function (data) {
                console.log(data);
                var json = data;
                if (json.error !== "No") {
                    alert(json.error);
                    return;
                }
                console.log(json.info);
                refresh();
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.log(textStatus, errorThrown);
            }
        });
    });

    // Funktioniert nicht?!
    // Wird nicht aufgerufen
    $(".remove").click(function (e) {
        console.log("Clicked a remove button");
        var lic = $(this).attr("for-id");
        alert(lic);
    });
});
