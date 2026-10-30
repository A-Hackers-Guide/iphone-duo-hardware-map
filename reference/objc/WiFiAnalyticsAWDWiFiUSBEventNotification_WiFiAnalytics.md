# `WiFiAnalyticsAWDWiFiUSBEventNotification`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 10 properties, 29 instance methods, 0 class methods

## Instance variables

```
Q _durationSinceUSBEventInSeconds;
I _usbAction;
I _usbTotal;
B _isVendorApple;
B _smartCCADesenseSupported;
{?="durationSinceUSBEventInSeconds"b1"usbAction"b1"usbTotal"b1"isVendorApple"b1"smartCCADesenseSupported"b1} _has;
```

## Properties

```
@property (TB,N) hasUsbAction;
@property (TI,N,V_usbAction) usbAction;
@property (TB,N) hasUsbTotal;
@property (TI,N,V_usbTotal) usbTotal;
@property (TB,N) hasDurationSinceUSBEventInSeconds;
@property (TQ,N,V_durationSinceUSBEventInSeconds) durationSinceUSBEventInSeconds;
@property (TB,N) hasIsVendorApple;
@property (TB,N,V_isVendorApple) isVendorApple;
@property (TB,N) hasSmartCCADesenseSupported;
@property (TB,N,V_smartCCADesenseSupported) smartCCADesenseSupported;
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiUSBEventNotification writeTo:];
-[WiFiAnalyticsAWDWiFiUSBEventNotification mergeFrom:];
-[WiFiAnalyticsAWDWiFiUSBEventNotification hash];
-[WiFiAnalyticsAWDWiFiUSBEventNotification copyTo:];
-[WiFiAnalyticsAWDWiFiUSBEventNotification description];
-[WiFiAnalyticsAWDWiFiUSBEventNotification readFrom:];
-[WiFiAnalyticsAWDWiFiUSBEventNotification copyWithZone:];
-[WiFiAnalyticsAWDWiFiUSBEventNotification isEqual:];
-[WiFiAnalyticsAWDWiFiUSBEventNotification dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiUSBEventNotification setHasSmartCCADesenseSupported:];
-[WiFiAnalyticsAWDWiFiUSBEventNotification setHasUsbTotal:];
-[WiFiAnalyticsAWDWiFiUSBEventNotification durationSinceUSBEventInSeconds];
-[WiFiAnalyticsAWDWiFiUSBEventNotification hasDurationSinceUSBEventInSeconds];
-[WiFiAnalyticsAWDWiFiUSBEventNotification hasIsVendorApple];
-[WiFiAnalyticsAWDWiFiUSBEventNotification hasSmartCCADesenseSupported];
-[WiFiAnalyticsAWDWiFiUSBEventNotification hasUsbAction];
-[WiFiAnalyticsAWDWiFiUSBEventNotification hasUsbTotal];
-[WiFiAnalyticsAWDWiFiUSBEventNotification isVendorApple];
-[WiFiAnalyticsAWDWiFiUSBEventNotification setDurationSinceUSBEventInSeconds:];
-[WiFiAnalyticsAWDWiFiUSBEventNotification setHasDurationSinceUSBEventInSeconds:];
-[WiFiAnalyticsAWDWiFiUSBEventNotification setHasIsVendorApple:];
-[WiFiAnalyticsAWDWiFiUSBEventNotification setHasUsbAction:];
-[WiFiAnalyticsAWDWiFiUSBEventNotification setIsVendorApple:];
-[WiFiAnalyticsAWDWiFiUSBEventNotification setSmartCCADesenseSupported:];
-[WiFiAnalyticsAWDWiFiUSBEventNotification setUsbAction:];
-[WiFiAnalyticsAWDWiFiUSBEventNotification setUsbTotal:];
-[WiFiAnalyticsAWDWiFiUSBEventNotification smartCCADesenseSupported];
-[WiFiAnalyticsAWDWiFiUSBEventNotification usbAction];
-[WiFiAnalyticsAWDWiFiUSBEventNotification usbTotal];
```
