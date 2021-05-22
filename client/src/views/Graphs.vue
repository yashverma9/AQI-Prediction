<template>
  <div>
    <div class="grid-container">
      <div class="grid-item grid-item-3 nav"></div>
      <div class="grid-item grid-item-1">
        <div @click="router('/')" class="logo-text">
          <img style="width:40px; heignt:40px;" src="../images/worldwide.png" alt />
          <p>aqi</p>
        </div>
        <div class="button-parent">
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
      </div>
      <div class="grid-item grid-item-2">
        <div class="header-content">
          <div class="location-text">
            <img style="width:40px; height:40px;" src="../images/graph.png" alt />
            <p>Graphs</p>
          </div>
          <div class="buttons-parent">
            <div @click="slice()" class="button">
              <p>{{timeline}}</p>
            </div>
            <div @click="changeType()" style="margin-left:15px;" class="button">
              <p>{{typename}}</p>
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
export default {
  name: "Graphs",
  async mounted() {
    let res = await axios.get(
      "http://api.worldweatheronline.com/premium/v1/past-weather.ashx?tp=24&q=Bengaluru&date=2021-04-16&enddate=2021-05-15&key=2b0714b1fb8e4b38a93185230211605&format=json"
    );
    let restwo = await axios.get("http://127.0.0.1:5000/aqiMonthChart");

    for (var i = 0; i < res.data.data.weather.length; i++) {
      this.date.push(res.data.data.weather[i].date);
      this.humidity.push(res.data.data.weather[i].hourly[0].humidity);
      this.temp.push(res.data.data.weather[i].avgtempC);
    }
    this.aqi_date = restwo.data.date;
    this.aqi = restwo.data.aqi;
    this.destroy = false;
    this.type = "line";
    this.timeline = "Monthly";

    //reverse
    // this.aqi_date =  this.aqi_date.reverse();
    // this.aqi.reverse();
    // this.date.reverse();
    // this.humidity.reverse();
    // this.temp.reverse();
    // this.aqi_date.reverse();
    // this.aqi.reverse();

    this.plotGraph();
  },
  data() {
    return {
      date: [],
      humidity: [],
      temp: [],
      aqi_date: [],
      aqi: [],
      type: "",
      typename: "Line",
      timeline: "Monthly"
    };
  },
  methods: {
    router(x) {
      this.$router.push(x);
    },
    plotGraph() {
      g1(this.aqi_date, this.aqi, this.type);
      g2(this.date, this.temp, this.type);
      g3(this.date, this.humidity, this.type);
    },
    slice() {
      if (this.timeline == "Monthly") {
        destroy(chartobj);
        g1(this.aqi_date.slice(23, 30), this.aqi.slice(23, 30), this.type);
        g2(this.date.slice(23, 30), this.temp.slice(23, 30), this.type);
        g3(this.date.slice(23, 30), this.humidity.slice(23, 30), this.type);
        this.timeline = "Weekly";
      } else {
        destroy(chartobj);
        this.plotGraph();
        this.timeline = "Monthly";
      }

      // this.aqi_date.slice(0,22);
      // console.log(this.humidity);
      //  console.log(this.humidity.slice(23,30));
    },
    changeType() {
      console.log("called");
      if (this.type == "bar") {
        this.type = "line";
        this.typename = "Line";
      } else {
        this.type = "bar";
        this.typename = "Bar";
      }
      destroy(chartobj);
      // this.destroy = true;
      // g1(this.aqi_date, this.aqi, this.type, this.destroy);
      // console.log(this.type);
      if (this.timeline == "Monthly") {
        this.plotGraph();
      } else {
        g1(this.aqi_date.slice(23, 30), this.aqi.slice(23, 30), this.type);
        g2(this.date.slice(23, 30), this.temp.slice(23, 30), this.type);
        g3(this.date.slice(23, 30), this.humidity.slice(23, 30), this.type);
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
function g1(aqi_date, aqi, type, destroy) {
 
  if (myChart) {
    myChart.destroy();
    console.log("destroyed");
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
          backgroundColor: [ , "white"],
          borderColor: [ "white"],
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
              size: 16
            }
          },
          beginAtZero: true
        },

        x: {
          ticks: {
            color: "white"
          }
        }
      },

      plugins: {
        legend: {
          display: true,
          labels: {
            color: "white",
            font: {
              size: 18
            }
          }
        }
      }
    }
  });
  chartobj.push(myChart);
  console.log(chartobj);
}



function g2(date, temp, type) {
  console.log("called");
  console.log(date);
  console.log(temp);
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
              size: 16
            }
          },
          beginAtZero: true
        },

        x: {
          ticks: {
            color: "white"
          }
        }
      },

      plugins: {
        legend: {
          display: true,
          labels: {
            color: "white",
            font: {
              size: 18
            }
          }
        }
      }
    }
  });
  chartobj.push(myChart);
}

function g3(date, humidity, type) {
  console.log("called");
  console.log(date);
  console.log(humidity);
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
              size: 16
            }
          },
          beginAtZero: true
        },

        x: {
          ticks: {
            color: "white",
            font: {
             
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
              size: 18
            }
          }
        }
      }
    }
  });
  chartobj.push(myChart);
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
  animation: transitionIn 0.40s;
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
  width: 80%;
  height: 27.5vw;
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
  width: 40vw;
}
.chart-parent {
  position: absolute;
  top: 18%;
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
}
</style>
