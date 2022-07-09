import file from "./index.json"

Page({
  props: {
    list: [],
  },
	onLoad() {
    let dataList = Object.entries(file.data)
    let temp = {}
    let tempArray = new Array()
    let appData = new Array()
    
    dataList.forEach((data) => {
      appData.push({
        category: data[0],
        appList: data[1].apps
      })
    })
    this.setData({
      list: appData
    })
    console.log(appData[0].appList)
    // appList.forEach((apps) => {
    //   apps["apps"].forEach((app) => {
    //     appData.push({
    //       description: app.description,
    //       id: app.id,
    //       icon: app.image_url,
    //       title: app.name,
    //     })
    //   })
    // })
    // categoryList.forEach((category) => {
    //   data.push({
    //     category: category,
    //     appData: appData
    //   })
    // })
    
	},
	onReady() {
    
	},
	onShow() {
    
	},
	onHide() {
	},
	onUnload() {
	}
});