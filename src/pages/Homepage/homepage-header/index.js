Component({
  props: {
    title: '',
    onTapActionButton: () => {},
    redirectTo: () => {},
  },
  methods: {
    _onTapActionButton() {
      this.props.onTapActionButton({
        redirectTo: this.props.redirectTo()
      })
    },
    redirectTo() {
      my.redirectTo({url: 'pages/popular-apps-page/index'});
    }
  }
	
});