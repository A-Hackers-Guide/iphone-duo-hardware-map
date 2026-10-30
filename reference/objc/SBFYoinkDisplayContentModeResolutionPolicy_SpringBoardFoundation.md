# `SBFYoinkDisplayContentModeResolutionPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFDisplayContentModeResolutionPolicy`
- 4 instance variables, 3 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _persistentYoinkAssertions;
@"NSMutableSet" _transientYoinkAssertions;
q _preferredSurfaceType;
@? _activationAssertionStateDidChangeHandler;
```

## Properties

```
@property (Tq,R,N,V_preferredSurfaceType) preferredSurfaceType;
@property (T@?,C,N,V_activationAssertionStateDidChangeHandler) activationAssertionStateDidChangeHandler;
@property (T@"NSString",R,C,N) assertionSummary;
```

## Instance methods

```
-[SBFYoinkDisplayContentModeResolutionPolicy init];
-[SBFYoinkDisplayContentModeResolutionPolicy dealloc];
-[SBFYoinkDisplayContentModeResolutionPolicy isUserInitiated];
-[SBFYoinkDisplayContentModeResolutionPolicy name];
-[SBFYoinkDisplayContentModeResolutionPolicy _invalidateAssertions:forEvent:];
-[SBFYoinkDisplayContentModeResolutionPolicy _isHoldingAnyAssertion];
-[SBFYoinkDisplayContentModeResolutionPolicy _notifyActivationAssertionStateDidChange];
-[SBFYoinkDisplayContentModeResolutionPolicy acquireActivationAssertionForSurfaceType:reason:persistent:invalidationHandler:];
-[SBFYoinkDisplayContentModeResolutionPolicy activationAssertionStateDidChangeHandler];
-[SBFYoinkDisplayContentModeResolutionPolicy assertionSummary];
-[SBFYoinkDisplayContentModeResolutionPolicy notePolicyDidActivate];
-[SBFYoinkDisplayContentModeResolutionPolicy notePolicyDidDeactivate];
-[SBFYoinkDisplayContentModeResolutionPolicy noteResolvedPrevailingPolicy:];
-[SBFYoinkDisplayContentModeResolutionPolicy preferredPrimarySurfaceTypeForDevicePose:];
-[SBFYoinkDisplayContentModeResolutionPolicy preferredSurfaceType];
-[SBFYoinkDisplayContentModeResolutionPolicy resolvedModeForDisplayProxy:devicePose:];
-[SBFYoinkDisplayContentModeResolutionPolicy setActivationAssertionStateDidChangeHandler:];
-[SBFYoinkDisplayContentModeResolutionPolicy shouldBeActiveForDevicePose:prevailingPolicy:candidatePolicy:];
-[SBFYoinkDisplayContentModeResolutionPolicy targetModeForDisplayProxy:devicePose:];
```
