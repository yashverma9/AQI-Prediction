<template>
  <div>
    <div class="grid-container">
      <div class="grid-item grid-item-3 nav"></div>
      <div class="grid-item grid-item-1">
        <div @click=" router('/')" class="logo-text">
          <img  style="width:40px; heignt:40px;" src="../images/worldwide.png" alt />
          <p>aqi</p>
        </div>
        <div class="button-parent">
          <div @click=" router('/')" class="button" style>
            <p>Home</p>
          </div>
          <div @click=" router('Graphs')" class="button">
            <p>Graphs</p>
          </div>
          <div @click=" router('Prediction')" class="button">
            <p>Prediction</p>
          </div>
        </div>
      </div>
      <div class="grid-item grid-item-2">
        <div class="header-content">
          <div class="location-text">
            <img style="width:40px; height:40px;" src="../images/placeholder.png" alt />
            <p>Bangalore</p>
          </div>
          <div class="button">
            <p>2021-05-14 04:00</p>
          </div>
        </div>

        <div class="content">
          <div class="aqi">
            <div class="aqi-inner">
              <div class="aqi-val">
                <p>299</p>
              </div>
              <p id="status">Unhealthy</p>
              <p id="tag">AQI</p>
            </div>
          </div>
          <div class="params-parent">
            <ul>
              <li>
                <div class="params">
                  <p id="title">Temperature</p>

                  <p id="value">33</p>
                  <p id="unit">°C</p>
                </div>
              </li>
              <li>
                <div class="params"></div>
              </li>
              <li>
                <div class="params"></div>
              </li>
              <li>
                <div class="params"></div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {};
  },
  methods: {
    router(x) {
      this.$router.push(x);
    }
  }
};
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Reem+Kufi&display=swap");
.grid-container {
  display: grid;
  grid-template-columns: 12vw 76vw 12vw;
  grid-template-rows: 60px calc(100vh - 60px);
}

.grid-item-1 {
  grid-row-start: 1;
  grid-row-end: 2;
  grid-column-start: 2;
  grid-column-end: 3;
 // border: solid blue;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.grid-item-3 {
  grid-row-start: 1;
  grid-row-end: 2;
  grid-column-start: 1;
  grid-column-end: 4;
 // border: solid blue;
}

.grid-item-2 {
  grid-row-start: 2;
  grid-row-end: 3;
  grid-column-start: 2;
  grid-column-end: 3;
// border: solid blue;
}

.logo-text {
  display: flex;
  align-items: center;
  justify-content: space-between;
  // border: dotted red;
  width: 120px;
  height: 100%;
  p {
    font-family: "Reem Kufi", sans-serif;

    font-style: normal;
    font-weight: normal;
    font-size: 48px;
    line-height: 72px;
    /* identical to box height */

    color: #ffffff;
  }
}
.button-parent {
  display: flex;
  align-items: center;
  justify-content: space-between;
  // border: dotted red;
  width: 290px;
  height: 100%;
}
.button:hover {
  cursor: pointer;
  background: #d1a609;
  //  border: 1.8px solid #000000;
  // box-sizing: border-box;
  border-radius: 4px;
}

.button {
  background: #ffc700;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  max-height: 37px;
  width: max-content;
  padding-left: 10px;
  padding-right: 10px;
  p {
    font-family: "Poppins";
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 27px;
    /* identical to box height */

    color: #000000;
  }
}

.header-content {
  width: 100%;
  height: 12vh;
  // border: dotted red;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.location-text {
  display: flex;
  align-items: center;
  justify-content: space-between;
  // border: dotted forestgreen;
  width: 240px;
  height: 100%;

  p {
    font-family: "Poppins";
    font-style: normal;
    font-weight: normal;
    font-size: 36px;
    line-height: 54px;
    /* identical to box height */

    color: #000000;
  }
}

.content {
  background-color: #3c37ff;
  box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.25);
  border-radius: 4px;
  width: 100%;
  height: 550px;
  position: relative;
  // margin-top: 20px;
}
.aqi {
  position: absolute;
  width: 284px;
  height: 144px;
  top: 6%;
  left: 50%;
  transform: translate(-50%, 0%);

  background: #161389;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 4px;
}
.aqi-inner {
  width: 100%;
  height: 100%;
  position: relative;
}
.aqi-val {
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  top: 12%;
  left: 50%;
  transform: translate(-50%, 0%);
  width: 76px;
  height: 37px;
  background: #e10000;
  border-radius: 4px;
  p {
    margin: 0;
    padding: 0;
    font-family: Poppins;
    font-style: normal;
    font-weight: normal;
    font-size: 30px;

    /* identical to box height */

    color: #121010;
  }
}
#status {
  margin: 0;
  padding: 0;

  position: absolute;
  top: 60%;
  left: 50%;
  transform: translate(-50%, 0%);
  font-family: Poppins;

  font-size: 24px;

  color: #ffffff;
}
#tag {
  margin: 0;
  padding: 0;
  position: absolute;
  top: 6%;
  left: 10%;
  transform: translate(-50%, 0%);
  font-family: Poppins;

  font-size: 18px;

  color: #ffffff;
}
.params-parent {
  position: absolute;
  width: 82%;
  height: 300px;
  //border: solid red;
  top: 40%;
  left: 50%;
  transform: translate(-50%, 0%);
  // display: flex;
  // align-items: flex-start;
  // justify-content: flex-start;
  // flex-wrap: wrap;
  ul {
    width: 100%;

    padding: 0;
    list-style-type: none;
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
  }

  li {
    margin: 1rem;
  }
}
.params {
  width: 202px;
  height: 105px;
  background: #161389;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 4px;
  // margin-right: 10px;
  position: relative;
}
#title {
  margin: 0;
  padding: 0;

  position: absolute;
  top: 10%;
  left: 6%;
  transform: translate(0%, 0%);
  font-family: Poppins;

  font-size: 24px;

  color: #dadada;
}

#value {
  margin: 0;
  padding: 0;

  position: absolute;
  bottom: 1%;
  left: 6%;
  transform: translate(0%, 0%);
  font-family: Poppins;

  font-size: 36px;

  color: #ffffff;
}

#unit {
  margin: 0;
  padding: 0;

  position: absolute;
  bottom: 10%;
  right: 6%;
  transform: translate(0%, 0%);
  font-family: Poppins;

  font-size: 18px;

  color: #dadada;
}
</style>
