'use strict';

/* Controllers */

var LoremLinkinControllers = angular.module 'LoremLinkinControllers', [];

LoremLinkinControllers.controller('LLCtrl', ['$scope', '$log', 'Link',

  function($scope, $log, Link) {
    $scope.link = Link.create();


    $scope.link_save = function() {
       Link.save($scope.link);
    };

  }]);