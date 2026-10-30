# `BLSBacklightStateObservable` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `BLSDisplaySpecifying`
- 0 instance variables, 5 properties, 7 instance methods, 0 class methods

## Properties

```
@property (Tq,R,N) backlightState;
@property (Tq,R,N) flipbookState;
@property (TB,R,N,GisTransitioning) transitioning;
@property (TB,R,N,GisAlwaysOnEnabled) alwaysOnEnabled;
@property (TB,R,N) deviceSupportsAlwaysOn;
```

## Instance methods

```
-[BLSBacklightStateObservable deviceSupportsAlwaysOn];
-[BLSBacklightStateObservable isAlwaysOnEnabled];
-[BLSBacklightStateObservable removeObserver:];
-[BLSBacklightStateObservable isTransitioning];
-[BLSBacklightStateObservable flipbookState];
-[BLSBacklightStateObservable addObserver:];
-[BLSBacklightStateObservable backlightState];
```
