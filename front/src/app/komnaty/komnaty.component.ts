import { Component, OnInit } from '@angular/core';
import { HotellService } from '../hotell.service';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { Room } from '../rooms'

@Component({
  selector: 'app-komnaty',
  templateUrl: './komnaty.component.html',
  styleUrls: ['./komnaty.component.css']
})
export class KomnatyComponent implements OnInit {
  room: Room;
  constructor(private route: ActivatedRoute,
    private hotellService: HotellService,
    private location: Location) { }

  ngOnInit(): void {
    this.getRooms();
  }

  getRooms(): void{
    const id = +this.route.snapshot.paramMap.get('id');
    this.hotellService.getRooms(id)
    .subscribe(room => this.room=room);
  }

  goBack(): void {
    this.location.back();
  }
}
