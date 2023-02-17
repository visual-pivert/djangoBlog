class Search extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(e) {
    this.props.onSearch(e.target.value);
  }
  render() {
    return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("input", {
      type: "search",
      onChange: this.handleChange
    })));
  }
}
function Topbar({
  onSearch
}) {
  return /*#__PURE__*/React.createElement("header", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("div", {
    className: "logo"
  }, /*#__PURE__*/React.createElement("h1", {
    className: "name"
  }, "djangoBlog")), /*#__PURE__*/React.createElement(Search, {
    onSearch: onSearch
  }));
}
const Blog = React.memo(function ({
  blog
}) {
  console.log('blogiiiiiiii');
  return /*#__PURE__*/React.createElement("li", {
    className: "blog"
  }, /*#__PURE__*/React.createElement("h3", null, blog.title), /*#__PURE__*/React.createElement("div", {
    className: "desc_container"
  }, /*#__PURE__*/React.createElement("p", null, blog.comment)));
});
function BlogList({
  filter
}) {
  var lists = [];
  const [fetchValue, setFetch] = React.useState([]);
  React.useEffect(() => {
    fetch('http://192.168.1.103:8000/api/blogs').then(response => response.json()).then(response => {
      setFetch(response);
    }).catch(error => console.error("Erreur : " + error));
  }, []);
  fetchValue.forEach(blog => {
    let str = blog.title.concat(' ', blog.comment);
    let counter = 0;
    if (str.find(filter)) {
      lists.push( /*#__PURE__*/React.createElement(Blog, {
        key: blog.title,
        blog: blog
      }));
    }
  });
  return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("main", {
    className: "bloglist_main"
  }, /*#__PURE__*/React.createElement("ul", null, lists)));
}
class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      searchValue: ""
    };
    this.getSearchValue = this.getSearchValue.bind(this);
  }
  getSearchValue(value) {
    this.setState({
      searchValue: value
    });
  }
  render() {
    return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement(Topbar, {
      onSearch: this.getSearchValue
    }), /*#__PURE__*/React.createElement(BlogList, {
      filter: this.state.searchValue
    }));
  }
}
ReactDOM.createRoot(document.getElementById('root')).render( /*#__PURE__*/React.createElement(React.StrictMode, null, /*#__PURE__*/React.createElement(Home, null)));