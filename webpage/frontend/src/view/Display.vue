<template>
    <div style="margin-top:10px;">
        <b style="font-size:35px;">SBP Diagram</b>
        <div style="display: flex;justify-content: center;align-items: center;">
            <div class="display-card shadow-lg p-3">
                <line-chart label="Value" :data="SPdata" :min=80 :max=120 :curve="false" ></line-chart>
            </div>
        </div>
    </div>
    <div style="margin-top:10px;">
        <b style="font-size:35px;">DBP Diagram</b>
        <div style="display: flex;justify-content: center;align-items: center;">
            <div class="display-card shadow-lg p-3">
                <line-chart label="Value" :data="DPdata" :min=80 :max=200 :curve="false" ></line-chart>
            </div>
        </div>
    </div>
    <div style="margin-top:10px;">
        <b style="font-size:35px;">HR Diagram</b>
        <div style="display: flex;justify-content: center;align-items: center;">
            <div class="display-card shadow-lg p-3">
                <line-chart label="Value" :data="HRdata" :min=50 :max=150 :curve="false" ></line-chart>
            </div>
        </div>
    </div>
    <div style="margin-top:10px;">
        <b style="font-size:35px;">RR Diagram</b>
        <div style="display: flex;justify-content: center;align-items: center;">
            <div class="display-card shadow-lg p-3">
                <line-chart label="Value" :data="RRdata" :min=0 :max=30 :curve="false" ></line-chart>
            </div>
        </div>
    </div>
            
</template>

<script>
import{mapState,mapGetters} from 'vuex';
export default{
    created(){
        this.processData();
    },
    computed:{
      ...mapState({
        HistoryList : state=>state.HistoryList,
      }),
      ...mapGetters(["FindDataWithID"]),
    },
    methods:{
        FindDataWithID(id,date){
            return this.FindDataWithID(id,date);
        },
        processData :function() {
          console.log(this.date)
          console.log(this.$store.getters.FindDataWithID(this.pid,this.date))
        //   this.sp = this.$store.getters.FindDataWithID(this.pid,this.date).SP;
        //   this.time = this.$store.getters.FindDataWithID(this.pid,this.date).time;
        //   this.ob.one = this.$store.getters.FindDataWithID(this.pid,this.date).one;
        //   this.ob.two = this.$store.getters.FindDataWithID(this.pid,this.date).two;
        //   this.ob.three = this.$store.getters.FindDataWithID(this.pid,this.date).three;
        //   this.ob.four = this.$store.getters.FindDataWithID(this.pid,this.date).four;
        //   console.log(this.ob.one)
          this.SPdata[this.$store.getters.FindDataWithID(this.pid,this.date).one.time] = this.$store.getters.FindDataWithID(this.pid,this.date).one.SP;
          this.SPdata[this.$store.getters.FindDataWithID(this.pid,this.date).two.time] = this.$store.getters.FindDataWithID(this.pid,this.date).two.SP;
          this.SPdata[this.$store.getters.FindDataWithID(this.pid,this.date).three.time] = this.$store.getters.FindDataWithID(this.pid,this.date).three.SP;
          this.SPdata[this.$store.getters.FindDataWithID(this.pid,this.date).four.time] =  this.$store.getters.FindDataWithID(this.pid,this.date).four.SP;
          this.SPdata[this.$store.getters.FindDataWithID(this.pid,this.date).five.time] =  this.$store.getters.FindDataWithID(this.pid,this.date).five.SP;
          this.DPdata[this.$store.getters.FindDataWithID(this.pid,this.date).one.time] = this.$store.getters.FindDataWithID(this.pid,this.date).one.DP;
          this.DPdata[this.$store.getters.FindDataWithID(this.pid,this.date).two.time] = this.$store.getters.FindDataWithID(this.pid,this.date).two.DP;
          this.DPdata[this.$store.getters.FindDataWithID(this.pid,this.date).three.time] = this.$store.getters.FindDataWithID(this.pid,this.date).three.DP;
          this.DPdata[this.$store.getters.FindDataWithID(this.pid,this.date).four.time] =  this.$store.getters.FindDataWithID(this.pid,this.date).four.DP;
          this.DPdata[this.$store.getters.FindDataWithID(this.pid,this.date).five.time] =  this.$store.getters.FindDataWithID(this.pid,this.date).five.DP;
          this.HRdata[this.$store.getters.FindDataWithID(this.pid,this.date).one.time] = this.$store.getters.FindDataWithID(this.pid,this.date).one.HR;
          this.HRdata[this.$store.getters.FindDataWithID(this.pid,this.date).two.time] = this.$store.getters.FindDataWithID(this.pid,this.date).two.HR;
          this.HRdata[this.$store.getters.FindDataWithID(this.pid,this.date).three.time] = this.$store.getters.FindDataWithID(this.pid,this.date).three.HR;
          this.HRdata[this.$store.getters.FindDataWithID(this.pid,this.date).four.time] =  this.$store.getters.FindDataWithID(this.pid,this.date).four.HR;
          this.HRdata[this.$store.getters.FindDataWithID(this.pid,this.date).five.time] =  this.$store.getters.FindDataWithID(this.pid,this.date).five.HR;
          this.RRdata[this.$store.getters.FindDataWithID(this.pid,this.date).one.time] = this.$store.getters.FindDataWithID(this.pid,this.date).one.RR;
          this.RRdata[this.$store.getters.FindDataWithID(this.pid,this.date).two.time] = this.$store.getters.FindDataWithID(this.pid,this.date).two.RR;
          this.RRdata[this.$store.getters.FindDataWithID(this.pid,this.date).three.time] = this.$store.getters.FindDataWithID(this.pid,this.date).three.RR;
          this.RRdata[this.$store.getters.FindDataWithID(this.pid,this.date).four.time] =  this.$store.getters.FindDataWithID(this.pid,this.date).four.RR;
          this.RRdata[this.$store.getters.FindDataWithID(this.pid,this.date).five.time] =  this.$store.getters.FindDataWithID(this.pid,this.date).five.RR;
        //  console.log('chartdata',this.chartdata) 
        //   for(var i=0; i<this.HistoryList.length; i++){
        //     if((this.HistoryList[i].PatientID === this.pid) && (this.HistoryList[i].Date === this.date)){
        //       this.show = 'true';
        //       break;
        //     }
        //   }
        },
        show : function(){
        console.log(this.$route.query);
        }
    },
    data(){
      return{
        pid : this.$route.query.PatientID,
        date : this.$route.query.Date,
        // time : '',
        // sp : 0,
        SPdata:{},
        DPdata:{},
        HRdata:{},
        RRdata:{},
        // ob :{
        //   one :{
        //     time:'',
        //     predict : false,
        //     dangerous : false,
        //     sp: 0,
        //   },
        //   two :{
        //     time:'',
        //     predict : false,
        //     dangerous : false,
        //     sp: 0,
        //   },
        //   three :{
        //     time:'',
        //     predict : false,
        //     dangerous : false,
        //     sp: 0,
        //   },
        //   four :{
        //     time:'',
        //     predict : false,
        //     dangerous : false,
        //     sp: 0,
        //   }
        // },
      }
    },
}
</script>
<style>
    .display-card{
    display:flex;
    flex-wrap:wrap;
    border-style:none;
    justify-content: center;
    border-radius: 20px;
    background: rgb(196, 215, 215);
    margin:30px;
    margin-right: 60px;
    margin-left: 60px;
    width:75%;
}
</style>