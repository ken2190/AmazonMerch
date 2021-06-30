var url = "https://merch.amazon.com/api/ng-amazon/coral/com.amazon.gear.merchandiseservice.GearMerchandiseService/GetPublishingEligibility";

var xhr = new XMLHttpRequest();
xhr.open("POST", url);

xhr.setRequestHeader("Connection", "keep-alive");
xhr.setRequestHeader("sec-ch-ua", ""; Not A Brand ";v="
    99 ", "
    Chromium ";v="
    89 ", "
    Google Chrome ";v="
    89 "");
xhr.setRequestHeader("Accept", "application/json, text/plain, */*");
xhr.setRequestHeader("X-CSRF-Token", "goHQSb03YJ11tCpFtuBDLQ40x+b8up31npBkDRUAAAABAAAAAGCGPx5yYXcAAAAAWC9WfMQDvie4v1Ep9rqj");
xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
xhr.setRequestHeader("sec-ch-ua-mobile", "?0");
xhr.setRequestHeader("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36");
xhr.setRequestHeader("Content-Type", "text/plain");
xhr.setRequestHeader("Origin", "https://merch.amazon.com");
xhr.setRequestHeader("Sec-Fetch-Site", "same-origin");
xhr.setRequestHeader("Sec-Fetch-Mode", "cors");
xhr.setRequestHeader("Sec-Fetch-Dest", "empty");
xhr.setRequestHeader("Referer", "https://merch.amazon.com/dashboard");
xhr.setRequestHeader("Cookie", "session-id=133-3683522-5095917; ubid-main=132-8237479-2782856; lc-main=en_US; sid="
    lh4gDu6JrqupFavM3oLhmQ == | N7 / W9WDi3uJqRVNPnSIrVZaS3Cq0l0s0xOS0pls18Xs = "; x-main="
    VghL1P0rDmBu950mlo ? XjebJRTPcsdvz4ebBtg9jiFr ? ZaDqE ? ? BQjLLlo8J75bU "; at-main=Atza|IwEBIIjM2XFDVwmsypJMiEl0TvwNOb33AzohNTwDrh6bfuAQ9AHjHFk9QF-W4W-BSKmEyZdqAG8Aj6znq_0KvfxgWGsqwKgTnI1AzGgQoxk0Xk-4rkvQF1zJ2IzHGZDu-F8WH_772ZCNgzCOx0G7xD2cEAJxozfpf7uuO5qI2j67JJ88dqhfc0c0FDDpS43SWFaLdptpVb_wEIqr8tSZLCQtEU6Pih5GeI3kyulTCzR718MFwYsZjXzup7V6F1gOA5DNODxhsf7V1-QuACm6Ccqbdi0qx4tzf-G2TC1pOEqgASCraQ; sess-at-main="
    rJ4dNkpnubC2EsnnweqeXs7xezJhnC1QDY / A1DARc8A = "; sst-main=Sst1|PQE5xp0Ae-MAAhRWNqfEuzP1CfrihunXksZREIh87SnK4Y2sVA6BOQpSmZWVf7ze_DcYQXgoES8EdKt5LubgatAAdU7IBtSl8eqXtDXuKWlh5eOj_hxHm9JJt4FiuHmFkn8DLwqkmlHiC8EaKATAX6muIvZ16GWjIQB7pwhgBWD8awqi0QQgqARut8lKeaYWij3k7f3b2VWKkv0UlfVRYM9Wuqj32mWclZCVdtAf5-FIrUW2y-FXoikVoJAamum5N2BXkDAWAQnz67AV0jx--h9ihaF68ccjFyR5kwzgXjItnMI; session-id-time=2082787201l; i18n-prefs=USD; merch-language=en_US; csm-hit=tb:6B70176YHDA7RPGZ3JB1+s-9942YJ3BE3FZPF0YTWPX|1619410726874&t:1619410726874&adb:adblk_no; session-token="
    k6sWaJ0ZMsQ0o7REdPsRAg6tJodJHW0221m5xWIf6GmukzqMq6hF94z31XRJ6Ag5qkyE08AwGOLzgqQtL29 + e7XHuiWFpHI5SC1sTexarH1e4IT9mjVD8s44ykw + fUIcFCXZmzDi5OYFdlNcWaI0ZCjjvMD + YKllHtPEayg + 2 d9zzADnhla0KHoxohyiPB / rvBVJV0vmdr + YEdohejoPug == "");

xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
        console.log(xhr.status);
        console.log(xhr.responseText);
    }
};

var data = '{"accountId":"504154114","__type":"com.amazon.gear.merchandiseservice#GetPublishingEligibilityInput"}';

xhr.send(data);