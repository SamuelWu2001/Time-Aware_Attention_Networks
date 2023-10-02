<template>
<div>
  <div style="display: flex;justify-content: center;align-items: center;">
    <div style="display: flex;width:80%;border-style:double;margin:30px;">
      <div style="flex:4;font-size:25px;text-align: left;padding:25px;padding-left: 50px;"> 
        <b> Sample Data  </b>
        <br>
        <button style="margin:10px;border-radius:5px;background:beige;" @click="getFile1"> 樣本一 </button>
        <button style="margin:10px;border-radius:5px;background: beige;" @click="getFile2"> 樣本二 </button>
      </div>
      <div style="flex:8;">
        <div class="mb-3" style="padding-top: 50px;display:flex;">
          <input class="form-control" type="file" id="formFile" @change="select_file">
          <button @click="submit_predict_data" style="margin-left:20px;margin-right:20px;border-radius: 5px;background: blanchedalmond;"> Upload </button>
        </div>
      </div>
    </div> 
  </div>
    <div v-show="predict===0" style="display: flex;justify-content: center;align-items: center;">
      <div style="font-size:25px;width:40%;background:lavenderblush;padding:30px;border-radius: 20px;">
        <div style="text-align:left;margin:5px;font-weight:bold;font-size:30px;"> 
          Example :
        </div>
        病歷號 : 65301
        <br>
        體重 : 80 (kg)
        <br>
        透析日期 : 2021/12/05
        <br>
        透析時間 : 08:25
        <br>
        舒張壓 : 100
        <br>
        收縮壓 : 150
        <br>
        心跳 : 70
        <br>
        呼吸頻率 : 22
        <br>
        透析血流溫度 : 35
        <br>
        血流速度 : 30
      </div>
    </div>
    <div v-show="predict===1" style="display: flex;justify-content: center;align-items: center;margin:50px;">
        <div class="shadow-lg" style="width:75%;background:rgb(235, 225, 225);border-radius:20px">
          <div v-if="result===''" style="display: flex;flex-wrap:wrap;justify-content: center;align-items: center;">
              <b style="font-size:50px;width:100%;padding-top:50px;">{{title}}</b>
              <div ref="load" :key="option" style="width:500px;height:500px;"></div>
          </div>
          <div v-else-if="result===false" style="display: flex;flex-wrap:wrap;justify-content: center;align-items: center;">
              <b style="font-size:50px;width:100%;padding-top:50px;">Result : Safe</b>
              <img src="../assets/safe.png" style="width:400px;height:400px;">
          </div>
          <div v-else style="display: flex;flex-wrap:wrap;justify-content: center;align-items: center;">
              <b style="font-size:50px;width:100%;padding-top:50px;">Result : Danger</b>
              <div style="display:flex;"> 
                <div style="flex:1;"> 
                  <img src="../assets/notice.png" style="width:100%;">
                </div>
                <div style="flex:1;font-size:50px;padding-top:50px;"> 72% </div>
              </div>
          </div>
          <button @click="Return" style="font-size:25px;float:right;border-radius:10px;margin-bottom:30px;margin-right:30px;">return</button>
        </div>
    </div>
</div>
</template>
<script >
  import axios from "axios";
  import * as echarts from "echarts"
  export default {
    mounted () {
      // 两张引入方式都可以，这里我用ref,注意一定要节点 初始化完成
      this.myChart = echarts.init(this.$refs.load)
      this.myChart.setOption(this.option)
    },
    data(){
        return{
            predict : 0,
            result : '',
            myChart: null,
            title:'Loading',
            upload_file:null,
            predictdata:{
              PatientID:'',
              weight:'',
              date:'',
              time:'',
              SP:'',
              DP:'',
              HR:'',
              RR:'',
              BT:'',
              BR:'',
              UF:'',
            },
            option : {
              color: ['#fc8251', '#C0C0C0'],
              series: [
                {
                  type: 'pie',
                  label: {
                    normal: {
                       position: 'inner',
                       show : false
                    }
                  },
                  data: [
                    {
                      value: 0,
                    },
                    {
                      value: 6,
                    }
                  ],
                  radius: ['40%', '70%']
                }
              ]
            },
        }
    },
    methods:{
        Return(){
            location.reload();
        },
        select_file(event){
            this.upload_file = event.target.files[0];
            console.log(this.upload_file);
        },
        getFile1: function () {
          const config = {
            method: 'get',
            url: 'http://127.0.0.1:5000/api/download',
            params:{
              file : 1,
            },
            responseType: 'blob'
          };
          axios(config).then(response => {
            console.log(response.data);
            const url = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', 'positive.json');
            document.body.appendChild(link);
            link.click();
          });
        },
        getFile2: function () {
          const config = {
            method: 'get',
            url: 'http://127.0.0.1:5000/api/download',
            params:{
              file : 0,
            },
            responseType: 'blob'
          };
          axios(config).then(response => {
            console.log(response.data);
            const url = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', 'negative.json');
            document.body.appendChild(link);
            link.click();
          });
        },
        submit_predict_data(){
        const fd = new FormData();
        fd.append("json",this.upload_file,this.upload_file.name)
        axios.post('http://127.0.0.1:5000/api/predictdata',fd,
          ).then((res)=>{
              console.log('res',res);
              if(res.data==='error'){
                alert('Patient not found');
              }
              if(res.data==='ok'){
                  this.predict = 1;
                  var count = 0;
                  let _this = this;
                  var intervalID = setInterval(function(){
                    console.log(_this.option.series);
                    switch(count){
                      case 0:
                        _this.title = 'Loading';
                        _this.option.series[0].data[0].value=0;
                        _this.option.series[0].data[1].value=6;
                        console.log(_this.option.series[0].data[0].value);
                        _this.myChart.setOption(_this.option);
                        break;
                      case 1:
                        _this.title = 'Loading.';
                        _this.option.series[0].data[0].value=1;
                        _this.option.series[0].data[1].value=5;
                        console.log(_this.option.series[0].data[0].value);
                        _this.myChart.setOption(_this.option);
                        break;
                      case 2:
                        _this.title = 'Loading..';
                        _this.option.series[0].data[0].value=2;
                        _this.option.series[0].data[1].value=4;
                        console.log(_this.option.series[0].data[0].value);
                        _this.myChart.setOption(_this.option);
                        break;
                      case 3:
                        _this.title = 'Loading...';
                        _this.option.series[0].data[0].value=3;
                        _this.option.series[0].data[1].value=3;
                        console.log(_this.option.series[0].data[0].value);
                        _this.myChart.setOption(_this.option);
                        break;
                      case 4:
                        _this.title = 'Loading.';
                        _this.option.series[0].data[0].value=4;
                        _this.option.series[0].data[1].value=2;
                        console.log(_this.option.series[0].data[0].value);
                        _this.myChart.setOption(_this.option);
                        break;
                      case 5:
                        _this.title = 'Loading..';
                        _this.option.series[0].data[0].value=5;
                        _this.option.series[0].data[1].value=1;
                        console.log(_this.option.series[0].data[0].value);
                        _this.myChart.setOption(_this.option);
                        break;
                      case 6:
                        _this.title = 'Loading...';
                        _this.option.series[0].data[0].value=6;
                        _this.option.series[0].data[1].value=0;
                        console.log(_this.option.series[0].data[0].value);
                        _this.myChart.setOption(_this.option);
                        break;
                    }
                    if(count==7){
                      window.clearInterval(intervalID);
                      axios.get('http://127.0.0.1:5000/api/getresult',{
                        }).then((res)=>{
                          console.log(res.data);
                          
                          _this.result = res.data[1];
                          console.log(_this.result);
                        });
                    }
                    count++;
                  },1000);
              }
          }).catch(function(err) {
              console.error(err);
          });
        }
    }
  }
</script>


<style >
.upload{
    border-style:none;
    justify-content: center;
    border-radius: 20px;
    background: rgb(235, 225, 225);
    margin:30px;
    margin-right: 60px;
    margin-left: 60px;
}
.forminput{
    width:100%;
    margin-left:50px;
    font-size: 24px;
}
</style>