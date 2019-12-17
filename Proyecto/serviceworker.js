var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(

    fetch(event.request)
    .then((result)=>{
      return caches.open(CACHE_NAME)
      .then(function(c) {
        c.put(event.request.url, result.clone())
        return result;
      })
      
    })
    .catch(function(e){
        return caches.match(event.request)
    })   
  );
});

importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var firebaseConfig = {
  apiKey: "AIzaSyD6-bz2yn3yBfrbVm5LltESnx3HXjaKUHc",
  authDomain: "floreriapetalos-4f75b.firebaseapp.com",
  databaseURL: "https://floreriapetalos-4f75b.firebaseio.com",
  projectId: "floreriapetalos-4f75b",
  storageBucket: "floreriapetalos-4f75b.appspot.com",
  messagingSenderId: "922558372819",
  appId: "1:922558372819:web:b896bd32716a475c3f6d26"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

let messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function(payload){
  console.log("Ha llegado notificacion");
  let title = payload.notification.title;

  let options = {
    body: payload.notification.body,
    icon: payload.notification.icon
  }

  self.registration.showNotification(title, options);
});