import Vuex from 'vuex'
 
export default new Vuex.Store({
  state: { 
    PatientList:[],
    // PatientList:[
    //     {
    //         PatientID:'65535',
    //         Name: '王大明',
    //         Age:'54',
    //         Sex:'Male',
    //         Address:'台南市東區大學路22號',
    //     },
    //     {
    //         PatientID:'1072980',
    //         Name: '陳小美',
    //         Age:'48',
    //         Sex:'Female',
    //         Address:'台南市南區中華路108號',
    //     },
    //     {
    //         PatientID:'2170850',
    //         Name: '楊小龍',
    //         Age: '62',
    //         Sex:'Male',
    //         Address:'台南市永康區民族路87號',
    //     },
    // ],
    HistoryList :[],
    // HistoryList:[
    //   {
    //     PatientID:'65535',
    //     BedID:'A1' ,
    //     Date: '2022/05/01',
    //     one :{
    //         time : '08:16',
    //         predict : false,
    //         correct : true,
    //         SP : 98,
    //         DP : 161,
    //         HR : 99,
    //         RR : 20
    //     },
    //     two :{
    //         time : '09:23',
    //         predict : false,
    //         correct : false,
    //         SP : 103,
    //         DP : 166,
    //         HR : 81,
    //         RR : 20
    //     },
    //     three :{
    //         time : '10:27',
    //         predict : true,
    //         correct : true,
    //         SP : 87,
    //         DP : 166,
    //         HR : 81,
    //         RR : 20
    //     },
    //     four :{
    //         time : '11:20',
    //         predict : false,
    //         correct : true,
    //         SP : 82,
    //         DP : 168,
    //         HR : 82,
    //         RR : 20
    //     },
    //     five :{
    //         time : '12:06',
    //         SP : 91,
    //         DP : 158,
    //         HR : 80,
    //         RR : 20
    //     },
    //   },
    //   {
    //     PatientID:'123456',
    //     BedID:'A2' ,
    //     Date: '2022/05/01',
    //     one :{
    //         time : '09:16',
    //         predict : false,
    //         correct : true,
    //         SP : 92,
    //         DP : 166,
    //         HR : 72,
    //         RR : 18
    //     },
    //     two :{
    //         time : '10:47',
    //         predict : true,
    //         correct : true,
    //         SP : 100,
    //         DP : 154,
    //         HR : 72,
    //         RR : 16
    //     },
    //     three :{
    //         time : '11:25',
    //         predict : true,
    //         correct : false,
    //         SP : 88,
    //         DP : 164,
    //         HR : 70,
    //         RR : 20
    //     },
    //     four :{
    //         time : '12:20',
    //         predict : false,
    //         correct : true,
    //         SP : 98,
    //         DP : 190,
    //         HR : 68,
    //         RR : 20
    //     },
    //     five :{
    //         time: '13:26',
    //         SP: 105,
    //         DP : 184,
    //         HR : 69,
    //         RR : 17
    //     },
    //   },
    //   {
    //     PatientID:'987654',
    //     BedID:'A3' ,
    //     Date: '2022/05/01',
    //     one :{
    //         time : '08:45',
    //         predict : false,
    //         correct : true,
    //         SP : 110,
    //         DP : 158,
    //         HR : 69,
    //         RR : 15
    //     },
    //     two :{
    //         time : '09:37',
    //         predict : false,
    //         correct : true,
    //         SP : 112,
    //         DP : 151,
    //         HR : 63,
    //         RR : 14
    //     },
    //     three :{
    //         time : '10:58',
    //         predict : false,
    //         correct : true,
    //         SP : 111,
    //         DP : 144,
    //         HR : 70,
    //         RR : 15
    //     },
    //     four :{
    //         time : '11:40',
    //         predict : false,
    //         correct : true,
    //         SP : 98,
    //         DP : 137,
    //         HR : 69,
    //         RR : 18
    //     },
    //     five :{
    //         time: '12:26',
    //         SP: 95,
    //         DP : 154,
    //         HR : 70,
    //         RR : 18
    //     }
    //   },
    //   {
    //     PatientID:'134679',
    //     BedID:'A4' ,
    //     Date: '2022/05/01',
    //     one :{
    //         time : '09:16',
    //         predict : false,
    //         correct : false,
    //         SP : 95,
    //         DP : 151,
    //         HR : 84,
    //         RR : 16
    //     },
    //     two :{
    //         time : '10:33',
    //         predict : true,
    //         correct : true,
    //         SP : 85,
    //         DP : 147,
    //         HR : 76,
    //         RR : 20
    //     },
    //     three :{
    //         time : '11:56',
    //         predict : true,
    //         correct : true,
    //         SP : 86,
    //         DP : 122,
    //         HR : 90,
    //         RR : 20
    //     },
    //     four :{
    //         time : '12:43',
    //         predict : false,
    //         correct : true,
    //         SP : 82,
    //         DP : 127,
    //         HR : 84,
    //         RR : 16
    //     },
    //     five :{   
    //         time: '13:28',
    //         SP: 105,
    //         DP : 133,
    //         HR : 82,
    //         RR : 20
    //     }
    //   },
    // ],
  },
  mutations: {
    AddPatient(state, Patient) {
        state.PatientList.push(Patient);
    },
    LoadPatient(state, Patient) {
      state.PatientList = Patient;
    },
    LoadHistory(state, History) {
        state.HistoryList = History;
    },
  },
  actions: {
    AddPatient({commit},data){
        commit('AddPatient',data);
    },
    LoadPatient({commit},data){
      commit('LoadPatient',data);
    },
    LoadHistory({commit},data){
        commit('LoadHistory',data);
    },
  },
  getters: {
      FindPatient:state=>(id)=>{
          return state.PatientList.find(PatientList=>PatientList.PatientID===id)
      },
      FindData:state=>(date)=>{
        return state.HistoryList.filter(HistoryList=>HistoryList.Date===date)
      },
      FindDataWithID:state=>(id,date)=>{
        return state.HistoryList.find(HistoryList=>((HistoryList.PatientID===id)&&(HistoryList.Date===date)))
      },
  }
});





