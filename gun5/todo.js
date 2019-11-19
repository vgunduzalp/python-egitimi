 var app = new Vue({
      el: '#app',
      data: {
        gorev: '',
        tamamlanmayanGorevList: [],
        tamamlananGorevList: []
      },
      methods: {
        gorevEkle: function(){

            this.tamamlanmayanGorevList.push({
                yazi: this.gorev,
                tamamlandiMi: false
            })

            this.gorev = "";
        },
        tamamlandi: function(item){

            index = this.tamamlanmayanGorevList.indexOf(item);
            this.tamamlanmayanGorevList.splice(index);
            item.tamamlandiMi = true;
            this.tamamlananGorevList.push(item);

        },
        tamamlanmadi : function(item){
                index = this.tamamlananGorevList.indexOf(item);
                this.tamamlananGorevList.splice(index);
                item.tamamlandiMi = false;
                this.tamamlanmayanGorevList.push(item);
        },

        sil : function(item, tamamlandiMi){
            if(tamamlandiMi){
                index = this.tamamlananGorevList.indexOf(item);
                this.tamamlananGorevList.splice(index);
            }else{
                index = this.tamamlanmayanGorevList.indexOf(item);
                this.tamamlanmayanGorevList.splice(index);
            }
        }


      }


 })
