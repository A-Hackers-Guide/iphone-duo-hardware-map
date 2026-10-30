# `SBSAContextMutator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 44 properties, 89 instance methods, 0 class methods

## Instance variables

```
@"SBSAContext" _context;
```

## Properties

```
@property (T@"SBSAPreferences",C,N) preferences;
@property (TQ,N) signals;
@property (TQ,N) flags;
@property (T@"SBSAContext",R,N,V_context) context;
@property (Td,N) displayScale;
@property (T@"NSArray",C,N) requests;
@property (T@"NSArray",C,N) gestureDescriptions;
@property (T@"NSArray",C,N) animatedTransitionResults;
@property (T@"NSArray",C,N) elapsedTimerDescriptions;
@property (TQ,N) minimumNumberOfContainers;
@property (TQ,N) maximumNumberOfElements;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) inertContainerFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) defaultFixedIndicatorFrameInWindowSpace;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) systemContainerBounds;
@property (T@"SBSAPlatformMetricsContext",N) platformMetrics;
@property (Tq,N) layoutDirection;
@property (Tq,N) traitInterfaceOrientation;
@property (Tq,N) statusBarAxis;
@property (Tq,N) overrideRenderingStyle;
@property (Tq,N) cloningStyle;
@property (TQ,N) activeDisplay;
@property (Tq,N) backlightLuminanceLevel;
@property (TB,N,GisHeavyShadowRequiredForTransition) heavyShadowRequiredForTransition;
@property (TB,N,GisKeyLineRequiredForTransition) keyLineRequiredForTransition;
@property (Tq,N) requestedIndicatorElevationStyle;
@property (TB,N,GisAccessibilityZoomActiveAndEnabled) accessibilityZoomActiveAndEnabled;
@property (TB,N,GisReduceTransparencyEnabled) reduceTransparencyEnabled;
@property (TB,N,GisAnimatedTransitionInProgress) animatedTransitionInProgress;
@property (TB,N,GisReachabilityActiveOrAnimating) reachabilityActiveOrAnimating;
@property (T@"SBSAIndicatorElementContext",C,N) indicatorElementContext;
@property (T@"SBSAMaintainedPreferences",C,N) maintainedPreferences;
@property (T@"SBSAViewDescription",C,N) containerParentViewDescription;
@property (T@"NSUUID",C,N) statusBarAvoidanceInterfaceElementIdentifier;
@property (T@"NSUUID",C,N) fixedSensorMatchMoveSourceViewInterfaceElementIdentifier;
@property (T@"NSArray",C,N) elementContexts;
@property (T@"NSArray",C,N) blankingRegionElementContexts;
@property (T@"NSArray",C,N) elementInteractionResults;
@property (T@"NSArray",C,N) elementSnapshotContexts;
@property (T@"SBSADefaultsContext",C,N) defaultsContext;
@property (T@"SBSAContainerViewDescription",C,N) indicatorContainerViewDescription;
@property (T@"NSArray",C,N) blankingRegionContainerViewDescriptions;
@property (T@"NSArray",C,N) effectPackageViewDescriptions;
@property (T@"NSArray",C,N) containerViewDescriptions;
@property (T@"SBSAExcursionViewDescription",C,N) acceptanceBounceExcursionViewDescription;
```

## Instance methods

```
-[SBSAContextMutator isAnimatedTransitionInProgress];
-[SBSAContextMutator initWithContext:];
-[SBSAContextMutator blankingRegionElementContexts];
-[SBSAContextMutator setContainerParentViewDescription:];
-[SBSAContextMutator setInertContainerFrame:];
-[SBSAContextMutator effectPackageViewDescriptions];
-[SBSAContextMutator isReduceTransparencyEnabled];
-[SBSAContextMutator setStatusBarAxis:];
-[SBSAContextMutator setRequestedIndicatorElevationStyle:];
-[SBSAContextMutator overrideRenderingStyle];
-[SBSAContextMutator setAnimatedTransitionResults:];
-[SBSAContextMutator setFlags:];
-[SBSAContextMutator flags];
-[SBSAContextMutator cloningStyle];
-[SBSAContextMutator setElementContexts:];
-[SBSAContextMutator setPreferences:];
-[SBSAContextMutator setDisplayScale:];
-[SBSAContextMutator isAccessibilityZoomActiveAndEnabled];
-[SBSAContextMutator containerViewDescriptions];
-[SBSAContextMutator requests];
-[SBSAContextMutator backlightLuminanceLevel];
-[SBSAContextMutator displayScale];
-[SBSAContextMutator setPlatformMetrics:];
-[SBSAContextMutator defaultsContext];
-[SBSAContextMutator setLayoutDirection:];
-[SBSAContextMutator setSignals:];
-[SBSAContextMutator preferences];
-[SBSAContextMutator setRequests:];
-[SBSAContextMutator setBacklightLuminanceLevel:];
-[SBSAContextMutator setAccessibilityZoomActiveAndEnabled:];
-[SBSAContextMutator setTraitInterfaceOrientation:];
-[SBSAContextMutator layoutDirection];
-[SBSAContextMutator maintainedPreferences];
-[SBSAContextMutator activeDisplay];
-[SBSAContextMutator setIndicatorContainerViewDescription:];
-[SBSAContextMutator elementSnapshotContexts];
-[SBSAContextMutator defaultFixedIndicatorFrameInWindowSpace];
-[SBSAContextMutator setElapsedTimerDescriptions:];
-[SBSAContextMutator setGestureDescriptions:];
-[SBSAContextMutator gestureDescriptions];
-[SBSAContextMutator setContainerViewDescriptions:];
-[SBSAContextMutator requestedIndicatorElevationStyle];
-[SBSAContextMutator traitInterfaceOrientation];
-[SBSAContextMutator maximumNumberOfElements];
-[SBSAContextMutator setReachabilityActiveOrAnimating:];
-[SBSAContextMutator setStatusBarAvoidanceInterfaceElementIdentifier:];
-[SBSAContextMutator setElementSnapshotContexts:];
-[SBSAContextMutator setFixedSensorMatchMoveSourceViewInterfaceElementIdentifier:];
-[SBSAContextMutator statusBarAvoidanceInterfaceElementIdentifier];
-[SBSAContextMutator elementContexts];
-[SBSAContextMutator setElementInteractionResults:];
-[SBSAContextMutator indicatorElementContext];
-[SBSAContextMutator setMinimumNumberOfContainers:];
-[SBSAContextMutator setActiveDisplay:];
-[SBSAContextMutator setDefaultsContext:];
-[SBSAContextMutator containerParentViewDescription];
-[SBSAContextMutator setDefaultFixedIndicatorFrameInWindowSpace:];
-[SBSAContextMutator description];
-[SBSAContextMutator setReduceTransparencyEnabled:];
-[SBSAContextMutator setMaintainedPreferences:];
-[SBSAContextMutator setKeyLineRequiredForTransition:];
-[SBSAContextMutator signals];
-[SBSAContextMutator setBlankingRegionContainerViewDescriptions:];
-[SBSAContextMutator systemContainerBounds];
-[SBSAContextMutator blankingRegionContainerViewDescriptions];
-[SBSAContextMutator fixedSensorMatchMoveSourceViewInterfaceElementIdentifier];
-[SBSAContextMutator setMaximumNumberOfElements:];
-[SBSAContextMutator isReachabilityActiveOrAnimating];
-[SBSAContextMutator elementInteractionResults];
-[SBSAContextMutator setSystemContainerBounds:];
-[SBSAContextMutator animatedTransitionResults];
-[SBSAContextMutator statusBarAxis];
-[SBSAContextMutator setHeavyShadowRequiredForTransition:];
-[SBSAContextMutator context];
-[SBSAContextMutator setEffectPackageViewDescriptions:];
-[SBSAContextMutator setAnimatedTransitionInProgress:];
-[SBSAContextMutator setAcceptanceBounceExcursionViewDescription:];
-[SBSAContextMutator isHeavyShadowRequiredForTransition];
-[SBSAContextMutator platformMetrics];
-[SBSAContextMutator isKeyLineRequiredForTransition];
-[SBSAContextMutator inertContainerFrame];
-[SBSAContextMutator elapsedTimerDescriptions];
-[SBSAContextMutator setBlankingRegionElementContexts:];
-[SBSAContextMutator setIndicatorElementContext:];
-[SBSAContextMutator setCloningStyle:];
-[SBSAContextMutator acceptanceBounceExcursionViewDescription];
-[SBSAContextMutator indicatorContainerViewDescription];
-[SBSAContextMutator setOverrideRenderingStyle:];
-[SBSAContextMutator minimumNumberOfContainers];
```
