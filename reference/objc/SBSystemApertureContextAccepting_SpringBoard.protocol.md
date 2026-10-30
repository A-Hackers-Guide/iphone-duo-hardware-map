# `SBSystemApertureContextAccepting` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 8 instance methods, 0 class methods

## Properties

```
@property (TB,?,N,GisAffiliatedWithSessionMonitor) affiliatedWithSessionMonitor;
@property (TB,?,R,N,GisAlerting) alerting;
@property (TB,?,N) elementProviderPrefersSuppression;
@property (TQ,?,N) obstructionEdge;
```

## Instance methods

```
-[SBSystemApertureContextAccepting isAlerting];
-[SBSystemApertureContextAccepting obstructionEdge];
-[SBSystemApertureContextAccepting setObstructionEdge:];
-[SBSystemApertureContextAccepting setAffiliatedWithSessionMonitor:];
-[SBSystemApertureContextAccepting setElementProviderPrefersSuppression:];
-[SBSystemApertureContextAccepting isAffiliatedWithSessionMonitor];
-[SBSystemApertureContextAccepting requestAlertingAssertionImplicitlyDismissable:];
-[SBSystemApertureContextAccepting elementProviderPrefersSuppression];
```
