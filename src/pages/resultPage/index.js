Page({
  data: {
    titleList: ["Đặt vé xe khách/máy bay", "Khách sạn/nhà nghỉ", "Nhà hàng"],
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