import {React, Component, Fragment} from 'react';
import axios from 'axios';


class AptTables extends Component {

    main_url = 'http://127.0.0.1:5000/'
    update_url = 'http://127.0.0.1:5000/update'


    constructor(props) {
        super(props);
        this.state = {'apts':[], 'headers':[]}
    }

    fetch_data = async (url) => {
        const response = await axios.get(url)
        const apts = response.data.apts
        const headers = [];
        for (let header in apts[0]){
            if (header !== 'link'){
                headers.push(header)
            }
        }
        this.setState({headers, apts})
      }

    componentDidMount = () => {
        this.fetch_data(this.main_url)
    }

    onUpdate = () => {
        this.fetch_data(this.update_url)

    }

    render() {
        return (
            <div className="ui center aligned container" style={{padding:'5em'}}>
                <button className='ui button' onClick={this.onUpdate}>Update</button>
                <table className="ui collapsing celled striped padded center aligned table">
                    <thead className="ui center aligned header">
                        <tr>{
                            this.state.headers.map(header => {
                                return(<th key = {header}>{header}</th>)
                            })
                        }</tr>
                    </thead>
                    <tbody>{
                        this.state.apts.map(apt => {
                            return(
                                <tr key={apt['id']}>
                                    <td key='link'>
                                        <a href={apt['link']}>
                                            {apt['id']}
                                        </a>
                                    </td>{
                                        this.state.headers
                                        .filter(header => header !== 'id')
                                        .map(header => {
                                            return(
                                                <td key={header}>
                                                    {apt[header]}
                                                </td>
                                            )
                                        })
                                    }
                                </tr>
                            )
                        })
                    }</tbody>
                </table>
            </div>
        );
    }
}

export default AptTables;