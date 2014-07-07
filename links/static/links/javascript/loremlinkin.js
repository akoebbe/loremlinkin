angular.module("LoremLinkin", ["xeditable"]).config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

function LoremLinkinCtrl($scope) {
  $scope.link = {
    title: "Here's my page",
    description: "This is just a placeholder page",
    bgColor: "#ff8888"
  }
}