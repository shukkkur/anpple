<h2 align = "center"> ANPPLE 🍎</h2>
<h4 align = "center"><i>letter "E" in ANPPLE stands for nothing. Had to add it, to make it sound like Apple</i></h4>

<p>Predict a price for a laptop on popular advertising website <a href="https://lalafo.kg/">lalafo.kg</a>, when price is set to <strong>Negotiable/Договорная</strong></p>

<h3>Usage Example</h3>

<ol>
  <li>Find a laptop ad with "Netogiable Price/Договорная" - <a href="https://lalafo.kg/bishkek/ads/apple-macbook-pro-intel-core-i5-8-gb-ozu-133-id-99023770">sample link</a></li>
  
  <li>We are hosting our model on <a href="https://lalafo-price-predictor.netlify.app/">netlify</a>. Paste the a link and click "Scrape". Our scraping algorithm will follow the link and scrape all the available features.</li>
  <li><p>The "Predict Price" button will run the model and display the approximated price for the chosen laptop advertisement.</p>
  <img src="https://user-images.githubusercontent.com/78250180/158939097-8fcf383f-e40e-4556-bc82-2357484ec44d.png" alt="img" style="width:100%">
  </li>
</ol>

<p><strong>Notice!</strong> In case you would like to run the project, you will have to follow netlify link, click scrape and in web console (<strong>SHIFT + CTRL + "C"</strong>) proceed to the ip address and verify security check. After that there should be no problems.</p>

<img src="https://user-images.githubusercontent.com/78250180/158939758-6fde0541-9857-4b13-ae80-4ae8fb43d526.png">


<h2>Model Building</h2>
<ol>
  <li>To collect the data for training, we wrote a script to scrape features and price for every laptop ad. We collected 3,700 ads.</li>
  <li>After cleaning the data and some feature engineering we had 1.5k instances.</li>
  <li>Since, we had a number of categorical features and due to some other factors we decided to go with <strong>LightGBM</strong>.</li>
  <li>Highest accuracy - 81%</li>
</ol>

<p>You can find a more detailed information regarding the  project in <a href="https://github.com/shukkkur/anpple/blob/50687e5a5897cf01170847c68dbefd93859c3dd1/ANPPLE.pptx">anpple.ppt</a>

  <hr/>
<p> This project is a result of group work: </p>
<ul> 
  <li><a href="https://github.com/ErlanBazarov/">@erlanbazarov</a> - (pre-processing & hosting)</li>
  <li><a href="https://github.com/AlgoAIBoss">@algoAIboss</a> - (model building)</li>
  <li><a href="https://github.com/AlgoAIBoss">@shukkkur</a> - Web Scraping</li>
</ul>



