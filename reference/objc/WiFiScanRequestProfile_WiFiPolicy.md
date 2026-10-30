# `WiFiScanRequestProfile`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
s _motionState;
I _attemptsWithZeroResult;
@"NSMutableSet" _scanResultCache;
@"WiFiSoftError" _softError;
```

## Properties

```
@property (T@"NSMutableSet",&,N,V_scanResultCache) scanResultCache;
@property (Ts,N,V_motionState) motionState;
@property (TI,N,V_attemptsWithZeroResult) attemptsWithZeroResult;
@property (T@"WiFiSoftError",&,N,V_softError) softError;
```

## Instance methods

```
-[WiFiScanRequestProfile motionState];
-[WiFiScanRequestProfile resetCache];
-[WiFiScanRequestProfile handleScanRequest:andResult:];
-[WiFiScanRequestProfile setMotionState:];
-[WiFiScanRequestProfile initWithSoftError:];
-[WiFiScanRequestProfile scanResultCache];
-[WiFiScanRequestProfile attemptsWithZeroResult];
-[WiFiScanRequestProfile handleMotionStateChange:];
-[WiFiScanRequestProfile handleScanRequest:andResult:forClient:];
-[WiFiScanRequestProfile raiseABCForClient:withEvent:];
-[WiFiScanRequestProfile setAttemptsWithZeroResult:];
-[WiFiScanRequestProfile setScanResultCache:];
-[WiFiScanRequestProfile setSoftError:];
-[WiFiScanRequestProfile softError];
```
