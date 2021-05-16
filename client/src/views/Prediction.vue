<template>
  <div>
    <div class="grid-container">
      <div class="grid-item grid-item-3 nav"></div>
      <div class="grid-item grid-item-1">
        <div @click=" router('/')" class="logo-text">
          <img style="width:40px; heignt:40px;" src="../images/worldwide.png" alt />
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
            <p>Prediction</p>
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
              <p id="tag">Predicted AQI</p>
            </div>
          </div>
          <div class="text">
            <ul>
              <li>
                <p>um lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero. Sed dignissim lacinia nunc. Curabitur tortor. Pellentesque nibh. Aenean quam. In scelerisque sem at dolor. Maecenas mattis. Sed convallis tristique sem. Proin ut ligula vel nunc egestas porttitor. Morbi lectus risus, iaculis vel, suscipit quis, luctus non, massa. Fusce ac turpis quis ligula lacinia aliquet. Mauris ipsum. Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh. Quisque volutpat condimentum velit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nam nec ante. Sed lacinia, urna non tincidunt mattis, tortor neque adipiscing diam, a cursus ipsum ante quis turpis. Nulla facilisi. Ut fringilla. Suspendisse potenti. Nunc feugiat mi a tellus consequat imperdiet. Vestibulum sapien. Proin quam. Etiam ultrices. Suspendisse in justo eu magna luctus suscipit. Sed lectus. Integer euismod lacus luctus</p>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Home",
  async mounted() {
    let response = await axios.get(
      "https://api.openweathermap.org/data/2.5/weather?q=Bengaluru&APPID=4b3b3ba35fcd7a3d24f3adc38895bbdd&units=metric"
    );
    let pp = 0;
    if (response) {
      if (response.data.rain && response.data.rain["3h"]) {
        pp = response.data.rain["3h"];
      } else if (response.data.snow && response.data.snow["3h"]) {
        pp = response.data.snow["3h"];
      }
    }

    console.log(response.data);
    let params = {
      T: response.data.main.temp,
      TM: response.data.main.temp_max,
      Tm: response.data.main.temp_min,
      H: response.data.main.humidity,
      PP: pp,
      VV: Number((response.data.visibility / 1000).toFixed(2)),
      V: Number(((response.data.wind.speed * 1000) / 3600).toFixed(2)),
      VM: Number(((response.data.wind.speed * 1000) / 3600).toFixed(2))
    };
    console.log(params);

    this.getPredict(params);
  },
  data() {
    return {};
  },
  methods: {
    router(x) {
      this.$router.push(x);
    },
    async getPredict(params) {
      console.log(params);
      let res = await axios.post("http://127.0.0.1:5000/getPrediction", {
        params
      });
      console.log(res.data);
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

  padding-top: 35px;
  padding-bottom: 35px;
  //   position: relative;
  // margin-top: 20px;
}
.aqi {
  //   position: absolute;
  width: 350px;
  height: 170px;
  //   top: 6%;
  //   left: 50%;
  //   transform: translate(-50%, 0%);
  margin: 0 auto;

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
  top: 34%;
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
  top: 70%;
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
  left: 22%;
  transform: translate(-50%, 0%);
  font-family: Poppins;

  font-size: 18px;

  color: #ffffff;
}
.text {
  //   position: absolute;
  //   top: 45%;
  //   left: 50%;
  //   transform: translate(-50%, 0%);
  width: 82%;
  min-height: 300px;
  max-height: max-content;
  margin: 0 auto;
  margin-top: 40px;
  background-color: white;
  border-radius: 4px;
  padding-top: 10px;

  ul {
    list-style: none;
    width: 80%;
    margin: 0 auto;

    padding: 0;
  }

  li {
    padding-bottom: 10px;
    p {
      font-family: Poppins;
      font-size: 18px;
      color: black;
      text-align: left;
    }
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
