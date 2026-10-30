# `BLSHSystemActivityAssertionConfiguration`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHSystemActivityAssertionConfiguring`
- 3 instance variables, 7 properties, 6 instance methods, 0 class methods

## Instance variables

```
B _acquireWaitsToAbortSleepRequested;
B _acquireWaitsToAbortSleepImminent;
@"<BLSHOSInterfaceProviding>" _osInterfaceProvider;
```

## Properties

```
@property (T@"<BLSHOSInterfaceProviding>",W,N,SsetOSInterfaceProvider:,V_osInterfaceProvider) osInterfaceProvider;
@property (TB,N,V_acquireWaitsToAbortSleepRequested) acquireWaitsToAbortSleepRequested;
@property (TB,N,V_acquireWaitsToAbortSleepImminent) acquireWaitsToAbortSleepImminent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHSystemActivityAssertionConfiguration setAcquireWaitsToAbortSleepRequested:];
-[BLSHSystemActivityAssertionConfiguration setAcquireWaitsToAbortSleepImminent:];
-[BLSHSystemActivityAssertionConfiguration osInterfaceProvider];
-[BLSHSystemActivityAssertionConfiguration acquireWaitsToAbortSleepImminent];
-[BLSHSystemActivityAssertionConfiguration acquireWaitsToAbortSleepRequested];
-[BLSHSystemActivityAssertionConfiguration setOSInterfaceProvider:];
```
