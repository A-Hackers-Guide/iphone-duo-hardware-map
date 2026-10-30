# `SBReachabilityController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemGestureRecognizerDelegate`, `SBFZStackParticipantDelegate`, `PTSettingsKeyObserver`, `BSInvalidatable`
- 24 instance variables, 13 properties, 56 instance methods, 2 class methods

## Instance variables

```
@"AWAttentionAwarenessClient" _attentionAwarenessClient;
@"NSHashTable" _observers;
B _reachabilityModeActive;
Q _reachabilityExtensionGenerationCount;
B _reachabilityModeEnabled;
@"NSMutableSet" _temporaryEnabledReasons;
@"NSMutableSet" _temporaryDisabledReasons;
@"SBReachabilityWindow" _reachabilityWindow;
@"UITransform" _reachabilityTransform;
@"UITransform" _inverseReachabilityTransform;
@"UITapGestureRecognizer" _dismissTapGestureRecognizer;
@"SBFZStackParticipant" _zStackParticipant;
@"NSHashTable" _ignoredWindows;
q _animationsInFlight;
@"<SAInvalidatable>" _jindoInertAssertion;
@"BSContinuousMachTimer" _jindoInertTimer;
@"SBReachabilitySettings" _settings;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _reachabilityBoundsInPixels;
B _invalidated;
@"SBReachabilityGestureRecognizer" _reachabilityGestureRecognizer;
d _effectiveReachabilityYOffset;
@"SBScreenEdgePanGestureRecognizer" _dismissEdgeGestureRecognizer;
@"UIPanGestureRecognizer" _dismissPanGestureRecognizer;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (TB,R,N,V_reachabilityModeActive) reachabilityModeActive;
@property (TB,R,N) reachabilityModeAnimating;
@property (TB,N) reachabilityEnabled;
@property (T@"SBReachabilityGestureRecognizer",R,N,V_reachabilityGestureRecognizer) reachabilityGestureRecognizer;
@property (T@"SBScreenEdgePanGestureRecognizer",R,N,V_dismissEdgeGestureRecognizer) dismissEdgeGestureRecognizer;
@property (T@"UIPanGestureRecognizer",R,N,V_dismissPanGestureRecognizer) dismissPanGestureRecognizer;
@property (Td,R,N) reachabilityYOffset;
@property (Td,R,N,V_effectiveReachabilityYOffset) effectiveReachabilityYOffset;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBReachabilityController _reachabilitySupported];
+[SBReachabilityController _reachabilitySupportedOnWindowScene:];
```

## Instance methods

```
-[SBReachabilityController reachabilityEnabled];
-[SBReachabilityController _screenDidDim];
-[SBReachabilityController effectiveReachabilityYOffset];
-[SBReachabilityController setWindowScene:];
-[SBReachabilityController _setupGestureRecognizers];
-[SBReachabilityController gestureRecognizer:shouldReceiveTouch:];
-[SBReachabilityController zStackParticipant:updatePreferences:];
-[SBReachabilityController removeObserver:];
-[SBReachabilityController dealloc];
-[SBReachabilityController zStackParticipantDidChange:];
-[SBReachabilityController zStackParticipant:updateZOrderPreferences:];
-[SBReachabilityController settings:changedValueForKey:];
-[SBReachabilityController viewForSystemGestureRecognizer:];
-[SBReachabilityController initWithWindowScene:];
-[SBReachabilityController addObserver:];
-[SBReachabilityController invalidate];
-[SBReachabilityController gestureRecognizerShouldBegin:];
-[SBReachabilityController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[SBReachabilityController setReachabilityEnabled:];
-[SBReachabilityController windowScene];
-[SBReachabilityController deactivateReachability];
-[SBReachabilityController toggleReachability];
-[SBReachabilityController dismissPanGestureRecognizer];
-[SBReachabilityController _activateReachability:];
-[SBReachabilityController _applyInteractiveConfiguration];
-[SBReachabilityController _applyNonInteractiveConfiguration];
-[SBReachabilityController _attentionAwarenessConfigurationWithTimeout:tag:];
-[SBReachabilityController _calculateReachabilityBoundsInPixels];
-[SBReachabilityController _invalidateJindoReason];
-[SBReachabilityController _modifyDefaultPresentationContextHostTransformForWindow:fromTransform:toTransform:];
-[SBReachabilityController _notifyObserversDidEndReachabilityAnimation];
-[SBReachabilityController _notifyObserversReachabilityModeActive:];
-[SBReachabilityController _notifyObserversReachabilityYOffsetDidChange];
-[SBReachabilityController _notifyObserversWillBeginReachabilityAnimation];
-[SBReachabilityController _panToDeactivateReachability:];
-[SBReachabilityController _sceneForWindow:];
-[SBReachabilityController _setKeepAliveTimer];
-[SBReachabilityController _setupReachabilityWindowIfNecessary];
-[SBReachabilityController _tapToDeactivateReachability:];
-[SBReachabilityController _tearDownReachabilityWindow];
-[SBReachabilityController _toggleReachabilityMode];
-[SBReachabilityController _transitionWithTransformer:fromTransform:toTransform:];
-[SBReachabilityController _updateReachabilityModeActive:];
-[SBReachabilityController _updateReachabilityModeActive:animated:];
-[SBReachabilityController _updateReachabilityWindowForYOffset:mode:completion:];
-[SBReachabilityController canActivateReachability];
-[SBReachabilityController dismissEdgeGestureRecognizer];
-[SBReachabilityController ignoreWindowForReachability:];
-[SBReachabilityController ignoredWindows];
-[SBReachabilityController reachabilityGestureRecognizer];
-[SBReachabilityController reachabilityModeActive];
-[SBReachabilityController reachabilityModeAnimating];
-[SBReachabilityController reachabilityYOffset];
-[SBReachabilityController setReachabilityTemporarilyDisabled:forReason:];
-[SBReachabilityController setReachabilityTemporarilyEnabled:forReason:];
-[SBReachabilityController stopIgnoringWindowForReachability:];
```
