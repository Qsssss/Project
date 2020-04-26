import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { KomnatyComponent } from './komnaty.component';

describe('KomnatyComponent', () => {
  let component: KomnatyComponent;
  let fixture: ComponentFixture<KomnatyComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ KomnatyComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(KomnatyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
