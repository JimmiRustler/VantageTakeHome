import React, { Component } from "react";
import { Button } from "reactstrap";
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      adImage: 'Woman.jpg',
      adInfo:"",
      adTitle:"",
      URL:"",
    };
  }

  //Working on learning adChange events
  handleAdChange = (e) => {
    this.setState({adImage: e.target.value})

  }

  

  //Saves required information and sends it via axios to backend
  adSave = () =>{
    axios.post('http://localhost:8000/api/ad/', {
      "id": "",
      "image": this.state.image,
      "adInfo": this.state.adInfo,
      "adTitle": this.state.adTitle,
      "URL": this.state.URL,
    })
    .then((response) => {
      console.log(response);
    })
    .catch((err) => {
      console.log(err)
    });
  }

  //Sets info from textboxes as the text is typed
  setAdInfo = (e) => {
    this.setState({adInfo: e.target.value})
  }
  setAdTitle = (e) => {
    this.setState({adTitle: e.target.value})
  }
  setAdURL = (e) => {
    this.setState({URL: e.target.value})
  }

  //Webpage Code:
  //Card Rendered to give the Adpreview its own box and space. Split into two section with the text area
  //having a title, ad blurb and URL entry with an image to the left.
  //Below dropdown added and working on adding hard coded values to use as an image selector as well as update the image when chosen
  //Three Text Fields allowing the change of the Ad Title, Info and URL
  //Save button to save preview info to backend.
  render() {
      return (
        <div>
          <div class='CardBody parent'>
              <div class='image'>
                <img src={this.state.adImage} alt="picture here" width="200" height="170"></img>
              </div>
              <div class='child'>
                <h4><b>{this.state.adTitle}</b></h4>
                <p>{this.state.adInfo}</p>
                <p>{this.state.URL}</p>
              </div>
          </div>

          <div class='image'>
          <select onChange={(e) => this.handleAdChange(e)} name="selectList" id="selectList" value={this.state.value}>
            <option selected disabled value="Images">Images</option>
            <option value="Woman.jpg">Woman</option>
            <option value="Man.jpg">Man</option>
          </select>
          </div>

          <div>
            <form class='adFields'>
              <input onChange={(e) => this.setAdTitle(e)} name="adName" placeholder ="Ad Title" type="text"/>
            </form>
            <form class='adFields'>
              <input onChange={(e) => this.setAdInfo(e)} name="adInfo" placeholder ="Ad Info" type="text"/>
            </form>
            <form class='adFields'>
              <input onChange={(e) => this.setAdURL(e)} name="adURL" placeholder ="Web URL" type="text"/>
            </form>
        </div>
        <div class = 'save'>
          <Button onClick={() => this.adSave()}>Save</Button>
        </div>  
      </div>
      );
    }
  }
export default App;