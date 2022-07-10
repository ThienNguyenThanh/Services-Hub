

Component({
	data: {
    categoryList: ['Phổ biến', 'Yêu thích'],
    category: '',
    action: 'Xem thêm',
    onTapActionButton: () => {},
    navigateTo: () => {},
  },
  
  methods: {
    didMount() {
     this.setData({
       category: this.data.categoryList.pop()
     })
    },
    _onTapActionButton() {
      if (this.data.category == 'Phổ biến') {
        my.navigateTo({url: '../apps-pages/popular-page/index'})
      }
      if (this.data.category == 'Lịch sử') {
        my.navigateTo({url: '../apps-pages/history-page/index'})
      }
      if (this.data.category == 'Yêu thích') {
        my.navigateTo({url: '../apps-pages/favorite-page/index'})
      }
    },
  
  }, 
});