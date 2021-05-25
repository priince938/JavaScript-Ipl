//Import all the fuction from another js
import { totalrunsfuction } from "./totalruns.js"
import { topbatsmanfuction } from "./topsbatman.js"
import { umpirefuction } from "./umpir.js"
import { season } from "./season.js"

//To load the fuction when browser open or refresh
totalrunsfuction()
//Onclick event are declared to run the fuction only when the button is clicked
document.getElementById("totalruns-btn").addEventListener("click",totalrunsfuction);
document.getElementById("topsbatman-btn").addEventListener("click",topbatsmanfuction);
document.getElementById("umpire-btn").addEventListener("click",umpirefuction);
document.getElementById("season-btn").addEventListener("click",season);

