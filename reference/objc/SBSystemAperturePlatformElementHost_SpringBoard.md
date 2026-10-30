# `SBSystemAperturePlatformElementHost`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemAperturePlatformElementHosting`
- 6 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _reasonsToUrgencyAssertions;
@"NSMapTable" _reasonsToRequiredPriorityAssertions;
@"<SBSystemApertureElement>" _element;
@"<SBSystemApertureDynamicsHandling><SBSystemAperturePlatformElementHostingDelegate>" _delegate;
@"<SAInvalidatable>" _urgentAndImportantAssertion;
@"<SAInvalidatable>" _requiredPriorityAssertion;
```

## Properties

```
@property (T@"<SAInvalidatable>",R,W,N,V_urgentAndImportantAssertion) urgentAndImportantAssertion;
@property (T@"<SAInvalidatable>",R,W,N,V_requiredPriorityAssertion) requiredPriorityAssertion;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemAperturePlatformElementHost destinationToken];
-[SBSystemAperturePlatformElementHost invalidateAllAssertions];
-[SBSystemAperturePlatformElementHost _requiredPriorityAssertionWithReason:creatingIfNecessary:];
-[SBSystemAperturePlatformElementHost _urgencyAssertionWithReason:creatingIfNecessary:];
-[SBSystemAperturePlatformElementHost activeRequiredPriorityReasons];
-[SBSystemAperturePlatformElementHost activeUrgencyReasons];
-[SBSystemAperturePlatformElementHost elementRequestsDiscreteAnimationOfType:];
-[SBSystemAperturePlatformElementHost elementRequestsPersistentAnimationOfType:];
-[SBSystemAperturePlatformElementHost initWithElement:delegate:];
-[SBSystemAperturePlatformElementHost performAction:withCompletionUponIndicatorSettling:];
-[SBSystemAperturePlatformElementHost requestRequiredPriorityAssertionWithReason:];
-[SBSystemAperturePlatformElementHost requestUrgentAndImportantPriorityWithReason:];
-[SBSystemAperturePlatformElementHost requiredPriorityAssertion];
-[SBSystemAperturePlatformElementHost sbWindowScene];
-[SBSystemAperturePlatformElementHost urgentAndImportantAssertion];
```
