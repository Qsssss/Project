import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Hotel } from './hotels';
import { HOTELS } from './hotel';
import { Room } from './rooms';
import { ROOMS } from './room';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HotellService {
  BASE_URL = 'http://localhost:8000'

  getHotels(): Observable<Hotel[]> {
    return this.http.get<Hotel[]>(`${this.BASE_URL}/hotels`)
  }

  getHotel(id: number): Observable<Hotel> {
    return this.http.get<Hotel>(`${this.BASE_URL}/hotels/${id}/`);
  }
  
  getRooms(id: number): Observable<Room> {
    return of(ROOMS.find(room => room.id === id));
  }

  constructor(private http: HttpClient) { }
}
