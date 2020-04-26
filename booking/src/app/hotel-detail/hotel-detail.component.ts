import { Component, OnInit } from '@angular/core';
import { Hotel } from '../hotels';
import { HotellService } from '../hotell.service';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

@Component({
  selector: 'app-hotel-detail',
  templateUrl: './hotel-detail.component.html',
  styleUrls: ['./hotel-detail.component.css']
})
export class HotelDetailComponent implements OnInit {

  hotel: Hotel;

  constructor(
    private route: ActivatedRoute,
    private hotellService: HotellService,
    private location: Location
    ) { }

  ngOnInit(): void {
    this.getHotel();
  }

  getHotel(): void{
    const id = +this.route.snapshot.paramMap.get('id');
    this.hotellService.getHotel(id)
    .subscribe(hotel => this.hotel=hotel);
  }

  goBack(): void {
    this.location.back();
  }

}
