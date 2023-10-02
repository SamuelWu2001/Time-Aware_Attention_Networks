<template>
<form class="search serchelement">
  <input class="me-4 serchelement" id="PatientInput" style="border-radius:5px;height:46px" type="search" placeholder="PatientID" aria-label="Search">
  <button class="btn btn-outline-success me-2 serchelement" type="submit" @click="processFormData();">Search</button>
  <button class="btn btn-outline-success me-2 serchelement" type="submit" data-bs-toggle="modal" data-bs-target="#add">Add</button>
  <button class="btn btn-outline-success me-3 serchelement" type="submit" data-bs-toggle="modal" data-bs-target="#modify">Update</button>
</form>
<div class="modal fade" id="add">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h3><b>新增病人資料</b></h3>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body">
        <form>
          <div class="form-group">
            <b style="float:left;">PatientID</b>
            <input class="form-control" v-model="Patient.PatientID" placeholder="PatientID">
          </div>
          <div class="form-group">
            <b style="float:left;">Name</b>
            <input class="form-control" v-model="Patient.Name" placeholder="Name">
          </div>
          <div class="form-group">
            <b style="float:left;">Age</b>
            <input class="form-control" v-model="Patient.Age" placeholder="Age">
          </div>
          <div class="form-group">
            <b style="float:left;">Sex</b>
            <input class="form-control" v-model="Patient.Sex" placeholder="Sex">
          </div>
          <div class="form-group">
            <b style="float:left;">Address</b>
            <input class="form-control" v-model="Patient.Address" placeholder="Address">
          </div>
          <div class="form-group">
            <b style="float:left;">hypertension</b>
            <input class="form-control" v-model="Patient.hypertension" placeholder="hypertension">
          </div>
          <div class="form-group">
            <b style="float:left;">cardiovascular</b>
            <input class="form-control" v-model="Patient.cardiovascular" placeholder="cardiovascular">
          </div>
          <div class="form-group">
            <b style="float:left;">diabetes</b>
            <input class="form-control" v-model="Patient.diabetes" placeholder="diabetes">
          </div>
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-info" data-bs-dismiss="modal" @click="submitPatient" style="background: rgb(112, 105, 104);border-style:none;color:white;">送出</button> 
      </div>
    </div>
  </div>
</div>
<div class="modal fade" id="modify">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h3><b>修改病人資料</b></h3>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body">
        <form>
          <div class="form-group">
            <b style="float:left;">PatientID</b>
            <input class="form-control" v-model="Patient.PatientID" placeholder="PatientID">
          </div>
          <div class="form-group">
            <b style="float:left;">Name</b>
            <input class="form-control" v-model="Patient.Name" placeholder="Name">
          </div>
          <div class="form-group">
            <b style="float:left;">Age</b>
            <input class="form-control" v-model="Patient.Age" placeholder="Age">
          </div>
          <div class="form-group">
            <b style="float:left;">Sex</b>
            <input class="form-control" v-model="Patient.Sex" placeholder="Sex">
          </div>
          <div class="form-group">
            <b style="float:left;">Address</b>
            <input class="form-control" v-model="Patient.Address" placeholder="Address">
          </div>
          <div class="form-group">
            <b style="float:left;">hypertension</b>
            <input class="form-control" v-model="Patient.hypertension" placeholder="hypertension">
          </div>
          <div class="form-group">
            <b style="float:left;">cardiovascular</b>
            <input class="form-control" v-model="Patient.cardiovascular" placeholder="cardiovascular">
          </div>
          <div class="form-group">
            <b style="float:left;">diabetes</b>
            <input class="form-control" v-model="Patient.diabetes" placeholder="diabetes">
          </div>
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-info" @click="submitPatient" style="background: rgb(112, 105, 104);border-style:none;color:white;">送出</button> 
      </div>
    </div>
  </div>
</div>
<div style="display: flex;justify-content: center;align-items: center;">
  <div class="P-table shadow-lg" style="width:80%">
  <table class="table table-striped ">
    <thead >
      <tr>
        <th scope="col">PatientID</th>
        <th scope="col">Name</th>
        <th scope="col">Age</th>
        <th scope="col">Sex</th>
      </tr>
    </thead>
    <tbody>
      <tr v-if="show==='true'" v-for="(patient) in [FindPatient(this.pid)]">
        <td>{{patient.PatientID}}</td>
        <td>{{patient.Name}}</td>
        <td>{{patient.Age}}</td>
        <td>{{patient.Sex}}</td>
      </tr>
      <tr v-if="show==='false'" v-for="(patient) in PatientList">
        <td>{{patient.PatientID}}</td>
        <td>{{patient.Name}}</td>
        <td>{{patient.Age}}</td>
        <td>{{patient.Sex}}</td>
      </tr>
    </tbody>
  </table>
  </div>
</div>
</template>

<script>
  import{mapState,mapGetters} from 'vuex';
  import axios from "axios";
  import store from '../../store'
  export default{
    computed:{
      ...mapState({
        PatientList : state=>state.PatientList,
      }),
      ...mapGetters(["FindPatient"]),
    },
    methods:{
      FindPatient(id){
        return this.FindPatient(id)
      },
      processFormData :function() {
        this.$router.push({
          path : `/Patient`,
          query: {
            PatientID : this.pid,
            Date : this.date
          }
        });
        const PatientElement = document.getElementById("PatientInput");
        const Patient = PatientElement.value;
        this.pid = Patient;
        this.show = 'false';
        for(var i=0; i<this.PatientList.length; i++){
          if(this.PatientList[i].PatientID === this.pid){
            this.show = 'true';
            break;
          }
        }
      },
      submitPatient(){
        // console.log(this.Patient);
        store.dispatch("AddPatient", this.Patient);
        axios.post('http://127.0.0.1:5000/api/adddata',
          {
            PatientID : this.Patient.PatientID,
            Name : this.Patient.Name,
            Age : this.Patient.Age,
            Sex : this.Patient.Sex,
            Address : this.Patient.Address,
            hypertension : this.Patient.hypertension,
            cardiovascular : this.Patient.cardiovascular,
            diabetes : this.Patient.diabetes,
          }
        ).catch(function(err) {
            console.error(err);
        });

      },
    },
    data(){
      return{
        pid:'',
        show:'false',
        Patient:{
          PatientID:'',
          Name:'',
          Age:'',
          Sex:'',
          Address:'',
          hypertension:'',
          cardiovascular:'',
          diabetes:'',
        }
      }
    }
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
</style>
