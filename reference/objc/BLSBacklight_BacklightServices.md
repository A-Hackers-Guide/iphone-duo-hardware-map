# `BLSBacklight`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSBacklightStateObservable`, `BLSBacklightChangeRequestable`
- 2 instance variables, 10 properties, 11 instance methods, 4 class methods

## Instance variables

```
@"<BLSBacklightProxy>" _backlightProxy;
@"<BLSDisplay>" _display;
```

## Properties

```
@property (Tq,R,N) backlightState;
@property (Tq,R,N) flipbookState;
@property (TB,R,N,GisTransitioning) transitioning;
@property (TB,R,N,GisAlwaysOnEnabled) alwaysOnEnabled;
@property (TB,R,N) deviceSupportsAlwaysOn;
@property (T@"<BLSDisplay>",R,N) display;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSBacklight backlightProxyForDisplay:];
+[BLSBacklight sharedBacklightForDisplay:];
+[BLSBacklight sharedBacklight];
+[BLSBacklight setBacklightProxy:forDisplay:];
```

## Instance methods

```
-[BLSBacklight display];
-[BLSBacklight deviceSupportsAlwaysOn];
-[BLSBacklight isAlwaysOnEnabled];
-[BLSBacklight initForDisplay:];
-[BLSBacklight removeObserver:];
-[BLSBacklight init];
-[BLSBacklight isTransitioning];
-[BLSBacklight performChangeRequest:];
-[BLSBacklight flipbookState];
-[BLSBacklight addObserver:];
-[BLSBacklight backlightState];
```
