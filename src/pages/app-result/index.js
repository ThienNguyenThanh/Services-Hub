Component({
	data: {
    appList: [],
    app: {
      icon: '',
      title: '',
      description: ''
    }
  },
  didMount() {
    this.setData({
      title: "title",
      description: "des"
    })
  }
});