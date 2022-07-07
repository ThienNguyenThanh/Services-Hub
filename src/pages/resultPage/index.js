Page({
  data: {
    titleList: ["Đặt vé xe khách/máy bay"],
    title: "",
    // _onTapActionButton: () => {},

  },
	onLoad() {
    this.setData({
      title: this.data.titleList.pop()
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