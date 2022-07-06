Component({
	data: {
    categoryList: ['Phổ biến', 'Lịch sử', 'Yêu thích'],
    category: '',
  },
  didMount() {
    this.setData({
      category: this.data.categoryList.pop(),
    })
  }
});