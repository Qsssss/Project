import { TestBed } from '@angular/core/testing';

import { HotellService } from './hotell.service';

describe('HotellService', () => {
  let service: HotellService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(HotellService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
