import React, { Component } from 'react';
import axios from 'axios';

import NavBar from "./navBar";
import SearchDispenser1 from "../images/search_dispenser1.png";
import "../css/search_dispenser.css";

class SearchDispenser extends Component {

    constructor(props) {
        super(props);
        this.state = {value: ''};

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
      }

    handleChange(event) {
        this.setState({value: event.target.value});
      }

    handleSubmit(event) {
        axios
            .get("/api/search_dispenser", {
              dispenserName: event,
            })
        event.preventDefault();
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <NavBar/>
                    <div className="register_fields">
                        <img src={SearchDispenser1} alt="search_dispenser_image" />
                        <br></br>
                            <input
                                className="dispenser_name"
                                type="text"
                                value={this.state.value}
                                onChange={this.handleChange}
                            />
                            <input className="dispenser_name" type="submit" value="ENTER" />
                    </div>
            </form>
        )
    }
}

export default SearchDispenser;
