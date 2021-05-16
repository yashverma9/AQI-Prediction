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
            <img style="width:40px; height:40px;" src="../images/graph.png" alt />
            <p>Graphs</p>
          </div>
          <div class="button">
            <p>Weekly</p>
          </div>
        </div>

        <div class="content">
          <div class="graph-parent">
            <p>Graph 1</p>
            <div class="chart-parent">
              <div class="chart-container">
                <canvas id="myChart"></canvas>
              </div>
            </div>
          </div>
          <div class="graph-parent">
            <p>Graph 1</p>
          </div>
          <div class="graph-parent">
            <p>Graph 1</p>
          </div>
          <div class="graph-parent">
            <p>Graph 1</p>
          </div>
          <div class="graph-parent">
            <p>Graph 1</p>
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
    console.log(res.data.data.weather)
    for(var i=0; i<res.data.data.weather.length;i++)
    {
      console.log(res.data.data.weather[i].date)
      console.log(res.data.data.weather[i].hourly[0].humidity)
      console.log(res.data.data.weather[i].avgtempC)
    }
    g1();
  },
  data() {
    return {};
  },
  methods: {
    router(x) {
      this.$router.push(x);
    }
  }
};
/* eslint-disable */
function g1() {
  console.log("called");
  var ctx = document.getElementById("myChart");
  var myChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
      datasets: [
        {
          label: "# of Votes",
          data: [12, 19, 3, 5, 2, 3],
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 206, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(255, 159, 64, 0.2)"
          ],
          borderColor: [
            "rgba(255, 99, 132, 1)",
            "rgba(54, 162, 235, 1)",
            "rgba(255, 206, 86, 1)",
            "rgba(75, 192, 192, 1)",
            "rgba(153, 102, 255, 1)",
            "rgba(255, 159, 64, 1)"
          ],
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
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
  height: 55vh;
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
  transform: translate(-50% ,);
  //border: dotted red;
  height: max-content;
  width: max-content;
}
</style>
