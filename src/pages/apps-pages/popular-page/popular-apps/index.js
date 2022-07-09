import file from "./index.json"

Component({
	data: {
    list: []
  },
  didMount() {
    let dataList = Object.entries(file.data)
    let appData = new Array()
    console.log(dataList[0].category)
    dataList.forEach((data) => {
      appData.push({
        category: data[0],
        appList: data[1].apps
      })
    
    })
    this.setData({
      list: appData
    })
    
  },
  export: data
}) ;
