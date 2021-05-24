<template>
  <div>
    <div class="grid-container">
      <div class="grid-item grid-item-3 nav"></div>
      <div class="grid-item grid-item-1">
        <div @click=" router('/')" class="logo-text">
          <img style="width:40px; heignt:40px;" src="../images/worldwide.png" alt />
          <p>aqi</p>
        </div>
        <div class="button-parent hide-for-mobile">
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

        <Nav />
      </div>
      <div class="grid-item grid-item-2">
        <div class="header-content">
          <div class="location-text">
            <img
              style="width:40px; height:40px;"
              class="hide-for-mo"
              src="../images/placeholder.png"
              alt
            />

            <p>Bangalore</p>
          </div>
          <div class="button">
            <p>{{date}}</p>
          </div>
        </div>

        <div class="content">
          <div class="aqi">
            <div class="aqi-inner">
              <div v-bind:style="{ background: color }" class="aqi-val">
                <p>{{aqi}}</p>
              </div>
              <p id="status">{{status}}</p>
              <p id="tag">AQI</p>
            </div>
          </div>
          <div class="params-parent">
            <div class="abs-parent">
              <ul>
                <li v-for="(d,index) in data" :key="index">
                  <div class="params">
                    <p id="title">{{d.name}}</p>
                    <p id="value">{{d.value}}</p>
                    <p id="unit">{{d.unit}}</p>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Nav from "../components/Nav.vue";
export default {
  name: "Home",
  components: {
    Nav
  },
  async mounted() {
    nav();
    //Setting date
    var date = new Date();
    var n = date.toDateString();
    this.date = n;

    let restwo = await axios.get(
      "https://api.waqi.info/feed/bangalore/?token=4a410c05fe249e46b247c4a8196b693139cd5210"
    );

    
    this.aqi = restwo.data.data.aqi;
    this.calcaqi();
    let res = await axios.get(
      "https://api.openweathermap.org/data/2.5/weather?q=Bengaluru&APPID=4b3b3ba35fcd7a3d24f3adc38895bbdd&units=metric"
    );

    let param = [
      {
        name: "Temperature",
        value: res.data.main.temp,
        unit: "°C"
      },
      {
        name: "Humidity",
        value: res.data.main.humidity,
        unit: "%"
      },
      {
        name: "Wind Speed",
        value: Number(((res.data.wind.speed * 1000) / 3600).toFixed(2)),
        unit: "Km/h"
      },
      {
        name: "Visibility",
        value: Number((res.data.visibility / 1000).toFixed(2)),
        unit: "Km"
      }
    ];
    this.data = param;
  },
  data() {
    return {
      data: [],
      date: "",
      aqi: "Loading",
      color: "",
      status: ""
    };
  },
  methods: {
    router(x) {
      this.$router.push(x);
    },
    calcaqi() {
      if (this.aqi <= 30) {
        this.status = "Good";
        this.color = "#00CC00";
      } else if (this.aqi > 30 && this.aqi <= 60) {
        this.status = "Satisfactory";
        this.color = "#67CC01";
      } else if (this.aqi > 60 && this.aqi <= 90) {
        this.status = "Moderately polluted";
        this.color = "#FFFE01";
      } else if (this.aqi > 90 && this.aqi <= 120) {
        this.status = "Poor";
        this.color = "#FE9901";
      } else if (this.aqi > 120 && this.aqi <= 250) {
        this.status = "Very Poor";
        this.color = "#FE0001";
      } else if (this.aqi > 250) {
        this.status = "Severe";
        this.color = "#A52A2A";
      }
    }
  }
};
/* eslint-disable */
function nav() {
  let burger = document.getElementById("burger"),
    nav = document.getElementById("main-nav"),
    slowmo = document.getElementById("slowmo");

  burger.addEventListener("click", function(e) {
    this.classList.toggle("is-open");
    nav.classList.toggle("is-open");
  });

  /* Onload demo - dirty timeout */
  let clickEvent = new Event("click");

  window.addEventListener("load", function(e) {
    slowmo.dispatchEvent(clickEvent);
    burger.dispatchEvent(clickEvent);

    setTimeout(function() {
      burger.dispatchEvent(clickEvent);

      setTimeout(function() {
        slowmo.dispatchEvent(clickEvent);
      }, 3500);
    }, 5500);
  });
}
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
  animation: transitionIn 0.4s;
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
    text-align: center;
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
  width: 31vw;
  height: 300px;
  // border: solid red;
  top: 40%;
  left: 50%;
  transform: translate(-50%, 0%);
  // display: flex;
  // align-items: flex-start;
  // justify-content: flex-start;
  // flex-wrap: wrap;
  //border: dotted red;
  ul {
    width: 100%;

    padding: 0;
    margin: 0;
    list-style-type: none;
    display: flex;
    justify-content: center;
    flex-wrap: wrap;

    position: absolute;
    top: 0%;
    left: 50%;
    transform: translate(-50%);
  }

  li {
    margin: 1rem;
  }
}

.abs-parent {
  height: 100%;
  width: 100%;
  position: relative;
  //border: dotted rebeccapurple;
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

  font-size: 34px;

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

@media only screen and (max-width: 1024px) {
  .grid-container {
    display: grid;
    grid-template-columns: 2vw 96vw 2vw;
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
    animation: transitionIn 0.4s;
    height: max-content;
    padding-bottom: 10px;
  }

  .logo-text {
    display: flex;
    align-items: center;
    justify-content: space-between;
    // border: dotted red;
    width: 106px;
    height: 100%;
    p {
      font-family: "Reem Kufi", sans-serif;
      text-align: center;
      
      font-size: 43px;
      
      /* identical to box height */

      color: #ffffff;
      margin: 0;
      margin-bottom: 10px;
      padding: 0;
    }
  }

  .location-text {
    display: flex;
    align-items: center;
    justify-content: space-between;
    // border: dotted forestgreen;
    width: 195px;
    height: 100%;

    p {
      font-family: "Poppins";
      font-style: normal;
      font-weight: normal;
      font-size: 30px;
      line-height: 54px;
      /* identical to box height */

      color: #000000;
    }
    img {
      width: 35px !important;
      height: 35px !important;
    }
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
      font-size: 16px;
      line-height: 27px;
      /* identical to box height */

      color: #000000;
    }
  }

  .content {
    background-color: #3c37ff;
    box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.25);
    border-radius: 4px;
    width: 100%;
    height: 800px;
    position: relative;
    // margin-top: 20px;
  }

  .params-parent {
    position: absolute;
    width: 31vw;
    height: 300px;
    // border: solid red;
    top: 28%;
    left: 50%;
    transform: translate(-50%, 0%);
    // display: flex;
    // align-items: flex-start;
    // justify-content: flex-start;
    // flex-wrap: wrap;
    //border: dotted red;
    ul {
      width: 100%;

      padding: 0;
      margin: 0;
      list-style-type: none;
      display: flex;
      justify-content: center;
      flex-wrap: wrap;

      position: absolute;
      top: 0%;
      left: 50%;
      transform: translate(-50%);
    }

    li {
      margin: 1rem;
    }
  }

  .space {
    width: 100%;

    height: 10px;
  }
  //end
}

@media only screen and (max-width: 360px) {
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
      font-size: 15px;
      line-height: 27px;
      /* identical to box height */

      color: #000000;
    }
  }
}
</style>
