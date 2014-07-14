'use strict';

var LoremLinkinServices = angular.module('LoremLinkinServices', []); // ,['ngResource']);

LoremLinkinServices.factory('Link', ['$log', '$http', 'urls',
  function($log, $http, urls){
    return {
        create: function() {
            return { title: '', description: '' }
        },
        save: function(link) {
            return $http.post(urls.link_save, link).then(function(data) {
                $log.log(data);
                return data.data;
            });
        },

    }

  }]);