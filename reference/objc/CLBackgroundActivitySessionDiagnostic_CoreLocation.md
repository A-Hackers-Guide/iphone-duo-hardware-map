# `CLBackgroundActivitySessionDiagnostic`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 6 properties, 8 instance methods, 0 class methods

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
@property (TB,R,N) authorizationRequestInProgress;
```

## Instance methods

```
-[CLBackgroundActivitySessionDiagnostic dealloc];
-[CLBackgroundActivitySessionDiagnostic authorizationDenied];
-[CLBackgroundActivitySessionDiagnostic authorizationDeniedGlobally];
-[CLBackgroundActivitySessionDiagnostic authorizationRequestInProgress];
-[CLBackgroundActivitySessionDiagnostic authorizationRestricted];
-[CLBackgroundActivitySessionDiagnostic initWithDiagnostics:];
-[CLBackgroundActivitySessionDiagnostic insufficientlyInUse];
-[CLBackgroundActivitySessionDiagnostic serviceSessionRequired];
```
