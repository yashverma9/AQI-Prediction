<template>
  <div class="hide-for-dekstop">
    <button id="burger" class="open-main-nav">
      <span class="burger"></span>
    </button>
    <nav class="main-nav" id="main-nav">
      <ul>
        <li>
          <a @click=" router('/')">Home</a>
        </li>
        <li>
          <a @click=" router('Graphs')">Graphs</a>
        </li>
        <li>
          <a @click=" router('Prediction')">Prediction</a>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  name: "nav",
  methods: {
    router(x) {
      this.$router.push(x);
    }
  }
};
</script>

<style lang="scss" scoped>
</style>