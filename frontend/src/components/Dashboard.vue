<template>
    <div class="dashboard">
      <h2>Patient Dashboard</h2>
      <ul>
        <li v-for="patient in patients" :key="patient.Patient_ID">
          <router-link :to="{ name: 'PatientProfile', params: { id: patient.Patient_ID } }">
            {{ patient.Name }}
          </router-link>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'Dashboard',
    data() {
      return {
        patients: [],
      };
    },
    created() {
      axios.get('http://localhost:5000/patients')
        .then(response => {
          this.patients = response.data;
        })
        .catch(error => {
          console.error('Error loading patients:', error);
        });
    },
  };
  </script>
  
  <style scoped>
  .dashboard {
    padding: 20px;
  }
  
  h2 {
    color: #18646c;
    font-weight: 700;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    margin: 10px 0;
  }
  </style>
  