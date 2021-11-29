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
    rsasend() {
      axios({
        method: "post",
        url: "./rsasend",
        data: {
          bitsize: this.bitsize,
          mess: this.mess,
        }
      }).then((response) => {
        this.isResponse = true;
        this.Response = response.data.message;
      });
    },
    rsasign() {
      axios({
        method: "post",
        url: "./rsasign",
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
