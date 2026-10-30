# `BLSHWatchdogProviderDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 1 properties, 6 instance methods, 0 class methods

## Properties

```
@property (TB,?,R,N,GisTesting) testing;
```

## Instance methods

```
-[BLSHWatchdogProviderDelegate abortForWatchdog:payload:payloadSize:explanation:];
-[BLSHWatchdogProviderDelegate isTailspinAvailable];
-[BLSHWatchdogProviderDelegate writeTailspinForWatchdog:completion:];
-[BLSHWatchdogProviderDelegate panicForWatchdog:withDelay:completion:];
-[BLSHWatchdogProviderDelegate isTesting];
-[BLSHWatchdogProviderDelegate didFinishDumpingStateForWatchdog:];
```
