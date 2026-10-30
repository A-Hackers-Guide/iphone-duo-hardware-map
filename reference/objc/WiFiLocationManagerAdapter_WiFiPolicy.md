# `WiFiLocationManagerAdapter`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiLocationProtocol`, `WiFiLocationManagerDelegate`
- 2 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"WiFiLocationManager" _locationManager;
@? _locationHandler;
```

## Properties

```
@property (T@"WiFiLocationManager",&,N,V_locationManager) locationManager;
@property (T@?,C,N,V_locationHandler) locationHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WiFiLocationManagerAdapter setLocationManager:];
-[WiFiLocationManagerAdapter didFailWithError:];
-[WiFiLocationManagerAdapter locationManager];
-[WiFiLocationManagerAdapter init];
-[WiFiLocationManagerAdapter didUpdateLocations:];
-[WiFiLocationManagerAdapter description];
-[WiFiLocationManagerAdapter stopLocationUpdates];
-[WiFiLocationManagerAdapter locationHandler];
-[WiFiLocationManagerAdapter setLocationHandler:];
-[WiFiLocationManagerAdapter startLocationUpdatesWithHandler:];
```
