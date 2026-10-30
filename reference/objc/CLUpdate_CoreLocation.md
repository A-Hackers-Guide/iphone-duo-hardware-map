# `CLUpdate`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 11 properties, 13 instance methods, 0 class methods

## Instance variables

```
Q _diagnostics;
@"CLLocation" _location;
```

## Properties

```
@property (TB,R,N) authorizationDenied;
@property (TB,R,N) authorizationDeniedGlobally;
@property (TB,R,N) authorizationRestricted;
@property (TB,R) isStationary;
@property (TB,R) stationary;
@property (TB,R,N) insufficientlyInUse;
@property (TB,R,N) locationUnavailable;
@property (TB,R,N) accuracyLimited;
@property (TB,R,N) serviceSessionRequired;
@property (TB,R,N) authorizationRequestInProgress;
@property (T@"CLLocation",R,N,V_location) location;
```

## Instance methods

```
-[CLUpdate location];
-[CLUpdate dealloc];
-[CLUpdate isStationary];
-[CLUpdate stationary];
-[CLUpdate accuracyLimited];
-[CLUpdate authorizationDenied];
-[CLUpdate authorizationDeniedGlobally];
-[CLUpdate authorizationRequestInProgress];
-[CLUpdate authorizationRestricted];
-[CLUpdate initWithLocation:diagnostics:];
-[CLUpdate insufficientlyInUse];
-[CLUpdate locationUnavailable];
-[CLUpdate serviceSessionRequired];
```
