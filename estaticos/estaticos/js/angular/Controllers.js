miapp=angular.module('MyApp.controllers', []);

miapp.controller('controlador', function ($scope) {
         $scope.mensaje="deiner";
  });

miapp.controller('json', function($scope, $http) {
    $http.get("http://www.w3schools.com/angular/customers.php")
    .success(function(response) {
            $scope.names = response.records;
        });
});

miapp.controller('json1', function($scope, $http) {
    $http.get("https://restcountries.eu/rest/v1/all")
    .success(function(response) {
            $scope.name = response;
        });
});