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
            <img style="width:45px; height:45px;" src="../images/prediction (1).png" alt />
            <p>Prediction</p>
          </div>
          <div @click="changeUser()" class="button">
            <p>{{user}}</p>
          </div>
        </div>

        <div class="content">
          <div class="aqi">
            <div class="aqi-inner">
              <div v-bind:style="{ background: color  }" class="aqi-val">
                <p>{{aqi}}</p>
              </div>
              <p id="status">{{status}}</p>
              <p id="tag">Predicted AQI <span>for tomorrow </span>  </p>
            </div>
          </div>
          <div class="text">
            <ul>
              <li>
                <p
                  style="font-weight:bold;"
                >Following precautions must be taken based on forecasted AQI value</p>
              </li>
            </ul>

            <ul style="list-style-type:inherit; margin-top:20px;">
              <li v-for="(d,index) in final" :key="index">
                <p>{{d}}</p>
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
import Nav from "../components/Nav.vue";
export default {
  name: "Home",
  components: {
    Nav
  },
  async mounted() {
    nav();
    this.user = "Causual";

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

    this.getPredict(params);
  },
  data() {
    return {
      aqi: "Loading",
      status: "",
      color: "",
      precautions: [],
      causual: [],
      org: [],
      user: "",
      final: []
    };
  },
  methods: {
    router(x) {
      this.$router.push(x);
    },
    async getPredict(params) {
      let res = await axios.post(
        "https://aqi-backend.herokuapp.com/getPrediction",
        {
          params
        }
      );

      this.aqi = res.data;
      if (this.aqi <= 30) {
        this.status = "Good";
        this.color = "#00CC00";
        this.causual = [
          "Go outdoor and enjoy the fresh breeze, play some games or have a brief walk!",
          "No use of mask required, safe for all kinds of people."
        ];
        this.org = [
          " The levels are very good, so take similar steps to maintain the same condition."
        ];
      } else if (this.aqi > 30 && this.aqi <= 60) {
        this.status = "Satisfactory";
        this.color = "#67CC01";
        this.causual = [
          " Normal air quality of majority of the population, though people with some severe health problems can avoid going out.",
          "Use mask while going out if you face respiratory problems."
        ];
        this.org = [
          "Conditions are good for most of the public, but release a health advisory for people with respiratory problem and suggest to wear a mask!"
        ];
      } else if (this.aqi > 60 && this.aqi <= 90) {
        this.status = "Moderately polluted";
        this.color = "#FFFE01";
        this.causual = [
          " Use mask if you are facing issues in breathing.",
          "Avoid use of cars to avoid worsening the conditions."
        ];
        this.org = [
          " Increase use of public transport compared to private transport by releasing relevant guidelines. Less cars on the road can make a difference.",
          "Health advise to lungs patients to wear a mask."
        ];
      } else if (this.aqi > 90 && this.aqi <= 120) {
        this.status = "Poor";
        this.color = "#FE9901";
        this.causual = [
          "Engage in car pool if necessary to go out or use public transport.",
          "Wear mask if facing any issues."
        ];
        this.org = [
          "This is pretty bad condition and special rules should be released for the public. Announce few days as No Private Cars day (unless very urgent) to control the situation.",
          " Mask a must for all facing health issues."
        ];
      } else if (this.aqi > 120 && this.aqi <= 250) {
        this.status = "Very Poor";
        this.color = "#FE0001";
        this.causual = [
          "Don't go out unless very urgent. If you do, prefer to wear a mask.",
          "Use Air Purifiers at your home to improve air quality inside your home.",
          "Only use public transport to avoid more pollution."
        ];
        this.org = [
          " As the condition becomes worse, it is important to take some big steps like introducing odd-even day for cars.",
          " Industries can also be given some hours to function to avoid more pollution.",
          "For long term, electric solutions can be looked into."
        ];
      } else if (this.aqi > 250) {
        this.status = "Severe";
        this.color = "#A52A2A";
        this.causual = [
          "This is a very bad condition, and a mask is must for all.",
          "Use Air Purifiers at home.",
          "Use pubic transport instead of private unless very urgent."
        ];
        this.org = [
          "This is the worst it can be and is very harmful for everyone's health. Health advisory and control on certain actions is very important.",
          "Take some big steps like introducing odd-even day for cars.",
          " Industries can also be given some hours to function to avoid more pollution.",
          "For long term, electric solutions can be looked into."
        ];
      }
      this.final = this.causual;
    },
    changeUser() {
      if (this.user == "Causual") {
        this.user = "Organization";
        this.final = this.org;
      } else {
        this.user = "Causual";
        this.final = this.causual;
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
  // background: #e10000;
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
  transform: translate(-50%,);
  font-family: Poppins;

  font-size: 24px;
  width: fit-content;
  color: #ffffff;
}
#tag {
  margin: 0;
  padding: 0;
  position: absolute;
  top: 6%;
  left: 4%;
  // transform: translate(-50%, 0%);
  font-family: Poppins;
  width: fit-content;
  font-size: 18px;

  color: #ffffff;
  span{
    
    font-size: 12px;
  }
}
.text {
  //   position: absolute;
  //   top: 45%;
  //   left: 50%;
  //   transform: translate(-50%, 0%);
  width: 60%;

  height: max-content;
  margin: 0 auto;
  margin-top: 40px;
  background-color: white;
  border-radius: 4px;
  padding-top: 15px;
  padding-bottom: 15px;

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
      margin: 0;
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

////////@at-root

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
      font-style: normal;
      font-weight: normal;
      font-size: 43px;
      line-height: 72px;
      /* identical to box height */

      color: #ffffff;
    }
  }

  .location-text {
    display: flex;
    align-items: center;
    justify-content: space-between;
    // border: dotted forestgreen;
    width: 200px;
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
      width: 40px !important;
      height: 40px !important;
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

  .text {
    //   position: absolute;
    //   top: 45%;
    //   left: 50%;
    //   transform: translate(-50%, 0%);
    width: 93%;

    height: max-content;
    margin: 0 auto;
    margin-top: 40px;
    background-color: white;
    border-radius: 4px;
    padding-top: 15px;
    padding-bottom: 15px;

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
        margin: 0;
      }
    }
  }

  .aqi {
    //   position: absolute;
    width: 90vw;
    height: 170px;
    //   top: 6%;
    //   left: 50%;
    //   transform: translate(-50%, 0%);
    margin: 0 auto;

    background: #161389;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 4px;
  }
}
</style>
