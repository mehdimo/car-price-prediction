import { Component, OnInit } from '@angular/core';
import {CarModelsService} from './car-models.service'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent implements OnInit {
  title = 'Car price prediction';
  manufacturers: { [key: string]: string[] } = {};
  engineVols: { [key: string]: string[] } = {};

  constructor(private carModelsService: CarModelsService) {}

  ngOnInit() {
    this.carModelsService.getManufacturers().subscribe(data => {
      this.manufacturers = data;
    });

    this.carModelsService.getEngineVolumes().subscribe(data => {
      this.engineVols = data;
    });
  }
}
