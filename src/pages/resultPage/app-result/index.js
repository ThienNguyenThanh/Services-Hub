import file from "./index.json"

Component({
  props: {
    categoryList: [],
    category: '',
    miniApps: [
      
    ],
    miniApp: {
    }
    // titleList: [],
    // title: '',
    // descriptionList: [],
    // description: ''
  },
  didMount() {
    // this.props = file.data
  
    let values = Object.values(file.data)
    const miniData = new Map()
    values.forEach(element => {
      miniData.set(element.category, element.miniApps)
    });
    for (let i = 0; i < values.length; i ++){
      this.props.categoryList.push(values[i].category)
    }
    console.log(this.props.categoryList)
    for (let i = 0; i < this.props.categoryList.length; i++){
      let temp = this.props.categoryList[i]
      this.props.category = temp
      let appTemp;
      if (miniData.has(temp)){
        appTemp = miniData.get(temp)
        this.props.miniApps.push(miniData.get(temp))  
        for (let j = 0; j < appTemp.length; j++){
          this.props.miniApp = appTemp[j]
        }
      }
    }
    console.log(this.props.miniApps)
    // console.log(this.props.category)
    console.log(this.props.miniApp.title)
    this.setData({props: this.props})
  }
})
    