<template>
  <div class="big-wrapper">
    <nuxt/>
  </div>
</template>

<style>
html {
  font-family: "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  height: 100%;
  width: 100%;
}

*, *:before, *:after {
  box-sizing: border-box;
  margin: 0;
}

.big-wrapper {
  min-height: 100vh;
  display: flex;
}
</style>
