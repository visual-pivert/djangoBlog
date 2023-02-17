

class Search extends React.Component {

    constructor(props) {
        super(props)
        this.handleChange = this.handleChange.bind(this)
    }

    handleChange(e) {
        this.props.onSearch(e.target.value)
    }

    render() {
        return(
            <>
                <div>
                    <input type="search" onChange={this.handleChange}/>
                </div>
            </>
        )
    }

}

function Topbar ({onSearch}) {
    return(
        <header className="topbar">
            <div className="logo">
                <h1 className="name">djangoBlog</h1>
            </div>
            <Search onSearch={onSearch}/>
            
        </header>
    )
}

const Blog = React.memo(function ({blog}) {
    console.log('blogiiiiiiii')
    return(
        <li className="blog">
            <h3>{blog.title}</h3>
            <div className="desc_container">
                <p>{blog.comment}</p>
            </div>
        </li>
    )
})

function BlogList ({filter}) {
    var lists = []
    const [fetchValue, setFetch] = React.useState([])

    
    React.useEffect(() => {
        fetch('http://192.168.1.103:8000/api/blogs')
        .then(response => response.json())
        .then(response => {
            setFetch(response)
        })
        .catch(error => console.error("Erreur : " + error));
    }, [])


    fetchValue.forEach(blog => {
        let str = blog.title.concat(' ', blog.comment)
        let counter = 0        
        if (str.find(filter)) {
            lists.push( <Blog key={blog.title} blog={blog} />)
        }
        
    })
    
        
    return(<>
        <main className="bloglist_main">
            <ul>
                {lists}
            </ul>
        </main>
        </>
    )
}


class Home extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            searchValue: ""
        }
        this.getSearchValue = this.getSearchValue.bind(this)
    }

    getSearchValue(value) {
        this.setState({searchValue: value})
    }

    render() {
        return(
            <>
                <Topbar onSearch={this.getSearchValue}/>  
                <BlogList filter={this.state.searchValue}/>
            </>
        )
    }

}

ReactDOM.createRoot(document.getElementById('root')).render(
    <React.StrictMode>
        <Home />
    </React.StrictMode>,
  )