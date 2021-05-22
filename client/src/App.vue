<template>
  <div id="app">
    <div id="nav"></div>
    <router-view />
  </div>
</template>

<style lang="scss" >
html,
body {
  margin: 0;
  padding: 0;
}
.nav {
  background-color: #3b37ff;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

@keyframes transitionIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}
.logo-text{
  cursor: pointer;
}
</style>
