ymaps.ready(['util.calculateArea']).then(init);

var polygon ;

function init () {
var myMap = new ymaps.Map('map', {
    center: [51.8872669, 95.6260172],
    zoom: 9,
    controls: ['default', 'routeButtonControl']

}, {
    searchControlProvider: 'yandex#search'
},
 {
    // Опции.
    // Необходимо указать данный тип макета.
    iconLayout: 'default#imageWithContent',
    // Своё изображение иконки метки.
    iconImageHref: 'images/ball.png',
    // Размеры метки.
    iconImageSize: [48, 48],
    // Смещение левого верхнего угла иконки относительно
    // её "ножки" (точки привязки).
    iconImageOffset: [-24, -24],
    // Смещение слоя с содержимым относительно слоя с картинкой.
    iconContentOffset: [15, 15],
    // Макет содержимого.

}
),
        polygon = new ymaps.Polygon([], {}, {
            // Курсор в режиме добавления новых вершин.
            editorDrawingCursor: "crosshair",
            // Максимально допустимое количество вершин.
            //editorMaxPoints: 5,
            // Цвет заливки.
            //fillColor: '#00FF00',
            // Цвет обводки.
            strokeColor: '#0000FF',
            // Ширина обводки.
            strokeWidth: 5
        });
myPlacemark = new ymaps.Placemark(myMap.getCenter());

myMap.geoObjects.add(myPlacemark);
myMap.geoObjects.add(polygon);
polygon.editor.startDrawing();


polygon.events.add([
    'mapchange', 'geometrychange', 'pixelgeometrychange', 'optionschange', 'propertieschange',
    'balloonopen', 'balloonclose', 'hintopen', 'hintclose', 'dragstart', 'dragend'
], function (e) {
    console.log('@' + e.get('type'));
});


$('input').attr('disabled', false);

    // Обработка нажатия на любую кнопку.
    $('input').click(
        function () {
            // Отключаем кнопки, чтобы на карту нельзя было
            // добавить более одного редактируемого объекта (чтобы в них не запутаться).
            $('input').attr('disabled', true);

            polygon.editor.stopEditing();

            area = ymaps.util.calculateArea(polygon)

            console.log(area)

            polygon.properties.set('balloonContent', area);

            printGeometry(polygon.geometry.getCoordinates());

            console.log(polygon.geometry)

        });


}

// Выводит массив координат геообъекта в <div id="geometry">
function printGeometry (coords) {
    console.log(coords);

    $('#geometry').html('Координаты: ' + stringify(coords));

    function stringify (coords) {
        var res = '';
        if ($.isArray(coords)) {
            res = '[ ';
            for (var i = 0, l = coords.length; i < l; i++) {
                if (i > 0) {
                    res += ', ';
                }
                res += stringify(coords[i]);
            }
            res += ' ]';
        } else if (typeof coords == 'number') {
            res = coords.toPrecision(6);
        } else if (coords.toString) {
            res = coords.toString();
        }

        return res;
    }
}
