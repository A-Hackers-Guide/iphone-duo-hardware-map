# `SBSAContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `SBSAContextRepresenting`, `NSCopying`, `SBSADictionaryDescribable`, `SBSABlockMutating`
- 44 instance variables, 52 properties, 103 instance methods, 4 class methods

## Instance variables

```
B _heavyShadowRequiredForTransition;
B _keyLineRequiredForTransition;
B _accessibilityZoomActiveAndEnabled;
B _reduceTransparencyEnabled;
B _animatedTransitionInProgress;
B _reachabilityActiveOrAnimating;
Q _queryIteration;
Q _minimumNumberOfContainers;
Q _maximumNumberOfElements;
@"SBSAPlatformMetricsContext" _platformMetrics;
q _layoutDirection;
q _traitInterfaceOrientation;
q _statusBarAxis;
q _overrideRenderingStyle;
q _cloningStyle;
Q _activeDisplay;
q _backlightLuminanceLevel;
q _requestedIndicatorElevationStyle;
@"SBSAIndicatorElementContext" _indicatorElementContext;
@"SBSAMaintainedPreferences" _maintainedPreferences;
@"SBSAViewDescription" _containerParentViewDescription;
@"NSUUID" _statusBarAvoidanceInterfaceElementIdentifier;
@"NSUUID" _fixedSensorMatchMoveSourceViewInterfaceElementIdentifier;
@"NSArray" _elementContexts;
@"NSArray" _blankingRegionElementContexts;
@"NSArray" _elementInteractionResults;
@"NSArray" _elementSnapshotContexts;
@"SBSADefaultsContext" _defaultsContext;
@"SBSAContainerViewDescription" _indicatorContainerViewDescription;
@"NSArray" _blankingRegionContainerViewDescriptions;
@"NSArray" _effectPackageViewDescriptions;
@"NSArray" _containerViewDescriptions;
@"SBSAExcursionViewDescription" _acceptanceBounceExcursionViewDescription;
d _displayScale;
@"NSArray" _requests;
@"NSArray" _gestureDescriptions;
@"NSArray" _animatedTransitionResults;
@"NSArray" _elapsedTimerDescriptions;
@"SBSAPreferences" _preferences;
Q _signals;
Q _flags;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inertContainerFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _defaultFixedIndicatorFrameInWindowSpace;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _systemContainerBounds;
```

## Properties

```
@property (T@"SBSAPreferences",R,C,N) preferences;
@property (TQ,R,N) signals;
@property (TQ,R,N) flags;
@property (Td,N,S_setDisplayScale:,V_displayScale) displayScale;
@property (TQ,N,S_setMinimumNumberOfContainers:,V_minimumNumberOfContainers) minimumNumberOfContainers;
@property (TQ,N,S_setMaximumNumberOfElements:,V_maximumNumberOfElements) maximumNumberOfElements;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setInertContainerFrame:,V_inertContainerFrame) inertContainerFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setDefaultFixedIndicatorFrameInWindowSpace:,V_defaultFixedIndicatorFrameInWindowSpace) defaultFixedIndicatorFrameInWindowSpace;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setSystemContainerBounds:,V_systemContainerBounds) systemContainerBounds;
@property (T@"SBSAPlatformMetricsContext",C,N,S_setPlatformMetrics:,V_platformMetrics) platformMetrics;
@property (Tq,N,S_setLayoutDirection:,V_layoutDirection) layoutDirection;
@property (Tq,N,S_setTraitInterfaceOrientation:,V_traitInterfaceOrientation) traitInterfaceOrientation;
@property (Tq,N,S_setStatusBarAxis:,V_statusBarAxis) statusBarAxis;
@property (Tq,N,S_setOverrideRenderingStyle:,V_overrideRenderingStyle) overrideRenderingStyle;
@property (Tq,N,S_setCloningStyle:,V_cloningStyle) cloningStyle;
@property (TQ,N,S_setActiveDisplay:,V_activeDisplay) activeDisplay;
@property (Tq,N,S_setBacklightLuminanceLevel:,V_backlightLuminanceLevel) backlightLuminanceLevel;
@property (TB,N,GisHeavyShadowRequiredForTransition,S_setHeavyShadowRequiredForTransition:,V_heavyShadowRequiredForTransition) heavyShadowRequiredForTransition;
@property (TB,N,GisKeyLineRequiredForTransition,S_setKeyLineRequiredForTransition:,V_keyLineRequiredForTransition) keyLineRequiredForTransition;
@property (Tq,N,S_setRequestedIndicatorElevationStyle:,V_requestedIndicatorElevationStyle) requestedIndicatorElevationStyle;
@property (TB,N,GisAccessibilityZoomActiveAndEnabled,S_setAccessibilityZoomActiveAndEnabled:,V_accessibilityZoomActiveAndEnabled) accessibilityZoomActiveAndEnabled;
@property (TB,N,GisReduceTransparencyEnabled,S_setReduceTransparencyEnabled:,V_reduceTransparencyEnabled) reduceTransparencyEnabled;
@property (TB,N,GisAnimatedTransitionInProgress,S_setAnimatedTransitionInProgress:,V_animatedTransitionInProgress) animatedTransitionInProgress;
@property (TB,N,GisReachabilityActiveOrAnimating,S_setReachabilityActiveOrAnimating:,V_reachabilityActiveOrAnimating) reachabilityActiveOrAnimating;
@property (T@"SBSAIndicatorElementContext",C,N,S_setIndicatorElementContext:,V_indicatorElementContext) indicatorElementContext;
@property (T@"SBSAMaintainedPreferences",C,N,S_setMaintainedPreferences:,V_maintainedPreferences) maintainedPreferences;
@property (T@"SBSAViewDescription",C,N,S_setContainerParentViewDescription:,V_containerParentViewDescription) containerParentViewDescription;
@property (T@"NSUUID",C,N,S_setStatusBarAvoidanceInterfaceElementIdentifier:,V_statusBarAvoidanceInterfaceElementIdentifier) statusBarAvoidanceInterfaceElementIdentifier;
@property (T@"NSUUID",C,N,S_setFixedSensorMatchMoveSourceViewInterfaceElementIdentifier:,V_fixedSensorMatchMoveSourceViewInterfaceElementIdentifier) fixedSensorMatchMoveSourceViewInterfaceElementIdentifier;
@property (T@"NSArray",C,N,S_setRequests:,V_requests) requests;
@property (T@"NSArray",C,N,S_setElementContexts:,V_elementContexts) elementContexts;
@property (T@"NSArray",C,N,S_setBlankingRegionElementContexts:,V_blankingRegionElementContexts) blankingRegionElementContexts;
@property (T@"NSArray",C,N,S_setElementInteractionResults:,V_elementInteractionResults) elementInteractionResults;
@property (T@"NSArray",C,N,S_setElementSnapshotContexts:,V_elementSnapshotContexts) elementSnapshotContexts;
@property (T@"SBSADefaultsContext",C,N,S_setDefaultsContext:,V_defaultsContext) defaultsContext;
@property (T@"NSArray",C,N,S_setGestureDescriptions:,V_gestureDescriptions) gestureDescriptions;
@property (T@"NSArray",C,N,S_setAnimatedTransitionResults:,V_animatedTransitionResults) animatedTransitionResults;
@property (T@"NSArray",C,N,S_setElapsedTimerDescriptions:,V_elapsedTimerDescriptions) elapsedTimerDescriptions;
@property (T@"SBSAContainerViewDescription",C,N,S_setIndicatorContainerViewDescription:,V_indicatorContainerViewDescription) indicatorContainerViewDescription;
@property (T@"NSArray",C,N,S_setBlankingRegionContainerViewDescriptions:,V_blankingRegionContainerViewDescriptions) blankingRegionContainerViewDescriptions;
@property (T@"NSArray",C,N,S_setEffectPackageViewDescriptions:,V_effectPackageViewDescriptions) effectPackageViewDescriptions;
@property (T@"NSArray",C,N,S_setContainerViewDescriptions:,V_containerViewDescriptions) containerViewDescriptions;
@property (T@"SBSAExcursionViewDescription",C,N,S_setAcceptanceBounceExcursionViewDescription:,V_acceptanceBounceExcursionViewDescription) acceptanceBounceExcursionViewDescription;
@property (T@"SBSAPreferences",C,N,S_setPreferences:,V_preferences) preferences;
@property (TQ,N,S_setSignals:,V_signals) signals;
@property (TQ,N,S_setFlags:,V_flags) flags;
@property (TQ,R,N,V_queryIteration) queryIteration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"BSOrderedDictionary",R,C,N) dictionaryDescription;
```

## Class methods

```
+[SBSAContext initialize];
+[SBSAContext instanceWithBlock:];
+[SBSAContext instanceWithQueryIteration:block:];
+[SBSAContext mutatorClass];
```

## Instance methods

```
-[SBSAContext isAnimatedTransitionInProgress];
-[SBSAContext blankingRegionElementContexts];
-[SBSAContext effectPackageViewDescriptions];
-[SBSAContext isReduceTransparencyEnabled];
-[SBSAContext overrideRenderingStyle];
-[SBSAContext flags];
-[SBSAContext cloningStyle];
-[SBSAContext _setFlags:];
-[SBSAContext isAccessibilityZoomActiveAndEnabled];
-[SBSAContext containerViewDescriptions];
-[SBSAContext requests];
-[SBSAContext backlightLuminanceLevel];
-[SBSAContext displayScale];
-[SBSAContext defaultsContext];
-[SBSAContext preferences];
-[SBSAContext layoutDirection];
-[SBSAContext maintainedPreferences];
-[SBSAContext activeDisplay];
-[SBSAContext elementSnapshotContexts];
-[SBSAContext defaultFixedIndicatorFrameInWindowSpace];
-[SBSAContext gestureDescriptions];
-[SBSAContext requestedIndicatorElevationStyle];
-[SBSAContext traitInterfaceOrientation];
-[SBSAContext maximumNumberOfElements];
-[SBSAContext dictionaryDescription];
-[SBSAContext statusBarAvoidanceInterfaceElementIdentifier];
-[SBSAContext elementContexts];
-[SBSAContext indicatorElementContext];
-[SBSAContext encodeWithCoder:];
-[SBSAContext hash];
-[SBSAContext containerParentViewDescription];
-[SBSAContext description];
-[SBSAContext signals];
-[SBSAContext systemContainerBounds];
-[SBSAContext blankingRegionContainerViewDescriptions];
-[SBSAContext fixedSensorMatchMoveSourceViewInterfaceElementIdentifier];
-[SBSAContext isReachabilityActiveOrAnimating];
-[SBSAContext copyWithZone:];
-[SBSAContext elementInteractionResults];
-[SBSAContext animatedTransitionResults];
-[SBSAContext statusBarAxis];
-[SBSAContext isEqual:];
-[SBSAContext isHeavyShadowRequiredForTransition];
-[SBSAContext platformMetrics];
-[SBSAContext isKeyLineRequiredForTransition];
-[SBSAContext inertContainerFrame];
-[SBSAContext elapsedTimerDescriptions];
-[SBSAContext acceptanceBounceExcursionViewDescription];
-[SBSAContext copyWithBlock:];
-[SBSAContext indicatorContainerViewDescription];
-[SBSAContext minimumNumberOfContainers];
-[SBSAContext _initWithContext:];
-[SBSAContext membersForCoder];
-[SBSAContext _setDisplayScale:];
-[SBSAContext _setLayoutDirection:];
-[SBSAContext _setAcceptanceBounceExcursionViewDescription:];
-[SBSAContext _setAccessibilityZoomActiveAndEnabled:];
-[SBSAContext _setActiveDisplay:];
-[SBSAContext _setAnimatedTransitionInProgress:];
-[SBSAContext _setAnimatedTransitionResults:];
-[SBSAContext _setBacklightLuminanceLevel:];
-[SBSAContext _setBlankingRegionContainerViewDescriptions:];
-[SBSAContext _setBlankingRegionElementContexts:];
-[SBSAContext _setCloningStyle:];
-[SBSAContext _setContainerParentViewDescription:];
-[SBSAContext _setContainerViewDescriptions:];
-[SBSAContext _setDefaultFixedIndicatorFrameInWindowSpace:];
-[SBSAContext _setDefaultsContext:];
-[SBSAContext _setEffectPackageViewDescriptions:];
-[SBSAContext _setElapsedTimerDescriptions:];
-[SBSAContext _setElementContexts:];
-[SBSAContext _setElementInteractionResults:];
-[SBSAContext _setElementSnapshotContexts:];
-[SBSAContext _setFixedSensorMatchMoveSourceViewInterfaceElementIdentifier:];
-[SBSAContext _setGestureDescriptions:];
-[SBSAContext _setHeavyShadowRequiredForTransition:];
-[SBSAContext _setIndicatorContainerViewDescription:];
-[SBSAContext _setIndicatorElementContext:];
-[SBSAContext _setInertContainerFrame:];
-[SBSAContext _setKeyLineRequiredForTransition:];
-[SBSAContext _setMaintainedPreferences:];
-[SBSAContext _setMaximumNumberOfElements:];
-[SBSAContext _setMinimumNumberOfContainers:];
-[SBSAContext _setOverrideRenderingStyle:];
-[SBSAContext _setPlatformMetrics:];
-[SBSAContext _setPreferences:];
-[SBSAContext _setReachabilityActiveOrAnimating:];
-[SBSAContext _setReduceTransparencyEnabled:];
-[SBSAContext _setRequestedIndicatorElevationStyle:];
-[SBSAContext _setRequests:];
-[SBSAContext _setSignals:];
-[SBSAContext _setStatusBarAvoidanceInterfaceElementIdentifier:];
-[SBSAContext _setStatusBarAxis:];
-[SBSAContext _setSystemContainerBounds:];
-[SBSAContext _setTraitInterfaceOrientation:];
-[SBSAContext allContainerViewDescriptions];
-[SBSAContext containerHasLaidOutOnce:];
-[SBSAContext containsAnyOfSignals:];
-[SBSAContext copyByAddingFlags:debugRequestingProvider:];
-[SBSAContext copyByAddingSignals:debugRequestingProvider:];
-[SBSAContext copyByUpdatingPreferences:];
-[SBSAContext initWithQueryIteration:];
-[SBSAContext queryIteration];
```
