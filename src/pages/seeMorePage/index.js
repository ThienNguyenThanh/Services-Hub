Page({
  data: {
    titleList: ["Đặt vé xe khách/máy bay"],
    title: "",
    // _onTapActionButton: () => {},
    seeMore: 'Hiện thêm kết quả',

  },
	onLoad() {
    this.setData({
      title: this.data.titleList.pop(),
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