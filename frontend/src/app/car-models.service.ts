import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CarModelsService {
  private car_models_url = "/assets/car_models_list.json";
  private car_engine_vols_url = "/assets/engine_vols_list.json";

  constructor(private http: HttpClient) {}

  getManufacturers(): Observable<{ [key: string]: string[] }> {
    return this.http.get<{ [key: string]: string[] }>(this.car_models_url);
  }

  getEngineVolumes(): Observable<{ [key: string]: string[] }> {
    return this.http.get<{ [key: string]: string[] }>(this.car_engine_vols_url);
  }
}
