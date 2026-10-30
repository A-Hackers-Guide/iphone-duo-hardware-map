# `WFMetricsManager`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSString" _processName;
@"NSMutableDictionary" _ssidHashes;
```

## Properties

```
@property (T@"NSString",C,N,V_processName) processName;
@property (T@"NSMutableDictionary",&,N,V_ssidHashes) ssidHashes;
```

## Class methods

```
+[WFMetricsManager sharedManager];
```

## Instance methods

```
-[WFMetricsManager setProcessName:];
-[WFMetricsManager init];
-[WFMetricsManager processName];
-[WFMetricsManager processEvent:];
-[WFMetricsManager _submitCAEvent:];
-[WFMetricsManager setSsidHashes:];
-[WFMetricsManager ssidHashes];
```
