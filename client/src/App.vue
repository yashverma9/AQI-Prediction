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
.logo-text {
  cursor: pointer;
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

.hide-for-dekstop {
  display: none;
}

@media only screen and (max-width: 1024px) {
  .hide-for-dekstop {
    display: block;
  }
  .hide-for-mobile {
    display: none !important;
  }
}

.space {
  width: 100%;

  height: 10px;
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

/* Main menu positionning */
.main-nav {
  position: absolute;
  top: 0;
  right: 0;
  left: 0;
  bottom: 0;
  text-align: center;
  background: #fff;
  opacity: 0;
  z-index: -1;
  visibility: hidden;
  transition: all 0.375s;
}

.main-nav.is-open {
  opacity: 1;
  z-index: 100;
  visibility: visible;
}

/* Yellow band effect */
.main-nav::before {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: -15px;
  background: #3c37ff;
  transform-origin: 0 0;
  transform: skew(-14deg) translateX(-120%);
  transition: all 0.275s 0.1s;
}

.main-nav.is-open::before {
  transform: skew(-14deg) translateX(0);
}

/* Skewing effect on menu links */
.main-nav ul {
  display: inline-flex;
  flex-direction: column;
  height: 93%; /* Should be 100%, but we have a notice message :D */
  align-items: flex-end;
  justify-content: center;
  transform: translateX(-18%) skew(-16deg);
}

.main-nav li {
  display: block;
  margin: 0.5rem 0;
  text-align: right;
  transform: skew(16deg);
}

/* Apparition effect on links */
.main-nav a {
  opacity: 0;
  transform: translateY(-10px);
}

.main-nav.is-open a {
  opacity: 1;
  transform: translateY(0);
}
.main-nav li:nth-child(1) a {
  transition: all 275ms 175ms;
}
.main-nav li:nth-child(2) a {
  transition: all 275ms 225ms;
}
.main-nav li:nth-child(3) a {
  transition: all 275ms 275ms;
}
.main-nav li:nth-child(4) a {
  transition: all 275ms 325ms;
}
.main-nav li:nth-child(5) a {
  transition: all 275ms 375ms;
}

/* Decoration */
.main-nav ul,
.main-nav li {
  list-style: none;
  padding: 0;
}
.main-nav a {
  display: block;
  padding: 12px 0;
  color: #ffffff;
  font-size: 1.4em;
  text-decoration: none;
  font-weight: bold;
  font-family: "Poppins";
}

/* Burger Style: @see: https://codepen.io/CreativeJuiz/full/oMZNXy */
.open-main-nav {
  position: absolute;
  top: 15px;
  padding-top: 20px;
  right: 15px;
  z-index: 1000;
  background: none;
  border: 0;
  cursor: pointer;
}
.open-main-nav:focus {
  outline: none;
}
.burger {
  position: relative;
  display: block;
  width: 28px;
  height: 4px;
  margin: 0 auto;
  background: #ffffff;
  transform: skew(5deg);
  transition: all 0.275s;
}

.burger:after,
.burger:before {
  content: "";
  display: block;
  height: 100%;
  background: #ffffff;
  transition: all 0.275s;
}

.burger:after {
  transform: translateY(-12px) translateX(-2px) skew(-20deg);
}

.burger:before {
  transform: translateY(-16px) skew(-10deg);
}

/* Toggle State part */
.is-open .burger {
  transform: skew(5deg) translateY(-8px) rotate(-45deg);
}

.is-open .burger:before {
  transform: translateY(0px) skew(-10deg) rotate(75deg);
}

.is-open .burger:after {
  transform: translateY(-12px) translateX(10px) skew(-20deg);
  opacity: 0;
}

/* MENU Text part */

.burger-text {
  display: block;
  font-size: 0.675rem;
  letter-spacing: 0.05em;
  margin-top: 0.5em;
  text-transform: uppercase;
  font-weight: 500;
  text-align: center;
  color: #5a3b5d;
}

.device {
  position: relative;
  width: 345px;
  height: 600px;
  background: #fff;
  border: 1px solid #eee;
  border-radius: 3px;
  box-shadow: 0 0 0 10px rgba(0, 0, 0, 0.1);
}

.container {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  overflow: hidden;
  background: linear-gradient(to bottom, #eee, #ddd);
}

/* Slow motion button */
[id="slowmo"] {
  position: absolute;
  top: 20px;
  right: 20px;
  padding: 10px;
  border: 0;
  font-size: 1rem;
  background: #fedc2a;
  color: #5a3b5d;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.275s;
}

[id="slowmo"] span {
  display: block;
  font-weight: normal;
}

[id="slowmo"]:hover,
[id="slowmo"]:focus {
  background: #5a3b5d;
  color: #fedc2a;
}

[id="slowmo"].is-slowmo span:after {
  content: "Activated";
  display: block;
  font-weight: bold;
}

/* When slowmotion is activated */

.is-slowmo + .device .open-main-nav .burger,
.is-slowmo + .device .open-main-nav .burger:before,
.is-slowmo + .device .open-main-nav .burger:after,
.is-slowmo + .device .main-nav,
.is-slowmo + .device .main-nav::before,
.is-slowmo + .device .main-nav a {
  transition-duration: 3s;
}
.is-slowmo + .device .main-nav li:nth-child(1) a {
  transition-delay: 1750ms;
}
.is-slowmo + .device .main-nav li:nth-child(2) a {
  transition-delay: 2250ms;
}
.is-slowmo + .device .main-nav li:nth-child(3) a {
  transition-delay: 2750ms;
}
.is-slowmo + .device .main-nav li:nth-child(4) a {
  transition-delay: 3250ms;
}
.is-slowmo + .device .main-nav li:nth-child(5) a {
  transition-delay: 3750ms;
}

/* Notice */
.notice {
  position: absolute;
  bottom: -15px;
  left: 0;
  right: 0;
  padding: 20px;
  background: #f2f2f2;
  color: #5a3b5d;
  font-size: 14px;
  font-weight: 400;
  line-height: 1.5;
  z-index: 100;
  text-align: center;
}
.notice strong {
  font-weight: 700;
}
.notice a {
  padding: 2px 3px;
  background: #fedc2a;
  text-decoration: none;
}
</style>
