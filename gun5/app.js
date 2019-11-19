 var app = new Vue({
          el: '#kapsayici',
          data: {
            message: 'Hello Vue!',
            mesajim: "merhaba dunya",
            model1 : "",
            messajiGoster: true,
            uyeler: [],
            yapilacaklar: [{yazi: "markete git", yapildiMi: false},
                            {yazi: "ekmek al", yapildiMi: true},
                            {yazi: "benzin al", yapildiMi: false},
                            {yazi: "ödevleri yap", yapildiMi: true}
                            ]
          },
          methods: {
            yapilacakEkle : function(){
                this.yapilacaklar.push({
                    yazi : this.model1,
                    yapildiMi : false
                })

                this.yapilacaklar[1].yazi = "ekmek al 4"
                this.yapilacaklar[1].yapildiMi = false;
                this.message += new Date()
            },
            uyeleriGetir : function(){
                var self = this;
                $.get('https://reqres.in/api/users?page=2',{},function(e){
                    self.uyeler = e.data;
                })
            }
          }
        })
