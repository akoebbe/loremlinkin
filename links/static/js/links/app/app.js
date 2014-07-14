'use strict';

var LoremLinkinApp = angular.module('LoremLinkinApp', [
  'ngCookies',
  'ngAnimate',
  'ngSanitize',
  'LoremLinkinControllers',
  'LoremLinkinServices',
  'xeditable'
]).config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});;

LoremLinkinApp.run(function($rootScope, $http, $cookies) {
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});