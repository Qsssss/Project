import { Component, OnInit } from '@angular/core';
import { Hotel } from '../hotels';
import { HotellService } from '../hotell.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  
  hotels: Hotel[] = [];

  constructor(public hotelService: HotellService) { }

  ngOnInit(): void {
    this.getHotels();
  }

  getHotels(){ 
    this.hotelService.getHotels()
      .subscribe( hotels => { console.log(this.hotels=hotels) });
  }
  
}
