import React, { Component } from 'react';
import axios from 'axios';

import NavBar from "./navBar";
import NameDispenser from "../images/name_dispenser.png";
import "../css/register_dispenser.css";

class RegisterDispenser extends Component {

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
            .post("/api/register_dispenser", {
              dispenserName: event,
            })
        event.preventDefault();
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <NavBar/>
                    <div className="register_fields">
                        <img src={NameDispenser} alt="link to homepage" />
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

export default RegisterDispenser;
