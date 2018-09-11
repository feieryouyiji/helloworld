<template>
  <div class="drag-container">

    <div class="b-img-wrapper" v-my-drag>
      <img class="b-img" src="https://s2.d2scdn.com/2018/9/10/f0c292ec-f015-4b2f-81a3-e01bd452adb5/10.png" 
      
      alt="">
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'

  const start = (ev, dom) => {
    let e = !ev.targetTouches ? ev : ev.targetTouches[0] // 兼容 mobile
    dom.setAttribute('dragFlag',true) 
    dom.deltaX = e.pageX - parseInt(dom.offsetLeft)
    dom.deltaY = e.pageY - parseInt(dom.offsetTop)
  }
  const move = (ev, dom) => {
    let e = !ev.targetTouches ? ev : ev.targetTouches[0] // 兼容 mobile
    if (dom.getAttribute('dragFlag')) {
      let x = e.pageX - dom.deltaX //控件左上角到屏幕左上角的相对位置
      let y = e.pageY - dom.deltaY
      dom.style.left = x + 'px'
      dom.style.top = y + 'px'
    }
  }
  const end = (ev, dom) => {
    dom.setAttribute('dragFlag', false) 
  }

  export default {
    data() {
      return {
        dragFlag: false,
        deltaX: 0,
        deltaY: 0,
      }
    },
    directives: {
      myDrag: {
        inserted(el, binding) {
          console.log('inserted------')
          el.addEventListener('mousedown', (ev)=>{
            start(ev, el)
          })
          el.addEventListener('mousemove', (ev)=>{
            move(ev, el)
          })
          el.addEventListener('mousedown', (ev)=>{
            end(ev, el)
          })
        }
      }
    },
    created() {

    },
    methods: {
      start(ev, i) {
        console.log('enter start', ev)
        let e = !ev.targetTouches ? ev : ev.targetTouches[0] // 兼容 mobile
        let imgDom = $(this.$el).find('.b-img-wrapper')
        let right = imgDom.css('right')

        this.dragFlag = true
        this.deltaX = e.pageX - parseInt(imgDom.css('left'))
        this.deltaY = e.pageY - parseInt(imgDom.css('top'))
      },
      move(ev, i) {
        console.log('enter move not start')
        let e = !ev.targetTouches ? ev : ev.targetTouches[0] // 兼容 mobile
        let imgDom = $(this.$el).find('.b-img-wrapper')
        let right = imgDom.css('right')

        if (right <= 0) return
        if (this.dragFlag) {
          console.log('move deltaX', this.deltaX)
          console.log('enter move start', ev)
          let x = e.pageX - this.deltaX //控件左上角到屏幕左上角的相对位置
          let y = e.pageY - this.deltaY
          imgDom.css({
            top: y,
            left: x
          })

        }
      },
      end(ev) {
        console.log('enter end', ev)
        this.dragFlag = false
      }
    }
  }
</script>

<style scoped>
  .drag-container {
    background-color: #ccc;
    width: 100%;
    height: 300px;
    position: relative;
  }

  .b-img-wrapper {
    display: inline-block;
    position: absolute;
    top: 10px;
    left: 10px;

  }

  .b-img {
    width: 50px;
    height: 50px;
  }
</style>