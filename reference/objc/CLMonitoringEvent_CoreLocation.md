# `CLMonitoringEvent`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 15 properties, 24 instance methods, 1 class methods

## Instance variables

```
B _authorizationRequestInProgress;
@"NSString" _identifier;
@"CLCondition" _refinement;
Q _state;
@"NSDate" _date;
Q _diagnosticMask;
```

## Properties

```
@property (TQ,R,N,V_diagnosticMask) diagnosticMask;
@property (T@"NSString",R,V_identifier) identifier;
@property (T@"CLCondition",R,V_refinement) refinement;
@property (TQ,R,N,V_state) state;
@property (T@"NSDate",R,V_date) date;
@property (TB,R,N) authorizationDenied;
@property (TB,R,N) authorizationDeniedGlobally;
@property (TB,R,N) authorizationRestricted;
@property (TB,R,N) insufficientlyInUse;
@property (TB,R,N) accuracyLimited;
@property (TB,R,N) conditionUnsupported;
@property (TB,R,N) conditionLimitExceeded;
@property (TB,R,N) persistenceUnavailable;
@property (TB,R,N) serviceSessionRequired;
@property (TB,R,N,V_authorizationRequestInProgress) authorizationRequestInProgress;
```

## Class methods

```
+[CLMonitoringEvent supportsSecureCoding];
```

## Instance methods

```
-[CLMonitoringEvent setState:];
-[CLMonitoringEvent identifier];
-[CLMonitoringEvent dealloc];
-[CLMonitoringEvent date];
-[CLMonitoringEvent encodeWithCoder:];
-[CLMonitoringEvent description];
-[CLMonitoringEvent initWithCoder:];
-[CLMonitoringEvent copyWithZone:];
-[CLMonitoringEvent state];
-[CLMonitoringEvent accuracyLimited];
-[CLMonitoringEvent authorizationDenied];
-[CLMonitoringEvent authorizationDeniedGlobally];
-[CLMonitoringEvent authorizationRequestInProgress];
-[CLMonitoringEvent authorizationRestricted];
-[CLMonitoringEvent conditionLimitExceeded];
-[CLMonitoringEvent conditionUnsupported];
-[CLMonitoringEvent diagnosticMask];
-[CLMonitoringEvent initWithIdentifier:refinement:state:date:diagnostics:];
-[CLMonitoringEvent insufficientlyInUse];
-[CLMonitoringEvent persistenceUnavailable];
-[CLMonitoringEvent refinement];
-[CLMonitoringEvent serviceSessionRequired];
-[CLMonitoringEvent updateDiagnosticMask:];
-[CLMonitoringEvent updateMonitoringState:];
```
