import file from "./index.json";

Component({
  data: {
    list: [],
    category: 'Thanh toan',
    onTapButtonAction: () => {}
  },
  methods: {
  didMount() {
      let values = Object.values(file.payment);
      let data = new Array();
      values.forEach((app) => {
        console.log(app)
        data.push({
          description: app.description,
          icon: app.image_url,
          title: app.name,
          deepLink: app.metadata.deep_link
        });
        this.data["id"] =  app.id
      });
      
      this.setData({
        list: data,
        category: this.data.category
      });
    },
    _onTapButtonAction() {
      my.navigateToMiniApp({
        appId: this.data.list.id,
        path: this.data.list.deepLink,
        extraData: {
          from: 'MiniApp Demo'
        },
        success: (res) => {
          console.log(res)
        },
        fail: (e) => {
          console.log(e)
        }
      })
      console.log(this.data.list)
    },
  }
});
