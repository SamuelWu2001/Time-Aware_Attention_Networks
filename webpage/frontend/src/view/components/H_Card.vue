<template>
<form class="search serchelement" >
  <!-- <input class="me-4 serchelement" id="PatientID" style="border-radius:5px;height:46px;" type="search" placeholder="PatientID" aria-label="Search"> -->
  <input class="me-4 serchelement" id="Date" style="border-radius:5px;height:46px" aria-label="Search" type="date">
  <button class="btn btn-outline-success me-2 serchelement" type="submit" @click="processFormData();">Search</button>
  <button class="btn btn-outline-success me-2 serchelement" @click="history_display" >start</button>
  <button class="btn btn-outline-success me-2 serchelement" data-bs-toggle="modal" data-bs-target="#result">result</button>
</form>
<div class="modal fade" id="result">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header">
        <h3><b>Result</b></h3>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body" style="font-size:20px;">
        <div style="height:50px;display:flex;">
          <b style="flex:1;">Bed ID</b>
          <b style="flex:1;">Parient ID</b>
          <b style="flex:1;">1</b>
          <b style="flex:1;">2</b>
          <b style="flex:1;">3</b>
          <b style="flex:1;">4</b>
        </div>
        <div style="height:50px;display:flex;" v-for="(data) in FindData(this.date)">
          <b style="flex:1;margin:5px;">{{data.BedID}}</b>
          <b style="flex:1;margin:5px;">{{data.PatientID}}</b>
          <div style="flex:1;margin:5px;" v-if="data.one.correct===true">
            <div style="border-radius:10px;background:rgb(106, 235, 59);padding:1px;color:black;">
              correct
            </div>
          </div>
          <div style="flex:1;margin:5px;" v-else>
            <div style="border-radius:10px;background:rgb(250, 41, 22);padding:1px;color:black;">
              false
            </div>
          </div>
          <div style="flex:1;margin:5px;" v-if="data.two.correct===true">
            <div style="border-radius:10px;background:rgb(106, 235, 59);padding:1px;color:black;">
              correct
            </div>
          </div>        
          <div style="flex:1;margin:5px;" v-else>
            <div style="border-radius:10px;background:rgb(250, 41, 22);padding:1px;color:black;">
              false
            </div>
          </div>
          <div style="flex:1;margin:5px;" v-if="data.three.correct===true">
            <div style="border-radius:10px;background:rgb(106, 235, 59);padding:1px;color:black;">
              correct
            </div>
          </div> 
          <div style="flex:1;margin:5px;" v-else>
            <div style="border-radius:10px;background:rgb(250, 41, 22);padding:1px;color:black;">
              false
            </div>
          </div>
          <div style="flex:1;margin:5px;" v-if="data.four.correct===true">
            <div style="border-radius:10px;background:rgb(106, 235, 59);padding:1px;color:black;">
              correct
            </div>
          </div> 
          <div style="flex:1;margin:5px;" v-else>
            <div style="border-radius:10px;background:rgb(250, 41, 22);padding:1px;color:black;">
              false
            </div>
          </div>
        </div>
        <div style="margin-top:20px;margin-down:10px;">
          <b>總計 : 正確 {{correct}} 錯誤 {{error}} </b>
        </div>
      </div>
    </div>
  </div>
</div>
<div class="modal fade" id="map">
  <div class="modal-dialog modal-xl">
    <div class="modal-content">
      <div class="modal-header">
        <h1><b>Map</b></h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body" style="font-size:20px;">
        <img  v-show="bed_id==='A1'" src="../../assets/A1.png" style="width:100%">
        <img  v-show="bed_id==='A2'" src="../../assets/A2.png" style="width:100%">
        <img  v-show="bed_id==='A3'" src="../../assets/A3.png" style="width:100%">
        <img  v-show="bed_id==='A4'" src="../../assets/A4.png" style="width:100%">
      </div>
    </div>
  </div>
</div>



<div v-for="(data) in FindData(this.date)" v-show="show==='true'" style="display: flex;justify-content: center;align-items: center;"> 
  <div style="width:78%;">
  <div class="progress" style="margin-right: 70px; margin-left: 70px; height:30px;;">
    <div class="progress-bar progress-bar-striped progress-bar-animated" v-if="display>=1 && data.one.predict===false" role="progressbar" style="width: 25%; background-color:rgb(82, 227, 84);"></div>
    <div class="progress-bar progress-bar-striped progress-bar-animated" v-if="display>=1 && data.one.predict===true" role="progressbar" style="width: 25%; background-color:rgb(255,184,5);"></div>
    <div class="progress-bar progress-bar-striped progress-bar-animated" v-if="display>=2 && data.two.predict===false" role="progressbar" style="width: 25%; background-color:rgb(82, 227, 84);"></div>
    <div class="progress-bar progress-bar-striped progress-bar-animated" v-if="display>=2 && data.two.predict===true" role="progressbar" style="width: 25%; background-color:rgb(255,184,5);"></div>
    <div class="progress-bar progress-bar-striped progress-bar-animated" v-if="display>=3 && data.three.predict===false" role="progressbar" style="width: 25%; background-color:rgb(82, 227, 84);"></div>
    <div class="progress-bar progress-bar-striped progress-bar-animated" v-if="display>=3 && data.three.predict===true" role="progressbar" style="width: 25%; background-color:rgb(255,184,5);"></div>
    <div class="progress-bar progress-bar-striped progress-bar-animated" v-if="display>=4 && data.four.predict===false" role="progressbar" style="width: 25%; background-color:rgb(82, 227, 84);"></div>
    <div class="progress-bar progress-bar-striped progress-bar-animated" v-if="display>=4 && data.four.predict===true" role="progressbar" style="width: 25%; background-color:rgb(255,184,5);"></div> 
  </div>
  <div class="history-card shadow-lg p-3" >  
    <div style="text-align:left; margin:10px; font-size:18px;">
      <button @click="decidebedid(data.BedID)" data-bs-toggle="modal" data-bs-target="#map" style="font-weight:bolder;margin-right:10px;border-radius:10px;background:rgb(118, 161, 73);padding:6px;color:rgb(218, 233, 187);border:None;">Bed ID : {{data.BedID}}</button> 
      <b style="margin-right:10px;border-radius:10px;background:rgb(107, 168, 199);padding:10px;margin-left:10px;color:rgb(200, 229, 240)">Patient ID : {{data.PatientID}}</b> 
      <b style="margin-right:10px;border-radius:10px;background:rgb(110, 179, 173);padding:10px;margin-left:10px;color:rgb(212, 241, 236)">End Time : {{data.five.time}}</b> 
      <button style="float:right;border-radius:10px;font-size:18px;" class="h-button" @click="display_info(data.PatientID)" >See more</button>
    </div>
    <div style="display:flex;">
      <div class="card p-card" v-if="display<1">
        <div class="card-body" style="padding-down:10px;margin:5px;display:flex;background:rgb(255,255,255);border-radius:15px;height:100px;">
            <h5 class="card-title" style="font-size:25px"><b>waiting</b></h5>
        </div>
      </div>
      <div class="card p-card" v-else-if="data.one.predict===true">
        <div class="card-body" style="padding-down:10px;margin:5px;display:flex;background:rgb(255,184,5);border-radius:15px">
          <img src="../../assets/notice.png" class="card-img-top" style="flex:1;height:75px;">
          <div style="flex:2;">
            <h5 class="card-title" style="font-size:25px"><b>{{data.one.time}}</b></h5>
            <h5 class="card-title" style="font-size:25px"><b>{{data.one.DP}}/{{data.one.SP}}</b></h5>
          </div>
        </div>
      </div>
      <div class="card p-card" v-else>
        <div class="card-body" style="padding-down:10px;margin:5px;display:flex;background:rgb(82, 227, 84);border-radius:15px">
          <img src="../../assets/safe.png" class="card-img-top" style="flex:1; height:75px;">
          <div style="flex:2;">
            <h5 class="card-title" style="font-size:25px"><b>{{data.one.time}}</b></h5>
            <h5 class="card-title" style="font-size:25px"><b>{{data.one.DP}}/{{data.one.SP}}</b></h5>
          </div>
        </div>
      </div>
      <div class="card p-card" v-if="display<2">
        <div class="card-body" style="padding-down:10px;margin:5px;display:flex;background:rgb(255,255,255);border-radius:15px;height:100px;">
            <h5 class="card-title" style="font-size:25px"><b>waiting</b></h5>
        </div>
      </div>
      <div class="card p-card" v-else-if="data.two.predict===true">
        <div class="card-body" style="padding-down:10px;margin:5px;display:flex;background:rgb(255,184,5);border-radius:15px">
          <img src="../../assets/notice.png" class="card-img-top" style="flex:1;height:75px;">
          <div style="flex:2;">
            <h5 class="card-title" style="font-size:25px"><b>{{data.two.time}}</b></h5>
            <h5 class="card-title" style="font-size:25px"><b>{{data.two.DP}}/{{data.two.SP}}</b></h5>
          </div>
        </div>
      </div>
      <div class="card p-card" v-else>
        <div class="card-body" style="padding-down:10px;margin:5px;display:flex;background:rgb(82, 227, 84);border-radius:15px">
          <img src="../../assets/safe.png" class="card-img-top" style="flex:1; height:75px;">
          <div style="flex:2;">
            <h5 class="card-title" style="font-size:25px"><b>{{data.two.time}}</b></h5>
            <h5 class="card-title" style="font-size:25px"><b>{{data.two.DP}}/{{data.two.SP}}</b></h5>
          </div>
        </div>
      </div>
      <div class="card p-card" v-if="display<3">
        <div class="card-body" style="padding-down:10px;margin:5px;display:flex;background:rgb(255,255,255);border-radius:15px;height:100px;">
            <h5 class="card-title" style="font-size:25px"><b>waiting</b></h5>
        </div>
      </div>
      <div class="card p-card" v-else-if="data.three.predict===true">
        <div class="card-body" style="padding-down:10px;margin:5px;display:flex;background:rgb(255,184,5);border-radius:15px">
          <img src="../../assets/notice.png" class="card-img-top" style="flex:1;height:75px;">
          <div style="flex:2;">
            <h5 class="card-title" style="font-size:25px"><b>{{data.three.time}}</b></h5>
            <h5 class="card-title" style="font-size:25px"><b>{{data.three.DP}}/{{data.three.SP}}</b></h5>
          </div>
        </div>
      </div>
      <div class="card p-card" v-else>
        <div class="card-body" style="padding-down:10px;margin:5px;display:flex;background:rgb(82, 227, 84);border-radius:15px">
          <img src="../../assets/safe.png" class="card-img-top" style="flex:1; height:75px;">
          <div style="flex:2;">
            <h5 class="card-title" style="font-size:25px"><b>{{data.three.time}}</b></h5>
            <h5 class="card-title" style="font-size:25px"><b>{{data.three.DP}}/{{data.three.SP}}</b></h5>
          </div>
        </div>
      </div>
      <div class="card p-card" v-if="display<4">
        <div class="card-body" style="padding-down:10px;margin:5px;display:flex;background:rgb(255,255,255);border-radius:15px;height:100px;">
            <h5 class="card-title" style="font-size:25px"><b>waiting</b></h5>
        </div>
      </div>
      <div class="card p-card" v-else-if="data.four.predict===true">
        <div class="card-body" style="padding-down:10px;margin:5px;display:flex;background:rgb(255,184,5);border-radius:15px">
          <img src="../../assets/notice.png" class="card-img-top" style="flex:1;height:75px;">
          <div style="flex:2;">
            <h5 class="card-title" style="font-size:25px"><b>{{data.four.time}}</b></h5>
            <h5 class="card-title" style="font-size:25px"><b>{{data.four.DP}}/{{data.four.SP}}</b></h5>
          </div>
        </div>
      </div>
      <div class="card p-card" v-else>
        <div class="card-body" style="padding-down:10px;margin:5px;display:flex;background:rgb(82, 227, 84);border-radius:15px;">
          <img src="../../assets/safe.png" class="card-img-top" style="flex:1; height:75px;">
          <div style="flex:2;">
            <h5 class="card-title" style="font-size:25px"><b>{{data.four.time}}</b></h5>
            <h5 class="card-title" style="font-size:25px"><b>{{data.four.DP}}/{{data.four.SP}}</b></h5>
          </div>
        </div>
      </div>
    </div>
  </div>
  </div>
</div> 
</template>

<script>
  import{mapState,mapGetters} from 'vuex';
  import axios from 'axios';
  import store from '../../store'
  export default{
    created(){
      if(this.$route.query.Date!= null){
        console.log('this.$route.query.Date,',this.$route.query.Date);
        this.date = this.$route.query.Date;
        this.show = 'false';
        if(this.$route.query.Display!= null)
        this.display = this.$route.query.Display;
        for(var i=0; i<this.HistoryList.length; i++){
          if(this.HistoryList[i].Date === this.date){
            this.show = 'true';
            break;
          }
        }
        for(var i=0; i<this.HistoryList.length; i++){
          if(this.HistoryList[i].Date === this.date){
            if(this.HistoryList[i].one.correct===true){
              this.correct++;
            }else{
              this.error++;
            }
            if(this.HistoryList[i].two.correct===true){
              this.correct++;
            }else{
              this.error++;
            }
            if(this.HistoryList[i].three.correct===true){
              this.correct++;
            }else{
              this.error++;
            }
            if(this.HistoryList[i].four.correct===true){
              this.correct++;
            }else{
              this.error++;
            }
          }
        }
      }
    },
    computed:{
      ...mapState({
        HistoryList : state=>state.HistoryList,
      }),
      ...mapGetters(["FindData"]),
    },
    methods:{
      FindData(id,date){
        return this.FindData(id,date);
      },
      decidebedid :function(id){
        this.bed_id = id;
      },
      processFormData :function() {
        const DateElement = document.getElementById("Date");
        const Date = DateElement.value;
        this.date = Date.replace(/-/g,'/');
        this.$router.push({
          path : `/History`,
          query: {
            Date : this.date,
          }
        });
        // axios.get('http://127.0.0.1:5000/api/getdata',{
        //   params:{
        //     PatientID : this.pid,
        //     Date : this.date,
        //   }
        // }).then((res)=>{
        //   console.log('資料 : ',res.data)
        //   store.dispatch("UpDateHistory", res.data);
        //   this.SP = res.data.SP;
        //   this.time = res.data.time;
        //   this.ob.one = res.data.one;
        //   this.ob.two = res.data.two;
        //   this.ob.three = res.data.three;
        //   this.ob.four = res.data.four;
        // });
        console.log(this.date)
        console.log(this.$store.getters.FindData(this.date))
        // this.SP = this.$store.getters.FindData(this.date).SP;
        // this.time = this.$store.getters.FindData(this.date).time;
        // this.ob.one = this.$store.getters.FindData(this.date).one;
        // this.ob.two = this.$store.getters.FindData(this.date).two;
        // this.ob.three = this.$store.getters.FindData(this.date).three;
        // this.ob.four = this.$store.getters.FindData(this.date).four;
        // console.log(this.ob.one)
        
        this.show = 'false';
        this.display = 0;
        this.correct = 0;
        this.error = 0;
        for(var i=0; i<this.HistoryList.length; i++){
          if(this.HistoryList[i].Date === this.date){
            this.show = 'true';
            break;
          }
        }
        for(var i=0; i<this.HistoryList.length; i++){
          if(this.HistoryList[i].Date === this.date){
            if(this.HistoryList[i].one.correct===true){
              this.correct++;
            }else{
              this.error++;
            }
            if(this.HistoryList[i].two.correct===true){
              this.correct++;
            }else{
              this.error++;
            }
            if(this.HistoryList[i].three.correct===true){
              this.correct++;
            }else{
              this.error++;
            }
            if(this.HistoryList[i].four.correct===true){
              this.correct++;
            }else{
              this.error++;
            }
          }
        }
      },
      display_info :function(pid) {
        this.$router.push({
          path : `/Display`,
          query: {
            Date : this.date,
            PatientID : pid,
          }
        });
      },
      history_display :function() {
        var count = 0;
        let _this = this;
        _this.display=0;
        _this.$router.push({
          path : `/History`,
          query: {
            Date : _this.date,
            Display : 4,
          }
        });
        var intervalID = setInterval(function(){
          // console.log();
          switch(count){
            case 0:
              _this.display=1;
              console.log(_this.display);
              break;
            case 1:
              _this.display=2;
              console.log(_this.display);
              break;
            case 2:
              _this.display=3;
              console.log(_this.display);
              break;
            case 3:
              _this.display=4;
              console.log(_this.display);
              break;
          }
          if(count==4){
            window.clearInterval(intervalID);
          }
          count++;
        },3000);
      }
    },
    data(){
      return{
        bed_id:'map',
        // date:'',
        // show:'false',
        // time : '',
        display: 0,
        correct: 0,
        error: 0,
        // predict : false,
        // dangerous : false,
        // SP : '',
        // dangerous : false,
        // ob :{
        //   one :{
        //     time:'',
        //     predict : false,
        //     dangerous : false,
        //     SP: '',
        //   },
        //   two :{
        //     time:'',
        //     predict : false,
        //     dangerous : false,
        //     SP: '',
        //   },
        //   three :{
        //     time:'',
        //     predict : false,
        //     dangerous : false,
        //     SP: '',
        //   },
        //   four :{
        //     time:'',
        //     predict : false,
        //     dangerous : false,
        //     SP: '',
        //   }
        // }
      }
    },
  }
</script>


<style>
.table{
    font-size:25px;
}
.P-table{
    margin:30px;
    margin-left: 50px;
    margin-right: 50px;
    border-style: solid;
    border-radius: 20px;
}
.search{
    margin:30px;
    margin-left: 50px;
    margin-right: 50px;
    border-style: none;
    border-radius: 10px;
    height:70px;
    background: white;
}
.serchelement{
    position: relative;
    top:7px;
    font-size: 22px;
}

.history-card{
    flex-wrap:wrap;
    border-style:none;
    border-radius: 20px;
    background: rgb(218, 215, 215);
    margin:30px;
    margin-right: 60px;
    margin-left: 60px;
}

button:active{
  background-color: rgb(198, 158, 236) !important
}

.p-card{
  border-style:none;
  flex: 1;
  background: rgb(218, 215, 215);
}

.h-button{
  background:white;
  border-style:groove;
  color:black;
  box-shadow: 2px;
}

</style>


