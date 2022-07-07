import file from "./index.json"

Component({
	props: {
    category: '',
    apps: {
      title: '',
      description: '',
    },
    loadData: () => {}
  },
  
  didMount() {  
    this.setData({
      category: this.props.loadData(),
    })
  },
  methods: {
    _loadData() {
      for (i = 0; i < file.data.length; i++){
        data = file.data[i];
        category = data.category;
        // for (j = 0; j < data.apps.length; j++)
      }
    },
  }

});