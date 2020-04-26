import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Hotel } from './hotels';
import { HOTELS } from './hotel';
import { Room } from './rooms';
import { ROOMS } from './room';

@Injectable({
  providedIn: 'root'
})
export class HotellService {

  getHotels(): Observable<Hotel[]> {
    return of(HOTELS);
  }

  getHotel(id: number): Observable<Hotel> {
    return of(HOTELS.find(hotel => hotel.id === id));
  }
  
  getRooms(id: number): Observable<Room> {
    return of(ROOMS.find(room => room.id === id));
  }

  constructor() { }
}
