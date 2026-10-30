# `CLCondition`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 8 instance variables, 9 properties, 27 instance methods, 1 class methods

## Instance variables

```
B _isMonitoring;
@"CLClientKeyPath" _ckp;
@"NSString" _identifier;
@"CLClientManagerAuthorizationContext" _authorizationContext;
@? _onConditionUpdateCallbackHandler;
@"<CLIntersiloUniverse>" _universe;
@"CLCondition" _refinement;
Q _lastMonitoringState;
```

## Properties

```
@property (T@"CLClientKeyPath",&,N,V_ckp) ckp;
@property (T@"NSString",&,N,V_identifier) identifier;
@property (T@"NSString",R) monitoredIdentifier;
@property (T@"CLClientManagerAuthorizationContext",&,N,V_authorizationContext) authorizationContext;
@property (T@?,C,N,V_onConditionUpdateCallbackHandler) onConditionUpdateCallbackHandler;
@property (T@"<CLIntersiloUniverse>",N,V_universe) universe;
@property (T@"CLCondition",&,N,V_refinement) refinement;
@property (TQ,N,V_lastMonitoringState) lastMonitoringState;
@property (TB,N,V_isMonitoring) isMonitoring;
```

## Class methods

```
+[CLCondition supportsSecureCoding];
```

## Instance methods

```
-[CLCondition startMonitoring];
-[CLCondition isMonitoring];
-[CLCondition identifier];
-[CLCondition setAuthorizationContext:];
-[CLCondition authorizationContext];
-[CLCondition copy];
-[CLCondition dealloc];
-[CLCondition stopMonitoring];
-[CLCondition setIdentifier:];
-[CLCondition encodeWithCoder:];
-[CLCondition initWithCoder:];
-[CLCondition copyWithZone:];
-[CLCondition isAuthorized];
-[CLCondition setIsMonitoring:];
-[CLCondition setCkp:];
-[CLCondition ckp];
-[CLCondition initCondition];
-[CLCondition lastMonitoringState];
-[CLCondition monitoredIdentifier];
-[CLCondition onConditionUpdateCallbackHandler];
-[CLCondition refinement];
-[CLCondition setCallbackHandler:];
-[CLCondition setLastMonitoringState:];
-[CLCondition setOnConditionUpdateCallbackHandler:];
-[CLCondition setRefinement:];
-[CLCondition setUniverse:];
-[CLCondition universe];
```
