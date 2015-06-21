 var my_app=angular.module('MyApp',['MyApp.controllers']).config(function ($interpolateProvider) {
             $interpolateProvider.startSymbol('[[');
  		     $interpolateProvider.endSymbol(']]');

          });
