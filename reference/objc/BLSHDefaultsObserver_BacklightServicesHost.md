# `BLSHDefaultsObserver`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 3 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSUserDefaults" _observedDefaults;
@"NSMapTable" _handlers;
B _invalidated;
```

## Properties

```
@property (TB,V_invalidated) invalidated;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHDefaultsObserver observeValueForKeyPath:ofObject:change:context:];
-[BLSHDefaultsObserver invalidated];
-[BLSHDefaultsObserver init];
-[BLSHDefaultsObserver dealloc];
-[BLSHDefaultsObserver setInvalidated:];
-[BLSHDefaultsObserver invalidate];
-[BLSHDefaultsObserver addHandlerForKey:attributes:];
```
