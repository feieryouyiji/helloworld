<template>
  <div class="b-container">
    <div id="b-my-test">
      <img style="width: 50px; height: 50px" src="https://s2.d2scdn.com/2018/9/10/f0c292ec-f015-4b2f-81a3-e01bd452adb5/10.png" alt="">
      I am freedom
    </div>
    <button @click="takeScreenshot">截图</button>
    <div id="b-my-canvas" v-show="dataUrl">
      <img :src="dataUrl" alt="">
    </div>

    
  </div>
  

</template>
<script>

import html2canvas from 'html2canvas'
import $ from 'jquery'



export default {
  name: 'Html2Canvas',
  data(){
    return {
      dataUrl: undefined,
    }
  },
  mounted(){
    // this.createQRCode()
  },
  methods: {
    createQRCode() {
      const dom = $(this.$el).find('.b-qrcode')[0]
      //if (qrcode) return
      qrcode = new QRCode(dom, {
        text: location.href,
        width: 50,
        height: 50,
        colorDark: '#000000',
        colorLight: '#ffffff',
        correctLevel: QRCode.CorrectLevel.H
      })
    },
    takeScreenshot() {
      let originDom = $(this.$el).find('#b-my-test')[0]

      originDom = originDom.cloneNode(true)
      originDom.style['z-index'] = '-1'
      
      document.body.append(originDom)

      html2canvas(originDom, {
        useCORS: true
      }).then(canvas => {
        this.dataUrl = canvas.toDataURL('image/jpeg')
        originDom.remove()
      })
    }
  }
}


</script>
<style scoped>

</style>