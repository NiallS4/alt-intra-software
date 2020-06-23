import React, { Component } from "react";
import { Link } from "react-router-dom";
import "../css/home.css"
// import { withAuthenticator } from "aws-amplify-react";
// import aws_exports from "./../aws-exports";
import NavBar from "./navBar";

// Amplify.configure(aws_exports);

class Home extends Component {
    render() {
        return (
            <div><NavBar />
                <div className="home_body">
                    <div className="user_voptions">
                        <div className="register_dispenser">
                            <Link to="/register_dispenser">
                                <button className="home_buttons">
                                    Register dispenser
                                </button>
                            </Link>
                        </div>
                        <div className="search_dispenser">
                            <Link to="/search_dispenser">
                                <button className="register">
                                    Search dispenser
                                </button>
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

// export default withAuthenticator(Home);
export default Home;
