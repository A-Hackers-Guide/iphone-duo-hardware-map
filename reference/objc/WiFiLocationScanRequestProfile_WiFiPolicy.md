# `WiFiLocationScanRequestProfile`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiScanRequestProfile`
- 2 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSDate" _penultimateScanRequestTime;
@"NSDate" _ultimateScanRequestTime;
```

## Properties

```
@property (T@"NSDate",&,N,V_penultimateScanRequestTime) penultimateScanRequestTime;
@property (T@"NSDate",&,N,V_ultimateScanRequestTime) ultimateScanRequestTime;
```

## Instance methods

```
-[WiFiLocationScanRequestProfile penultimateScanRequestTime];
-[WiFiLocationScanRequestProfile setUltimateScanRequestTime:];
-[WiFiLocationScanRequestProfile handleScanRequest:andResult:];
-[WiFiLocationScanRequestProfile ultimateScanRequestTime];
-[WiFiLocationScanRequestProfile initWithSoftError:];
-[WiFiLocationScanRequestProfile raiseABCForInterval:];
-[WiFiLocationScanRequestProfile setPenultimateScanRequestTime:];
```
