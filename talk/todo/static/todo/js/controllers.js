var TodoControllers = angular.module('TodoControllers', []);

TodoControllers.controller('TodoListCtrl', ['$scope', '$pusher', function ($scope, $pusher) {
    $scope.todoList = {};
    $scope.todoItems = [];

    var client = new Pusher("895dec4d68d4e286a48d");
    var pusher = $pusher(client);
    var todo_items_channel = pusher.subscribe('todo-item');
    todo_items_channel.bind('updated',
        function(data) {
            for(var i=0; i < $scope.todoItems.length; i++) {
                if($scope.todoItems[i].id == data.id) {
                    $scope.todoItems[i] = data;
                    return;
                }
            }
        }
    );
    todo_items_channel.bind('created',
        function(data) {
            console.log(data);
            $scope.todoItems.push(data);
        }
    );
    todo_items_channel.bind('deleted',
        function(data) {
            for(var i=$scope.todoItems.length-1; i >= 0; i--) {
                if($scope.todoItems[i].id === data.id) {
                    $scope.todoItems.splice(i, 1);
                    return;
                }
            }
        }
    );
}]);