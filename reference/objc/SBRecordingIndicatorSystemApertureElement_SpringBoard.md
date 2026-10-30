# `SBRecordingIndicatorSystemApertureElement`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SAIndicatorBehavior`, `SAUIIndicatorElementViewProviding`, `SBSystemApertureSuppressible`, `SBSystemApertureElementVisibilityObserving`, `SBSystemApertureElement`, `SBSystemApertureLayoutCustomizing`, `SBSystemApertureContainerViewGeometryObserver`, `SBSystemApertureHighLevelContainerRenderingObserving`, `SAUIIndicatorElementViewPreferencesObserving`, `PTSettingsKeyObserver`, `SBSystemApertureContextAccepting`, `SAUILayoutDirectionObserving`, `SAElement`, `SBSystemApertureContextProviding`, `SAUIIndicatorLayoutSpecifying`
- 27 instance variables, 43 properties, 80 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _windowScene;
@"<BSInvalidatable>" _blankingAssertion;
B _assistantIslandActive;
@"SBRecordingIndicatorRotationRateLimiter" _rotationRateLimiter;
Q _activeLayoutDirection;
B _hasActiveLayoutDirection;
B _rotationChangesShouldBeUnanimated;
B _rotationRateLimitForcesEjection;
Q _toleratedRotationCount;
B _indicatorAwaitsSteady;
B _suppressed;
B _minimumOnTimeSatisfied;
B _interSensorDwellTimerSatisfied;
@"NSString" _associatedBlankingRegionIdentifier;
@"<SBSystemAperturePlatformElementHosting>" _platformElementHost;
@"<SAUIIndicatorLayoutHosting>" _layoutHost;
@"NSString" _elementIdentifier;
@"<SBRecordingIndicatorSystemApertureElementDelegate>" _delegate;
@"SBDisplayRegionBlankingManager" _displayRegionBlankingManager;
@"SBRecordingIndicatorManager" _recordingIndicatorManager;
@"SBRecordingIndicatorVisualRepresentation" _interSensorRegionIndicator;
@"SBRecordingIndicatorVisualRepresentation" _microRegionIndicator;
@"BSContinuousMachTimer" _interSensorDwellTimer;
@"SBSystemApertureLayoutMetrics" _layoutMetrics;
@"BSContinuousMachTimer" _steadyTimer;
@"SBSecureIndicatorMinimumOnTimeCoordinator" _minimumOnTimeCoordinator;
@"<SBSecureIndicatorMinimumOnTimeCoordinatedBlockRegistration>" _minimumOnTimeAssertion;
```

## Properties

```
@property (T@"SBRecordingIndicatorManager",W,N,V_recordingIndicatorManager) recordingIndicatorManager;
@property (T@"SBRecordingIndicatorVisualRepresentation",&,N,V_interSensorRegionIndicator) interSensorRegionIndicator;
@property (T@"SBRecordingIndicatorVisualRepresentation",&,N,V_microRegionIndicator) microRegionIndicator;
@property (TB,N,V_minimumOnTimeSatisfied) minimumOnTimeSatisfied;
@property (TB,N,V_interSensorDwellTimerSatisfied) interSensorDwellTimerSatisfied;
@property (T@"BSContinuousMachTimer",&,N,V_interSensorDwellTimer) interSensorDwellTimer;
@property (T@"SBSystemApertureLayoutMetrics",&,N,V_layoutMetrics) layoutMetrics;
@property (TB,N,V_indicatorAwaitsSteady) indicatorAwaitsSteady;
@property (T@"BSContinuousMachTimer",&,N,V_steadyTimer) steadyTimer;
@property (T@"SBSecureIndicatorMinimumOnTimeCoordinator",&,N,V_minimumOnTimeCoordinator) minimumOnTimeCoordinator;
@property (T@"<SBSecureIndicatorMinimumOnTimeCoordinatedBlockRegistration>",&,N,V_minimumOnTimeAssertion) minimumOnTimeAssertion;
@property (T@"NSString",C,N,V_associatedBlankingRegionIdentifier) associatedBlankingRegionIdentifier;
@property (T@"<SBRecordingIndicatorSystemApertureElementDelegate>",W,N,V_delegate) delegate;
@property (T@"SBDisplayRegionBlankingManager",W,N,V_displayRegionBlankingManager) displayRegionBlankingManager;
@property (TB,N,GisAssistantIslandActive,V_assistantIslandActive) assistantIslandActive;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,N) indicatorView;
@property (T@"UIView",?,R,N) fixedIndicatorView;
@property (T@"<SAElement>",R,W,N) element;
@property (TB,?,N,GisSuppressed,V_suppressed) suppressed;
@property (T@"<SBSystemAperturePlatformElementHosting>",?,W,N,V_platformElementHost) platformElementHost;
@property (T@"<SAElementHosting>",?,W,N) elementHost;
@property (T@"NSString",R,C,N) clientIdentifier;
@property (T@"NSString",R,C,N,V_elementIdentifier) elementIdentifier;
@property (Tq,?,R,N) systemApertureCustomLayout;
@property (Tq,?,R,N) customLayoutRequestingSpecialFlowerBoundsResizingAnimation;
@property (Tq,?,R,N) systemApertureLayoutCustomizingOptions;
@property (TB,?,N,GisAffiliatedWithSessionMonitor) affiliatedWithSessionMonitor;
@property (TB,?,R,N,GisAlerting) alerting;
@property (TB,?,N) elementProviderPrefersSuppression;
@property (TQ,?,N) obstructionEdge;
@property (TQ,?,N) layoutDirection;
@property (T@"UIColor",?,R,N) keyColor;
@property (T@"FBScene",?,R,N) scene;
@property (TB,?,R,N) preventsSwipeToHide;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) preferredAvoidanceRect;
@property (Td,?,R,N) preferredAvoidanceCornerRadius;
@property (TB,?,R,N) inhibitsIndicatorMitosis;
@property (Td,?,R,N) preferredSystemClipPadding;
@property (T@"<SAUIIndicatorLayoutHosting>",?,W,N,V_layoutHost) layoutHost;
```

## Instance methods

```
-[SBRecordingIndicatorSystemApertureElement minimumOnTimeCoordinator];
-[SBRecordingIndicatorSystemApertureElement recordingIndicatorManager];
-[SBRecordingIndicatorSystemApertureElement layoutHost];
-[SBRecordingIndicatorSystemApertureElement setRecordingIndicatorManager:];
-[SBRecordingIndicatorSystemApertureElement isSuppressed];
-[SBRecordingIndicatorSystemApertureElement preferredIndicatorEdgeOutsets];
-[SBRecordingIndicatorSystemApertureElement systemApertureContainerView:didChangeResolutionTransitionStrength:];
-[SBRecordingIndicatorSystemApertureElement setLayoutHost:];
-[SBRecordingIndicatorSystemApertureElement isFixedInOrientation];
-[SBRecordingIndicatorSystemApertureElement sizeThatFitsSize:forProvidedView:];
-[SBRecordingIndicatorSystemApertureElement _positionMicroRegionIndicatorFromContainerView:containerPoint:];
-[SBRecordingIndicatorSystemApertureElement indicatorNeedsDisplayWellKnownLocation];
-[SBRecordingIndicatorSystemApertureElement steadyTimer];
-[SBRecordingIndicatorSystemApertureElement _indicatorContentSide];
-[SBRecordingIndicatorSystemApertureElement _cancelDwellTimer];
-[SBRecordingIndicatorSystemApertureElement clientIdentifier];
-[SBRecordingIndicatorSystemApertureElement indicatorRotationChangesShouldBeUnanimated];
-[SBRecordingIndicatorSystemApertureElement setInterSensorDwellTimer:];
-[SBRecordingIndicatorSystemApertureElement element];
-[SBRecordingIndicatorSystemApertureElement elementIdentifier];
-[SBRecordingIndicatorSystemApertureElement didUpdateIndicatorViewTransform:];
-[SBRecordingIndicatorSystemApertureElement fixedIndicatorView];
-[SBRecordingIndicatorSystemApertureElement setSteadyTimer:];
-[SBRecordingIndicatorSystemApertureElement viewProvider];
-[SBRecordingIndicatorSystemApertureElement interSensorDwellTimer];
-[SBRecordingIndicatorSystemApertureElement setLayoutDirection:];
-[SBRecordingIndicatorSystemApertureElement dealloc];
-[SBRecordingIndicatorSystemApertureElement isAssistantIslandActive];
-[SBRecordingIndicatorSystemApertureElement didUpdateIndicatorViewBlurProgress:];
-[SBRecordingIndicatorSystemApertureElement setSuppressed:];
-[SBRecordingIndicatorSystemApertureElement highLevelContainerRenderingConfigurationDidChange:];
-[SBRecordingIndicatorSystemApertureElement microRegionIndicator];
-[SBRecordingIndicatorSystemApertureElement didUpdateIndicatorViewAlpha:];
-[SBRecordingIndicatorSystemApertureElement setMinimumOnTimeAssertion:];
-[SBRecordingIndicatorSystemApertureElement settings:changedValueForKey:];
-[SBRecordingIndicatorSystemApertureElement didUpdateFixedIndicatorViewTransform:];
-[SBRecordingIndicatorSystemApertureElement setMicroRegionIndicator:];
-[SBRecordingIndicatorSystemApertureElement _ensureBlankingRegionAssertionsForRegionIdentifier:];
-[SBRecordingIndicatorSystemApertureElement setPlatformElementHost:];
-[SBRecordingIndicatorSystemApertureElement layoutMetrics];
-[SBRecordingIndicatorSystemApertureElement setLayoutMetrics:];
-[SBRecordingIndicatorSystemApertureElement indicatorAwaitsSteady];
-[SBRecordingIndicatorSystemApertureElement systemApertureContainerView:didChangeCenter:];
-[SBRecordingIndicatorSystemApertureElement setDelegate:];
-[SBRecordingIndicatorSystemApertureElement didUpdateFixedIndicatorViewAlpha:];
-[SBRecordingIndicatorSystemApertureElement resetInternalState];
-[SBRecordingIndicatorSystemApertureElement minimumOnTimeSatisfied];
-[SBRecordingIndicatorSystemApertureElement minimumOnTimeAssertion];
-[SBRecordingIndicatorSystemApertureElement didUpdateFixedIndicatorViewBlurProgress:];
-[SBRecordingIndicatorSystemApertureElement setMinimumOnTimeSatisfied:];
-[SBRecordingIndicatorSystemApertureElement element:visibilityWillChange:];
-[SBRecordingIndicatorSystemApertureElement delegate];
-[SBRecordingIndicatorSystemApertureElement pulse];
-[SBRecordingIndicatorSystemApertureElement setAssistantIslandActive:];
-[SBRecordingIndicatorSystemApertureElement interSensorRegionIndicator];
-[SBRecordingIndicatorSystemApertureElement setIndicatorAwaitsSteady:];
-[SBRecordingIndicatorSystemApertureElement shouldSuppressElementWhileOverLiquidDetectionCriticalUI];
-[SBRecordingIndicatorSystemApertureElement didUpdateInterSensorRegionFrameInScreenSpace:];
-[SBRecordingIndicatorSystemApertureElement associatedBlankingRegionIdentifier];
-[SBRecordingIndicatorSystemApertureElement indicatorView];
-[SBRecordingIndicatorSystemApertureElement shouldSuppressElementWhileOnCoversheet];
-[SBRecordingIndicatorSystemApertureElement setInterSensorDwellTimerSatisfied:];
-[SBRecordingIndicatorSystemApertureElement _ensureSteadyRequirements];
-[SBRecordingIndicatorSystemApertureElement indicatorWantsCornerPosition];
-[SBRecordingIndicatorSystemApertureElement destinationWindowScene];
-[SBRecordingIndicatorSystemApertureElement indicatorContentRendersAsSquare];
-[SBRecordingIndicatorSystemApertureElement displayRegionBlankingManager];
-[SBRecordingIndicatorSystemApertureElement setAssociatedBlankingRegionIdentifier:];
-[SBRecordingIndicatorSystemApertureElement interSensorDwellTimerSatisfied];
-[SBRecordingIndicatorSystemApertureElement _startDwellTimer];
-[SBRecordingIndicatorSystemApertureElement setMinimumOnTimeCoordinator:];
-[SBRecordingIndicatorSystemApertureElement shouldSuppressElementWhileOtherElementsPresent];
-[SBRecordingIndicatorSystemApertureElement _ensureMotRequirements];
-[SBRecordingIndicatorSystemApertureElement setDisplayRegionBlankingManager:];
-[SBRecordingIndicatorSystemApertureElement systemApertureContainerView:didChangeFrame:];
-[SBRecordingIndicatorSystemApertureElement platformElementHost];
-[SBRecordingIndicatorSystemApertureElement hasIndicatorBehavior];
-[SBRecordingIndicatorSystemApertureElement setInterSensorRegionIndicator:];
-[SBRecordingIndicatorSystemApertureElement _updateRotationRateLimiterSettings];
-[SBRecordingIndicatorSystemApertureElement initWithInterSensorRegionIndicatorVisualRepresentation:microRegionIndicatorVisualRepresentation:recordingIndicatorManager:windowScene:assistantIslandActive:minimumOnTimeCoordinator:];
```
