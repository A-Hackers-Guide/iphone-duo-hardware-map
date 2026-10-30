# `WiFiAirportInfoSource`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"CoreTelephonyClient" _coreTelephonyClient;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"CoreTelephonyClient",&,N,V_coreTelephonyClient) coreTelephonyClient;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
```

## Instance methods

```
-[WiFiAirportInfoSource setCoreTelephonyClient:];
-[WiFiAirportInfoSource coreTelephonyClient];
-[WiFiAirportInfoSource init];
-[WiFiAirportInfoSource queue];
-[WiFiAirportInfoSource setQueue:];
-[WiFiAirportInfoSource fetchAllDestinationAirportLocationsWithCompletionHandler:];
```
