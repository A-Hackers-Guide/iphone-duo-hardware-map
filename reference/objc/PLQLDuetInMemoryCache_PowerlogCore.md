# `PLQLDuetInMemoryCache`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 27 instance methods, 0 class methods

## Instance variables

```
i _refCount;
@"NSDictionary" _startArgs;
@"NSDictionary" _stopArgs;
d _startTime;
d _stopTime;
d _cellIn;
d _cellOut;
d _wifiIn;
d _wifiOut;
```

## Properties

```
@property (T@"NSDictionary",&,V_startArgs) startArgs;
@property (T@"NSDictionary",&,V_stopArgs) stopArgs;
@property (Td,V_startTime) startTime;
@property (Td,V_stopTime) stopTime;
@property (Td,V_cellIn) cellIn;
@property (Td,V_cellOut) cellOut;
@property (Td,V_wifiIn) wifiIn;
@property (Td,V_wifiOut) wifiOut;
@property (Ti,V_refCount) refCount;
```

## Instance methods

```
-[PLQLDuetInMemoryCache init];
-[PLQLDuetInMemoryCache startTime];
-[PLQLDuetInMemoryCache stopTime];
-[PLQLDuetInMemoryCache refCount];
-[PLQLDuetInMemoryCache setStartTime:];
-[PLQLDuetInMemoryCache setRefCount:];
-[PLQLDuetInMemoryCache setStopTime:];
-[PLQLDuetInMemoryCache wifiOut];
-[PLQLDuetInMemoryCache cellOut];
-[PLQLDuetInMemoryCache addDataWithCellIn:withCellOut:withWifiIn:withWifiOut:];
-[PLQLDuetInMemoryCache addStartEvent:withArgs:];
-[PLQLDuetInMemoryCache addStopEvent:withArgs:];
-[PLQLDuetInMemoryCache cellIn];
-[PLQLDuetInMemoryCache clearStop];
-[PLQLDuetInMemoryCache initWithStartTime:withStartargs:];
-[PLQLDuetInMemoryCache isStartPresent];
-[PLQLDuetInMemoryCache isStopPresent];
-[PLQLDuetInMemoryCache setCellIn:];
-[PLQLDuetInMemoryCache setCellOut:];
-[PLQLDuetInMemoryCache setStartArgs:];
-[PLQLDuetInMemoryCache setStopArgs:];
-[PLQLDuetInMemoryCache setWifiIn:];
-[PLQLDuetInMemoryCache setWifiOut:];
-[PLQLDuetInMemoryCache startArgs];
-[PLQLDuetInMemoryCache stopArgs];
-[PLQLDuetInMemoryCache updateDataStats:];
-[PLQLDuetInMemoryCache wifiIn];
```
