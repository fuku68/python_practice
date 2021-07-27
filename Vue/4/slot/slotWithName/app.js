var MyPage = {
  template: `
        <div>
	  <header>
	    <!-- ヘッダーのスロット（名前つきスロット） -->
	    <slot name="header"></slot>
	  </header>
	  <main>
	    <!-- ボディのスロット -->
	    <slot></slot>
	  </main>
	　<footer>
	　　　<!-- フッターのスロット（名前つきスロット） -->
	　　　<slot name="footer"></slot>
	　</footer>
	</div>
	`,
};

new Vue({
  el: "#app",
  components: {
    MyPage: MyPage,
  },
});
