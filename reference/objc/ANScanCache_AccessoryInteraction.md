# `ANScanCache`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _scanCache;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_scanCache) scanCache;
```

## Instance methods

```
-[ANScanCache scanCache];
-[ANScanCache init];
-[ANScanCache dealloc];
-[ANScanCache clearData];
-[ANScanCache setScanCache:];
-[ANScanCache addScanResultAtDate:address:reason:uuid:];
-[ANScanCache getAddressForUuid:];
-[ANScanCache getReasonForUuid:];
-[ANScanCache pruneAggregatedResults];
-[ANScanCache secondsFromLastQuarterHour];
```
