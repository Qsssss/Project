import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HotelDetailComponent } from './hotel-detail/hotel-detail.component';
import { MainComponent } from './main/main.component';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { SignUpComponent } from './sign-up/sign-up.component';


const routes: Routes = [
  { path: '', redirectTo: '/main', pathMatch: 'full' },
  { path: 'main', component: MainComponent},
  { path: 'detail', component: HotelDetailComponent},
  { path: 'login', component: LoginComponent},
  { path: 'sign-up', component: SignUpComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
