import { Component, Input, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Car} from '../Car'

type CarModels = {
    [key: string]: string[];
};

@Component({
  selector: 'app-car-info',
  templateUrl: './car-info.component.html',
  styleUrls: ['./car-info.component.sass']
})
export class CarInfoComponent implements OnInit{
    backendHost = 'localhost';
    backend_url = "/api";
    predicted_price = ""
    car: Car = {
        manufacturer: '',
        model: '',
        year: 2023,
        mileage: 0,
        engine: "4"
    }

    @Input() car_models: { [key: string]: string[] } = {};
    @Input() engine_vols: { [key: string]: string[] } = {};
    objectKeys = Object.keys;

    constructor(private http: HttpClient) {}

    submit() {
        console.log(`Car Info: ${this.car.year} ${this.car.manufacturer} ${this.car.model}, ${this.car.mileage} miles`);
        const predict_url = this.backendHost + this.backend_url + "/predict"
        this.http.post(predict_url, this.car).subscribe(
              (response: any) => {
                console.log('Car info sent successfully:', response);
                this.predicted_price = response.prediction
              },
              (error) => {
                console.log('Error sending car info:', error);
              }
            );
    }

    ngOnInit() {
        this.http.get('/assets/config.json').subscribe((config: any) => {
            this.backendHost = config.backendHost;
        });
    }

}
