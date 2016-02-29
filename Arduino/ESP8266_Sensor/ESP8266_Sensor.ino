#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include "environment.h"

#define ESP8266_LED 5

const char WiFiSSID[] = MY_WIFI_SSID;
const char WiFiPSK[] = MY_WIFI_PSK;

void initHardware();
void connectWiFi();

void setup()
{
  initHardware();
  connectWiFi();
}

void loop()
{
  delay(100);
}

void connectWiFi()
{
  byte ledStatus = LOW;

  // Set WiFi mode to station
  WiFi.mode(WIFI_STA);
  WiFi.begin(WiFiSSID, WiFiPSK);

  while (WiFi.status() != WL_CONNECTED)
  {
    // Blink the LED
    digitalWrite(ESP8266_LED, ledStatus);
    ledStatus = (ledStatus == HIGH) ? LOW : HIGH;
    delay(100);
  }

  digitalWrite(ESP8266_LED, LOW);
  delay(100);

  HTTPClient http;
  http.begin(MY_SERVER, 80, "/");
  
  int httpCode = http.POST("parameter=value&also=another");
  if(httpCode) {
     if(httpCode == 200) {
       digitalWrite(ESP8266_LED, HIGH);
     }
  }
}

void initHardware()
{
  pinMode(ESP8266_LED, OUTPUT);
  digitalWrite(ESP8266_LED, LOW);
}

