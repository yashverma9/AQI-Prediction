<template>
  <div>
    <div class="grid-container">
      <div class="grid-item grid-item-3 nav"></div>
      <div class="grid-item grid-item-1">
        <div @click="router('/')" class="logo-text">
          <img style="width:40px; heignt:40px;" src="../images/worldwide.png" alt />
          <p>aqi</p>
        </div>
        <div class="button-parent hide-for-mobile">
          <div @click="router('/')" class="button" style>
            <p>Home</p>
          </div>
          <div @click="router('Graphs')" class="button">
            <p>Graphs</p>
          </div>
          <div @click="router('Prediction')" class="button">
            <p>Prediction</p>
          </div>
        </div>
        <Nav />
      </div>
      <div class="grid-item grid-item-2">
        <div class="header-content">
          <div class="location-text">
            <img style="width:40px; height:40px;" src="../images/graph.png" alt />
            <p>Graphs</p>
          </div>
          <div class="buttons-parent">
            <div @click="slice()" class="button">
              <p>{{ timeline }}</p>
            </div>
            <div @click="changeType()" style="margin-left:15px;" class="button">
              <p>{{ typename }}</p>
            </div>
          </div>
        </div>

        <div class="content">
          <div class="graph-parent">
            <p>AQI</p>
            <div class="chart-parent">
              <div class="chart-container">
                <canvas id="myChart"></canvas>
              </div>
            </div>
          </div>
          <div class="graph-parent">
            <p>Temperature</p>
            <div class="chart-parent">
              <div class="chart-container">
                <canvas id="myChart-two"></canvas>
              </div>
            </div>
          </div>
          <div class="graph-parent">
            <p>Humidity</p>
            <div class="chart-parent">
              <div class="chart-container">
                <canvas id="myChart-three"></canvas>
              </div>
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
  name: "Graphs",
  components: {
    Nav
  },
  async mounted() {
    nav();

    //SETTING DATE
    let dateObj = new Date();
    let myDate =
      dateObj.getUTCFullYear() +
      "-" +
      (dateObj.getMonth() + 1) +
      "-" +
      dateObj.getUTCDate();
    let myDatee =
      dateObj.getUTCFullYear() +
      "-" +
      dateObj.getMonth() +
      "-" +
      dateObj.getUTCDate();
    var startdate = myDatee.toString();
    var enddate = myDate.toString();

    //SETTING DATE

    // TRYING TO GET MONTHLY AQI
    //   let aqi = await axios.get(
    //     "http://api.openweathermap.org/data/2.5/air_pollution/history?lat=13&lon=77&start=1619182588&end=1621774588&appid=4b3b3ba35fcd7a3d24f3adc38895bbdd"
    //   );
    // console.log(aqi.data.list);
    //   for (let i = 0; i < aqi.data.list.length; i++) {
    //     console.log(convertUnix(aqi.data.list[i].dt));
    //     console.log(aqi.data.list[i].main.aqi);
    //   }
    // END

    let res = await axios.get(
      `http://api.worldweatheronline.com/premium/v1/past-weather.ashx?tp=24&q=Bengaluru&date=${startdate}&enddate=${enddate}&key=2b0714b1fb8e4b38a93185230211605&format=json`
    );
    let restwo = await axios.get(
      "https://aqi-backend.herokuapp.com/aqiMonthChart"
    );

    for (var i = 0; i < res.data.data.weather.length; i++) {
      this.date.push(convertDate(res.data.data.weather[i].date));
      this.humidity.push(res.data.data.weather[i].hourly[0].humidity);
      this.temp.push(res.data.data.weather[i].avgtempC);
    }
    this.aqi_date = restwo.data.date;
    this.aqi = restwo.data.aqi;
    this.destroy = false;
    for (let i = 0; i < this.aqi_date.length; i++) {
      this.aqi_date[i] = convertDate(this.aqi_date[i]);
    }
    if (screen.width == 1024 || screen.width < 1024) {
      this.type = "line";
      this.typename = "Line";
      this.timeline = "Weekly";
      this.font = 14;
      this.plotGraphWeekly(this.font);
    } else {
      this.type = "line";
      this.timeline = "Monthly";
      this.typename = "Line";
      this.font = 18;
      this.plotGraph(this.font);
    }

    //reverse
    // this.aqi_date =  this.aqi_date.reverse();
    // this.aqi.reverse();
    // this.date.reverse();
    // this.humidity.reverse();
    // this.temp.reverse();
    // this.aqi_date.reverse();
    // this.aqi.reverse();

    //converting aqi date to correct format
  },
  data() {
    return {
      date: [],
      humidity: [],
      temp: [],
      aqi_date: [],
      aqi: [],
      type: "",
      typename: ". . . .",
      timeline: "Loading",
      font: null
    };
  },
  methods: {
    router(x) {
      this.$router.push(x);
    },
    plotGraph(font) {
      g1(this.aqi_date, this.aqi, this.type, font);
      g2(this.date, this.temp, this.type, font);
      g3(this.date, this.humidity, this.type, font);
    },
    plotGraphWeekly(font) {
      g1(this.aqi_date.slice(23, 30), this.aqi.slice(23, 30), this.type, font);
      g2(this.date.slice(23, 30), this.temp.slice(23, 30), this.type, font);
      g3(this.date.slice(23, 30), this.humidity.slice(23, 30), this.type, font);
    },
    slice() {
      if (this.timeline == "Monthly") {
        destroy(chartobj);
        g1(
          this.aqi_date.slice(23, 30),
          this.aqi.slice(23, 30),
          this.type,
          this.font
        );
        g2(
          this.date.slice(23, 30),
          this.temp.slice(23, 30),
          this.type,
          this.font
        );
        g3(
          this.date.slice(23, 30),
          this.humidity.slice(23, 30),
          this.type,
          this.font
        );
        this.timeline = "Weekly";
      } else {
        destroy(chartobj);
        this.plotGraph();
        this.timeline = "Monthly";
      }
    },
    changeType() {
      if (this.type == "bar") {
        this.type = "line";
        this.typename = "Line";
      } else {
        this.type = "bar";
        this.typename = "Bar";
      }
      destroy(chartobj);

      if (this.timeline == "Monthly") {
        this.plotGraph(this.font);
      } else {
        g1(
          this.aqi_date.slice(23, 30),
          this.aqi.slice(23, 30),
          this.type,
          this.font
        );
        g2(
          this.date.slice(23, 30),
          this.temp.slice(23, 30),
          this.type,
          this.font
        );
        g3(
          this.date.slice(23, 30),
          this.humidity.slice(23, 30),
          this.type,
          this.font
        );
      }
    }
  }
};
/* eslint-disable */
var chartobj = [];
function destroy(chartobj) {
  for (let i = 0; i < chartobj.length; i++) {
    chartobj[i].destroy();
  }
}
function g1(aqi_date, aqi, type, font) {
  if (myChart) {
    myChart.destroy();
  }
  var ctx = document.getElementById("myChart");
  var myChart = new Chart(ctx, {
    type: type,
    data: {
      labels: aqi_date,
      datasets: [
        {
          label: "AQI",
          data: aqi,
          backgroundColor: [, "white"],
          borderColor: ["white"],
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          ticks: {
            color: "white",
            // Include a dollar sign in the ticks
            callback: function(value, index, values) {
              return "" + value;
            },
            font: {
              size: font
            }
          },
          beginAtZero: true
        },

        x: {
          ticks: {
            color: "white",
            font: {
              size: font
            }
          }
        }
      },

      plugins: {
        legend: {
          display: true,
          labels: {
            color: "white",
            font: {
              size: font
            }
          }
        }
      }
    }
  });
  chartobj.push(myChart);
}

function g2(date, temp, type, font) {
  var ctx = document.getElementById("myChart-two");
  var myChart = new Chart(ctx, {
    type: type,
    data: {
      labels: date,
      datasets: [
        {
          label: "Temperature",
          data: temp,
          backgroundColor: ["#D90A39"],
          borderColor: ["#D90A39"],
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          ticks: {
            color: "white",
            // Include a dollar sign in the ticks
            callback: function(value, index, values) {
              return value + "°C";
            },
            font: {
              size: font
            }
          },
          beginAtZero: true
        },

        x: {
          ticks: {
            color: "white",
            font: {
              size: font
            }
          }
        }
      },

      plugins: {
        legend: {
          display: true,
          labels: {
            color: "white",
            font: {
              size: font
            }
          }
        }
      }
    }
  });
  chartobj.push(myChart);
}

function g3(date, humidity, type, font) {
  var ctx = document.getElementById("myChart-three");
  var myChart = new Chart(ctx, {
    type: type,
    data: {
      labels: date,
      datasets: [
        {
          label: "Humidity",
          data: humidity,
          backgroundColor: ["#29A744"],
          borderColor: ["#29A744"],
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          ticks: {
            color: "white",
            // Include a dollar sign in the ticks
            callback: function(value, index, values) {
              return value + "%";
            },
            font: {
              size: font
            }
          },
          beginAtZero: true
        },

        x: {
          ticks: {
            color: "white",
            font: {
              size: font
            }
          }
        }
      },

      plugins: {
        legend: {
          display: true,
          labels: {
            color: "white",
            font: {
              size: font
            }
          }
        }
      }
    }
  });
  chartobj.push(myChart);
}

function convertDate(date) {
  let dateObj = new Date(date);
  let myDate =
    dateObj.getUTCDate() +
    "-" +
    (dateObj.getMonth() + 1) +
    "-" +
    dateObj.getUTCFullYear();
  var str = myDate.toString();
  var result = str.slice(0, 5) + str.slice(7, 9);
  return result;
}

function convertUnix(date) {
  const milliseconds = date * 1000;
  let dateObj = new Date(milliseconds);
  let humanDateFormat = dateObj.toLocaleString();
  let x = convertDate(humanDateFormat);
  return x;
}

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
  grid-template-rows: 60px 100%;
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

  //background-color: #ffffff;
}
.location-text {
  display: flex;
  align-items: center;
  justify-content: space-between;
  // border: dotted forestgreen;
  width: 194px;
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
  height: max-content;
  padding-top: 40px;
  padding-bottom: 40px;
  position: relative;

  // margin-top: 20px;
  //   ul {
  //     // position: absolute;
  //     // top: 10%;
  //     // left: 50%;
  //     // transform: translate(-50%, 0%);
  //     // width: 100%;
  //     // height: 100%;
  //     list-style-type: none;
  //     margin: 0;
  //     padding: 0;
  //     margin: 0 auto;
  //   }
  //   li {
  //     margin-bottom: 40px;
  //   }
}

.graph-parent {
  position: relative;
  margin: 0 auto;
  margin-bottom: 40px;
  width: 95%;
  height: 39.5vw;
  background: #161389;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 4px;
  p {
    padding: 0;
    margin: 0;
    font-family: Poppins;
    font-style: normal;
    font-weight: normal;
    font-size: 24px;
    line-height: 36px;
    /* identical to box height */

    color: #ffffff;
    position: absolute;
    top: 4%;
    left: 2%;
  }
}

#myChart {
  // width: 50% !important;
  // height: 50% !important;
}
.chart-container {
  //border: dotted green;
  position: relative;
  height: 20vh;
  width: 68vw;
}
.chart-parent {
  position: absolute;
  top: 10%;
  left: 50%;
  transform: translate(-50%);
  //border: dotted red;
  height: max-content;
  width: max-content;
}

.buttons-parent {
  //border: solid red;
  width: max-content;
  display: flex;
  justify-content: space-between;
  align-items: center;
  //   position: sticky;
  // top: 0%;
  // z-index: 2;
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
    width: 154px;
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

  .graph-parent {
    position: relative;
    margin: 0 auto;
    margin-bottom: 40px;
    width: 95%;
    height: 60vw;
    background: #161389;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 4px;
    p {
      padding: 0;
      margin: 0;
      font-family: Poppins;
      font-style: normal;
      font-weight: normal;
      font-size: 24px;
      line-height: 36px;
      /* identical to box height */

      color: #ffffff;
      position: absolute;
      top: 4%;
      left: 2%;
    }
  }
  .chart-container {
    //border: dotted green;
    position: relative;
    height: 20vh;
    width: 87vw;
  }
  .chart-parent {
    position: absolute;
    top: 22%;
    left: 50%;
    transform: translate(-50%);
    //border: dotted red;
    height: max-content;
    width: max-content;
  }

  .content {
    background-color: #3c37ff;
    box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.25);
    border-radius: 4px;
    width: 100%;
    height: max-content;
    padding-top: 40px;
    padding-bottom: 10px;
    position: relative;

    // margin-top: 20px;
    //   ul {
    //     // position: absolute;
    //     // top: 10%;
    //     // left: 50%;
    //     // transform: translate(-50%, 0%);
    //     // width: 100%;
    //     // height: 100%;
    //     list-style-type: none;
    //     margin: 0;
    //     padding: 0;
    //     margin: 0 auto;
    //   }
    //   li {
    //     margin-bottom: 40px;
    //   }
  }
  //end
}
</style>
