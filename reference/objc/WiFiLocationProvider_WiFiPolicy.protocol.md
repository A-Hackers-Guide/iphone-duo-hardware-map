# `WiFiLocationProvider` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `WiFiContextProvider`
- 0 instance variables, 3 properties, 5 instance methods, 0 class methods

## Properties

```
@property (TB,R,N) isAuthorized;
@property (T@"CLLocation",R,N) currentLocation;
@property (T@?,C,N) locationChangedCallback;
```

## Instance methods

```
-[WiFiLocationProvider currentLocation];
-[WiFiLocationProvider isAuthorized];
-[WiFiLocationProvider locationChangedCallback];
-[WiFiLocationProvider requestHighAccuracyLocation:];
-[WiFiLocationProvider setLocationChangedCallback:];
```
