const app = Vue.createApp({
  data() {
    return {
      title : "Bismillah",
      content : "Selamün Aleyküm",
      linker: {
        title: "Google",
        target: "_blank",
        url: "https://www.google.com",
        alt: "Google ana sayfası"
      },
      owner: "Karpuzlu pudding",
    };
  },
});

app.mount("#app"); //id'si app olan elemente bağlanır