# `WAPCStoreSize`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _storeNeedsPruning;
B _noError;
@"NSNumber" _currentSize;
Q _limit;
```

## Properties

```
@property (TB,V_storeNeedsPruning) storeNeedsPruning;
@property (T@"NSNumber",&,V_currentSize) currentSize;
@property (TQ,V_limit) limit;
@property (TB,V_noError) noError;
```

## Instance methods

```
-[WAPCStoreSize limit];
-[WAPCStoreSize description];
-[WAPCStoreSize setLimit:];
-[WAPCStoreSize currentSize];
-[WAPCStoreSize setCurrentSize:];
-[WAPCStoreSize noError];
-[WAPCStoreSize initWithMaxStoreSize:];
-[WAPCStoreSize setNoError:];
-[WAPCStoreSize setStoreNeedsPruning:];
-[WAPCStoreSize storeNeedsPruning];
```
