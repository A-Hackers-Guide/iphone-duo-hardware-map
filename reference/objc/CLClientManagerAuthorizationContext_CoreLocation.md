# `CLClientManagerAuthorizationContext`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _authorizedForWidgetUpdates;
i _transientAwareRegistrationResult;
i _registrationResult;
i _inUseLevel;
Q _diagnosticMask;
Q _staticServiceMask;
Q _effectiveServiceMask;
Q _provisionalServiceMask;
```

## Properties

```
@property (TQ,R,N,V_staticServiceMask) staticServiceMask;
@property (TQ,R,N,V_effectiveServiceMask) effectiveServiceMask;
@property (TQ,R,N,V_provisionalServiceMask) provisionalServiceMask;
@property (Ti,R,N,V_transientAwareRegistrationResult) transientAwareRegistrationResult;
@property (Ti,R,N,V_registrationResult) registrationResult;
@property (TB,R,N,V_authorizedForWidgetUpdates) authorizedForWidgetUpdates;
@property (Ti,R,N,V_inUseLevel) inUseLevel;
@property (TQ,R,N,V_diagnosticMask) diagnosticMask;
```

## Instance methods

```
-[CLClientManagerAuthorizationContext getStateSummary];
-[CLClientManagerAuthorizationContext description];
-[CLClientManagerAuthorizationContext isEqual:];
-[CLClientManagerAuthorizationContext registrationResult];
-[CLClientManagerAuthorizationContext isAuthorizedForServiceTypeMask:];
-[CLClientManagerAuthorizationContext authorizationContextByANDingServiceMaskTuple:];
-[CLClientManagerAuthorizationContext authorizedForWidgetUpdates];
-[CLClientManagerAuthorizationContext diagnosticMask];
-[CLClientManagerAuthorizationContext effectiveServiceMask];
-[CLClientManagerAuthorizationContext inUseLevel];
-[CLClientManagerAuthorizationContext inUseLevelIsAtLeast:];
-[CLClientManagerAuthorizationContext initWithInUseLevel:registrationResult:transientAwareRegistrationResult:serviceMaskTuple:diagnosticMask:authorizedForWidgetUpdates:];
-[CLClientManagerAuthorizationContext isAuthorizedForServiceType:];
-[CLClientManagerAuthorizationContext isNonProvisionallyAuthorizedForServiceType:];
-[CLClientManagerAuthorizationContext isNonProvisionallyAuthorizedForServiceTypeMask:];
-[CLClientManagerAuthorizationContext provisionalServiceMask];
-[CLClientManagerAuthorizationContext staticServiceMask];
-[CLClientManagerAuthorizationContext transientAwareRegistrationResult];
```
