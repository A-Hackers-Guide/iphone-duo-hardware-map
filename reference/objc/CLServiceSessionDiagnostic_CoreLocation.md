# `CLServiceSessionDiagnostic`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 8 properties, 11 instance methods, 0 class methods

## Instance variables

```
Q _diagnostics;
```

## Properties

```
@property (TB,R,N) authorizationDenied;
@property (TB,R,N) authorizationDeniedGlobally;
@property (TB,R,N) authorizationRestricted;
@property (TB,R,N) insufficientlyInUse;
@property (TB,R,N) serviceSessionRequired;
@property (TB,R,N) fullAccuracyDenied;
@property (TB,R,N) alwaysAuthorizationDenied;
@property (TB,R,N) authorizationRequestInProgress;
```

## Instance methods

```
-[CLServiceSessionDiagnostic dealloc];
-[CLServiceSessionDiagnostic alwaysAuthorizationDenied];
-[CLServiceSessionDiagnostic authorizationDenied];
-[CLServiceSessionDiagnostic authorizationDeniedGlobally];
-[CLServiceSessionDiagnostic authorizationRequestInProgress];
-[CLServiceSessionDiagnostic authorizationRestricted];
-[CLServiceSessionDiagnostic diagnosticMask];
-[CLServiceSessionDiagnostic fullAccuracyDenied];
-[CLServiceSessionDiagnostic initWithDiagnostics:];
-[CLServiceSessionDiagnostic insufficientlyInUse];
-[CLServiceSessionDiagnostic serviceSessionRequired];
```
