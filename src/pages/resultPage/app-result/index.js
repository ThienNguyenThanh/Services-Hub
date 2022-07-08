import file from "./index.json"

Component({
  props: {
    categoryList: [],
    appList: [],
    title: '',
    category: '',
    description: ''
  },
  didMount() {
    this.setData({
      categoryList: file.data,
    })
    this.props.categoryList = file.data
    
  }
})
    