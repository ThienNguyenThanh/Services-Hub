

Component({
	data: {
    categoryList: ['Phổ biến', 'Lịch sử', 'Yêu thích', 'text'],
    category: '',
    apps: {
      url: '',
    },
    action: 'Xem thêm',
    onTapActionButton: () => {},
    navigateTo: () => {},
  },
  methods: {
    didMount() {
      this.setData({
        category: this.data.categoryList.pop(),
        action: this.data.action,
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