import file from "./index.json";

Component({
  data: {
    list: ["text", "text"],
  },
  didMount() {
    let values = Object.values(file.data);
    let data = new Array();
    values.forEach((category) => {
      data.push({
        categoryName: category.categoryName,
        miniApps: category.miniApps,
      });
    });
    console.log(data);
    this.setData({
      list: data,
    });
  },
});
