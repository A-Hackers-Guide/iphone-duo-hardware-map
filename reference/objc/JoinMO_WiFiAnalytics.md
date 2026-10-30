# `JoinMO`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EventMO`
- 0 instance variables, 13 properties, 2 instance methods, 1 class methods

## Properties

```
@property (T@"NSString",C,D,N) apProfileID;
@property (Ti,D,N) dhcpLatencyMs;
@property (Ti,D,N) dhcpLeaseMins;
@property (TB,D,N) dhcpSuccess;
@property (Ti,D,N) ipv4Addr;
@property (Ti,D,N) ipv4routerAddr;
@property (TB,D,N) isUsrPreference;
@property (Ts,D,N) networkAuthFlags;
@property (Ti,D,N) networkFlags;
@property (TB,D,N) networkIsHome;
@property (TB,D,N) networkIsWork;
@property (T@"NSString",C,D,N) routerMAC;
@property (Ts,D,N) snr;
```

## Class methods

```
+[JoinMO fetchRequest];
```

## Instance methods

```
-[JoinMO description];
-[JoinMO attributeDescription:];
```
