import file from "./index.json"

Component({
  props: {
  },
  
  didMount() {
    let values = Object.values(file.data)
    this.props = new Map()
    values.forEach(item => {
      this.props.set(item.category, item.miniApps)
      console.log(item.category)
      this.setData({
        props: item,
        category: item.category,
        miniApps: item.miniApps
      })
    });
    this.props.forEach(category => {
      // console.log(category)
      category.forEach(miniApp => {
        // console.log(miniApp)
        this.setData({
          title: miniApp.title,
          description: miniApp.description
        })
      })
      // this.setData({
      //   category.forEach(mini)
      // })
    })
   
    // for (let i = 0; i < values.length; i ++){
    //   this.props.categoryList.push(values[i].category)
    // }
    // console.log(this.props.categoryList)
    // for (let i = 0; i < this.props.categoryList.length; i++){
    //   let temp = this.props.categoryList[i]
    //   this.props.category = temp
    //   let appTemp;
    //   if (miniData.has(temp)){
    //     appTemp = miniData.get(temp)
    //     this.props.miniApps.push(miniData.get(temp))  
    //     for (let j = 0; j < appTemp.length; j++){
    //       this.props.miniApp = appTemp[j]
    //     }
    //   }
    // }
    // console.log(this.props.miniApps)
    // // console.log(this.props.category)
    // console.log(this.props.miniApp.title)
    
    
  }
})
    