import json

data = {
    "Gruppa":
    [
        {
        "FIO": "Podrezov N.S.",
        "adress":
         {
        "country": "Russia",
        "City": "Bataysk"
         },
         "contacts":
         {
          "vk": "vk.com/1234654",
          "Twitter": "twitter/12313214"
         },
          "phonenumber":
              [
              "8 800 555 35 35",
              "8 965 324 32 12"
              ],
            "primechanie": "adsaxcz"
        },
        {
        "FIO": "Myrzin A.M.",
        "adress":
         {
        "country": "Russia",
        "City": "Feodosia"
         },
         "contacts":
         {
          "vk": "vk.com/1234655",
          "Twitter": "twitter/12323434"
         },
          "phonenumber":
              [
              "8 332 132 32 41",
              "8 965 324 32 12"
              ],
            "primechanie": "fasdasw"
         }
  ]
}
with open('result1.json', 'w') as outfile:
    json.dump(data, outfile)