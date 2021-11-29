Vue.options.delimiters = ["[[", "]]"];

let app = new Vue({
  el: "#app",

  data: {
    isResponse: false,
    bitsize: null,
    mess: null,
    Response: null,
  },

  methods: {
    rabinsend() {
      axios({
        method: "post",
        url: "./rabinsend",
        data: {
          bitsize: this.bitsize,
          mess: this.mess,
        }
      }).then((response) => {
        this.isResponse = true;
        this.Response = response.data.message;
      });
    },
  },
});
