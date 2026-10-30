# `SBTapToWakeController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`
- 14 instance variables, 20 properties, 37 instance methods, 1 class methods

## Instance variables

```
B _digitizerInTapToWakeMode;
B _digitizerModeRequiresHitTestSuppression;
B _gesturesEnabled;
B _lastEvaluatedShouldTapToWake;
B _lastEvaluatedHasTapToWakeHandler;
@"<SBTapToWakeDelegate>" _delegate;
@"SBWindowScene" _windowScene;
@"SBSystemGestureManager" _systemGestureManager;
@"SBFTapToWakeGestureRecognizer" _tapToWakeGestureRecognizer;
@"SBFTapToWakeGestureRecognizer" _pencilToWakeGestureRecognizer;
@"SBIdleTimerDefaults" _idleTimerDefaults;
@"BSCompoundAssertion" _disableTapToWakeAssertions;
@"BSCompoundAssertion" _tapToWakeHandlerAssertions;
@"<BSInvalidatable>" _touchSuppressionAssertion;
```

## Properties

```
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (T@"SBSystemGestureManager",&,N,V_systemGestureManager) systemGestureManager;
@property (T@"SBFTapToWakeGestureRecognizer",&,N,V_tapToWakeGestureRecognizer) tapToWakeGestureRecognizer;
@property (T@"SBFTapToWakeGestureRecognizer",&,N,V_pencilToWakeGestureRecognizer) pencilToWakeGestureRecognizer;
@property (T@"SBIdleTimerDefaults",&,N,V_idleTimerDefaults) idleTimerDefaults;
@property (T@"BSCompoundAssertion",R,N,V_disableTapToWakeAssertions) disableTapToWakeAssertions;
@property (T@"BSCompoundAssertion",R,N,V_tapToWakeHandlerAssertions) tapToWakeHandlerAssertions;
@property (TB,N,G_gesturesEnabled,S_setGesturesEnabled:,V_gesturesEnabled) gesturesEnabled;
@property (T@"<BSInvalidatable>",&,N,V_touchSuppressionAssertion) touchSuppressionAssertion;
@property (TB,N,V_lastEvaluatedShouldTapToWake) lastEvaluatedShouldTapToWake;
@property (TB,N,V_lastEvaluatedHasTapToWakeHandler) lastEvaluatedHasTapToWakeHandler;
@property (T@"<SBTapToWakeDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisDigitizerInTapToWakeMode,V_digitizerInTapToWakeMode) digitizerInTapToWakeMode;
@property (TB,N,V_digitizerModeRequiresHitTestSuppression) digitizerModeRequiresHitTestSuppression;
@property (TB,R,N) shouldTapToWake;
@property (TB,R,N) hasTapToWakeHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBTapToWakeController isTapToWakeSupported];
```

## Instance methods

```
-[SBTapToWakeController isDigitizerInTapToWakeMode];
-[SBTapToWakeController lastEvaluatedHasTapToWakeHandler];
-[SBTapToWakeController setSystemGestureManager:];
-[SBTapToWakeController acquireTapToWakeHandlerAssertionForReason:handler:];
-[SBTapToWakeController setWindowScene:];
-[SBTapToWakeController pencilToWakeGestureRecognizer];
-[SBTapToWakeController setTouchSuppressionAssertion:];
-[SBTapToWakeController tapToWakeDidRecognize:];
-[SBTapToWakeController disableTapToWakeAssertions];
-[SBTapToWakeController setLastEvaluatedHasTapToWakeHandler:];
-[SBTapToWakeController dealloc];
-[SBTapToWakeController setDigitizerInTapToWakeMode:];
-[SBTapToWakeController pencilToWakeDidRecognize:];
-[SBTapToWakeController tapToWakeGestureRecognizer];
-[SBTapToWakeController initWithWindowScene:];
-[SBTapToWakeController setTapToWakeGestureRecognizer:];
-[SBTapToWakeController lastEvaluatedShouldTapToWake];
-[SBTapToWakeController setDelegate:];
-[SBTapToWakeController systemGestureManager];
-[SBTapToWakeController setDigitizerModeRequiresHitTestSuppression:];
-[SBTapToWakeController idleTimerDefaults];
-[SBTapToWakeController _setGesturesEnabled:];
-[SBTapToWakeController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[SBTapToWakeController delegate];
-[SBTapToWakeController acquireDisableTapToWakeAssertionForReason:];
-[SBTapToWakeController setLastEvaluatedShouldTapToWake:];
-[SBTapToWakeController _gesturesEnabled];
-[SBTapToWakeController _evaluateEnablement];
-[SBTapToWakeController digitizerModeRequiresHitTestSuppression];
-[SBTapToWakeController windowScene];
-[SBTapToWakeController tapToWakeHandlerAssertions];
-[SBTapToWakeController hasTapToWakeHandler];
-[SBTapToWakeController shouldTapToWake];
-[SBTapToWakeController touchSuppressionAssertion];
-[SBTapToWakeController setIdleTimerDefaults:];
-[SBTapToWakeController setPencilToWakeGestureRecognizer:];
-[SBTapToWakeController noteRecognizedTapWillWakeScreen];
```
