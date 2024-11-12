<template>
    <div class="patient-profile">
      <h2>Patient Profile</h2>
      <div v-if="patient">
        <p><strong>Name:</strong> {{ patient.Name }}</p>
        <p><strong>ID:</strong> {{ patient.Patient_ID }}</p>
        <p><strong>Medical Condition:</strong> {{ patient.Medical_Condition }}</p>
        <p><strong>Vitals:</strong> {{ patient.O2_Stats }}, {{ patient.Blood_Pressure }}, {{ patient.Pulse_Rate }}</p>
        <!-- Add other fields as needed -->
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'PatientProfile',
    props: ['id'],
    data() {
      return {
        patient: null,
      };
    },
    created() {
      axios.get(`http://localhost:5000/patients/${this.id}`)
        .then(response => {
          this.patient = response.data;
        })
        .catch(error => {
          console.error('Error loading patient data:', error);
        });
    },
  };
  </script>
  
  <style scoped>
  .patient-profile {
    padding: 20px;
  }
  
  h2 {
    color: #18646c;
    font-weight: 700;
  }
  </style>
  