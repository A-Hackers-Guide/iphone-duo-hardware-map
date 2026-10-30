# `SBBacklightController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHBacklightHostObserving`, `SBDisplayContentModeTransitionObserver`
- 23 instance variables, 19 properties, 59 instance methods, 5 class methods

## Instance variables

```
@"<SBBacklightControllerContextProviding>" _contextProvider;
@"NSHashTable" _observers;
@"NSHashTable" _informers;
@? _backlightCompletion;
q _lastReportedWillTransitionState;
@"BrightnessSystemClient" _brightnessSystemClient;
@"BLSAssertion" _disableAODAssertion;
@"SBBLSAssertionWrapper" _disableAODForDisplayContentModeAssertion;
@"SBAlwaysOnDefaults" _alwaysOnDefaults;
@"SBDisplayLinkController" _mainDisplayLinkController;
@"BSCompoundAssertion" _tapToInteractAssertions;
@"BSCompoundAssertion" _extendedWakeGesturesAssertions;
@"BSCompoundAssertion" _displayContentModePrewarmAssertions;
{?="stateToRestore"q"sourceToRestore"q"animatedRestore"B"applying"B} _prewarmAttributes;
@"BSCompoundAssertion" _wakeSwipeEdgesAssertions;
@"BSCompoundAssertion" _edgeWakeOnlyAssertions;
B _digitizerDisabled;
B _tapToWakeEnabled;
B _tapToWakeRequiresHitTestSuppression;
q _lastBacklightChangeSource;
@"<BSInvalidatable>" _currentHIDUISensorModeAssertion;
@"<BSInvalidatable>" _currentDisplayStateAssertion;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"<BSInvalidatable>",&,N,V_currentHIDUISensorModeAssertion) currentHIDUISensorModeAssertion;
@property (T@"<BSInvalidatable>",&,N,V_currentDisplayStateAssertion) currentDisplayStateAssertion;
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (T@"<BLSHBacklightHostObservable><BLSBacklightChangeRequestable>",R,N) blsBacklightHost;
@property (TB,R,N) screenIsOn;
@property (TB,R,N) screenIsDim;
@property (Tq,R,N,V_lastBacklightChangeSource) lastBacklightChangeSource;
@property (TB,R,N,GisDigitizerDisabled,V_digitizerDisabled) digitizerDisabled;
@property (TB,R,N,GisTapToWakeEnabled,V_tapToWakeEnabled) tapToWakeEnabled;
@property (TB,R,N,V_tapToWakeRequiresHitTestSuppression) tapToWakeRequiresHitTestSuppression;
@property (TB,R,N,GisPrewarmingDisplayContentMode) prewarmingDisplayContentMode;
@property (T@"SBDisplayLinkController",R,N,V_mainDisplayLinkController) mainDisplayLinkController;
@property (T@"<BLSDisplay>",R,N) blsDisplay;
@property (Tq,R,N) backlightState;
@property (T@"<BLSBacklightStateObservable><BLSBacklightChangeRequestable>",R,N) blsBacklight;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBBacklightController _factorToPublishForBacklightState:];
+[SBBacklightController _sharedInstanceCreateIfNeeded:];
+[SBBacklightController externalDisplayDummyBacklightControllerForWindowScene:];
+[SBBacklightController sharedInstanceForMainDisplay];
+[SBBacklightController sharedInstanceForMainDisplayIfExists];
```

## Instance methods

```
-[SBBacklightController isPrewarmingDisplayContentMode];
-[SBBacklightController setBacklightState:source:animated:completion:];
-[SBBacklightController blsBacklight];
-[SBBacklightController acquireExtendedWakeGesturesAssertionForReason:];
-[SBBacklightController _noteDigitizerDisabled:tapToWakeEnabled:disabledDigitizerMode:];
-[SBBacklightController removeObserver:];
-[SBBacklightController lastBacklightChangeSource];
-[SBBacklightController displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBBacklightController _invalidateDisplayContentModePrewarmDiscardingStateToRestore];
-[SBBacklightController acquireWakeSwipeEdges:forReason:];
-[SBBacklightController _updateAODDisablementForContentMode:completion:];
-[SBBacklightController _undimFromSource:];
-[SBBacklightController dealloc];
-[SBBacklightController displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBBacklightController unregisterInformer:];
-[SBBacklightController backlight:didCompleteUpdateToState:forEvent:];
-[SBBacklightController _factorToPublishForBacklightState:];
-[SBBacklightController _notifyObserversWillAnimateToFactor:source:];
-[SBBacklightController _restoreStateAfterDisplayContentModePrewarm];
-[SBBacklightController screenIsDim];
-[SBBacklightController _deferBacklightStateForPrewarm:source:animated:];
-[SBBacklightController _performDeferredBacklightRampWorkWithInfo:];
-[SBBacklightController initWithWindowScene:];
-[SBBacklightController _startFadeOutAnimationFromLockSource:];
-[SBBacklightController turnOnScreenFullyWithBacklightSource:];
-[SBBacklightController addObserver:];
-[SBBacklightController backlightState];
-[SBBacklightController isDigitizerDisabled];
-[SBBacklightController registerInformer:];
-[SBBacklightController screenIsOn];
-[SBBacklightController currentHIDUISensorModeAssertion];
-[SBBacklightController prewarmDisplayForReason:source:];
-[SBBacklightController _notifyObserversDidTransitionToBacklightState:source:];
-[SBBacklightController updateAODDisablementForContentModeAndSetBacklightState:source:animated:completion:];
-[SBBacklightController isTapToWakeEnabled];
-[SBBacklightController _notifyObserversWillTransitionToBacklightState:source:];
-[SBBacklightController setCurrentHIDUISensorModeAssertion:];
-[SBBacklightController initWithContextProvider:];
-[SBBacklightController _performBacklightChangeRequest:completion:];
-[SBBacklightController setCurrentDisplayStateAssertion:];
-[SBBacklightController blsBacklightHost];
-[SBBacklightController acquireTapToInteractAssertionForReason:];
-[SBBacklightController turnOnScreenFullyWithBacklightSource:completion:];
-[SBBacklightController currentDisplayStateAssertion];
-[SBBacklightController completeStartup];
-[SBBacklightController _userInterfaceStyleChanged];
-[SBBacklightController tapToWakeRequiresHitTestSuppression];
-[SBBacklightController windowScene];
-[SBBacklightController mainDisplayLinkController];
-[SBBacklightController blsDisplay];
-[SBBacklightController _notifyObserversDidAnimateToFactor:source:];
-[SBBacklightController _updateHIDUISensorModeForBacklightState:source:];
-[SBBacklightController shouldTurnOnScreenForBacklightSource:];
-[SBBacklightController acquireSwipeToWakeOnlyAssertionForReason:];
-[SBBacklightController backlightHost:willTransitionToState:forEvent:];
-[SBBacklightController setBacklightState:source:];
-[SBBacklightController noteTapToWakeEnablementDidChange];
-[SBBacklightController _setBacklightState:fromBacklightState:source:animated:completion:];
-[SBBacklightController _appendWindowSceneToNotificationUserInfo:];
```
