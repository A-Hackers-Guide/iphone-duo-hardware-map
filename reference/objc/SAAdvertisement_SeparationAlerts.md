# `SAAdvertisement`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSDate" _scanDate;
q _rssi;
q _batteryState;
```

## Properties

```
@property (T@"NSDate",R,C,N,V_scanDate) scanDate;
@property (Tq,R,N,V_rssi) rssi;
@property (Tq,R,N,V_batteryState) batteryState;
```

## Instance methods

```
-[SAAdvertisement rssi];
-[SAAdvertisement batteryState];
-[SAAdvertisement scanDate];
-[SAAdvertisement clearSensitiveFields];
-[SAAdvertisement initWithAdvertisement:];
```
