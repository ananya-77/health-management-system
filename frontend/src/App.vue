<template>
    <div id="app">
      <header>
        <img src="@/assets/logo.png" alt="Health Monitoring Logo" />
        <h1>Healthcare Vitals Monitoring System</h1>
      </header>
      <router-view />
    </div>
  </template>
  
  <script>
  export default {
    name: "App",
  };
  </script>
  
  <style scoped>
  header {
    background-color: #b8d2e4;
    color: #18646c;
    padding: 20px;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 15px;
  }
  
  header img {
    height: 50px;
    border-radius: 50%;
  }
  
  header h1 {
    margin: 0;
    font-size: 2em;
    font-weight: 700;
  }
  </style>
  