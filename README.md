# Google Weather Api

![](https://img.shields.io/badge/Python-3-green.svg?style=for-the-badge&logo=python)
![](https://img.shields.io/badge/api-v1-purple.svg?style=for-the-badge&logo=heroku)

Actually, it is the api for [weather.com](https://weather.com/en-IN/) that google uses to show weather.

#### Api endpoints : 
- For getting the weather of a place : 
    ```shell
    https://google-weather-api.herokuapp.com/place/<cityName>
    ```
- For getting gps coordinates of a place : 
    ```shell
    https://google-weather-api.herokuapp.com/cr/<cityName>
    ```
- For getting weather for a given coordinates : 
    ```shell
    https://google-weather-api.herokuapp.com/place/cr/<gpsCoordinates>
    ```
For eg. 
```shell
https://google-weather-api.herokuapp.com/cr/delhi
```

```shell
https://google-weather-api.herokuapp.com/place/cr/22.307,73.181
```

#### TODO:

- get the weather icons
 