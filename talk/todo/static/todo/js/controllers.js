var TodoControllers = angular.module('TodoControllers', []);

TodoControllers.controller('TodoListCtrl', ['$scope', '$pusher', function ($scope, $pusher) {
    $scope.todoList = {};
    $scope.todoItems = [];

    var client = new Pusher("895dec4d68d4e286a48d");
    var pusher = $pusher(client);
    var my_channel = pusher.subscribe('todo-item');
    my_channel.bind('updated',
        function(data) {
            for(var i=0; i < $scope.todoItems.length; i++) {
                if($scope.todoItems[i].id == data.id) {
                    $scope.todoItems[i] = data;
                    return;
                }
            }
            $scope.todoItems.push(data);
        }
    );
}]);