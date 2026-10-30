# `BLSPendingBacklightProxy`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSBacklightProxy`
- 6 instance variables, 10 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _requests;
@"NSMapTable" _observations;
@"<BLSBacklightProxy>" _replacementBacklightProxy;
@"<BLSDisplay>" _display;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
q _backlightState;
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

## Instance methods

```
-[BLSPendingBacklightProxy display];
-[BLSPendingBacklightProxy deviceSupportsAlwaysOn];
-[BLSPendingBacklightProxy isAlwaysOnEnabled];
-[BLSPendingBacklightProxy initForDisplay:];
-[BLSPendingBacklightProxy removeObserver:];
-[BLSPendingBacklightProxy isTransitioning];
-[BLSPendingBacklightProxy performChangeRequest:];
-[BLSPendingBacklightProxy flipbookState];
-[BLSPendingBacklightProxy addObserver:];
-[BLSPendingBacklightProxy backlightState];
-[BLSPendingBacklightProxy addObserver:forBacklight:];
-[BLSPendingBacklightProxy replaceWithBacklightProxy:];
```
