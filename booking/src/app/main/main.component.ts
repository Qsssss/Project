import { Component, OnInit } from '@angular/core';
import { HOTELS } from '../hotel';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  hotels = HOTELS;
  constructor() { }

  ngOnInit(): void {
  }
  getHotels(){
    var x = (<HTMLInputElement>document.getElementById('stars')).value;
    var y = (<HTMLInputElement>document.getElementById('city')).value;
    
    var div = document.getElementById('demo1');
    div.parentNode.removeChild(div);

    var div1 = document.createElement('div');
    div1.id = 'demo1';
    document.getElementById('demo').appendChild(div1);

    for (var i = 0; i<this.hotels.length; i++){

      if ( this.hotels[i]["stars"] == x && this.hotels[i]["city"] == y){

        var img1 = document.createElement('img');
        img1.src =  this.hotels[i]["photo"];
        img1.className = "ph";
        img1.onclick = this.getInfo;
        img1.height = 200;
        img1.width = 300;
        var text = document.createElement('a');
        text.textContent = this.hotels[i].name;
        text.href = "/detail";
        var br = document.createElement("br");
        
        document.getElementById('demo1').appendChild(br);
        document.getElementById('demo1').appendChild(img1);
        document.getElementById('demo1').appendChild(text);
      }
    }
  }
  getInfo(){
    window.alert("aaa");
  }
}
