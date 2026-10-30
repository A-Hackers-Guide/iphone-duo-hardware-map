# `BLSBacklightProxyObservation`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"<BLSBacklightStateObserving>" _observer;
@"<BLSBacklightStateObservable>" _backlight;
```

## Properties

```
@property (T@"<BLSBacklightStateObserving>",R,W,N,V_observer) observer;
@property (T@"<BLSBacklightStateObservable>",R,W,N,V_backlight) backlight;
```

## Class methods

```
+[BLSBacklightProxyObservation observationForObserver:backlight:];
```

## Instance methods

```
-[BLSBacklightProxyObservation observer];
-[BLSBacklightProxyObservation description];
-[BLSBacklightProxyObservation backlight];
-[BLSBacklightProxyObservation backlightForProxy:];
-[BLSBacklightProxyObservation initWithObserver:backlight:];
```
