Page({
  data: {
    category: 'Phổ biến',
    categoryApps: [],
    apps: {
      title: '',
      icon: '',
      url: ''
    },
    seeMore: 'Xem thêm',
  },

	onLoad() {
    this.setData({
      seeMore: this.data.seeMore,
    })
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
