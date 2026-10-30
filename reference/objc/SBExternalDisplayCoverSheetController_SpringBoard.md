# `SBExternalDisplayCoverSheetController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBExternalDisplayCoverSheetControllerWindowFactory`, `SBSDisplayLayoutElementProviding`, `SBTouchTemplateGestureRecognizerDelegate`, `SBBacklightControllerObserver`, `SBCoverSheetPresentationManagerDismissalObserver`, `SBLockStateProviding`, `BSInvalidatable`
- 19 instance variables, 22 properties, 60 instance methods, 0 class methods

## Instance variables

```
B _isInvalidated;
@"NSHashTable" _lockStateObservers;
B _coversheetPresented;
B _transitioningToCoverSheetPresented;
B _shouldBeVisible;
B _screenOn;
B _noAnimations;
@"UIWindow" _coversheetWindow;
@"SBExternalDisplayCoverSheetViewController" _rootViewController;
@"SBSDisplayLayoutElement" _displayLayoutElement;
@"<BSInvalidatable>" _displayLayoutElementAssertion;
@"NSHashTable" _observers;
@"SBWindowScene" _sbWindowScene;
@"SBWindowSceneManager" _windowSceneManager;
@"SBBacklightController" _backlightController;
@"SBCoverSheetPresentationManager" _presentationManager;
@"<SBExternalDisplayCoverSheetControllerWindowFactory>" _windowFactory;
@"SBFMouseButtonDownGestureRecognizer" _mouseButtonDownGesture;
@"SBFluidScrunchGestureRecognizer" _scrunchDismissGestureRecognizer;
```

## Properties

```
@property (T@"UIWindow",&,N,V_coversheetWindow) coversheetWindow;
@property (T@"SBExternalDisplayCoverSheetViewController",&,N,V_rootViewController) rootViewController;
@property (T@"SBSDisplayLayoutElement",&,N,V_displayLayoutElement) displayLayoutElement;
@property (T@"<BSInvalidatable>",&,N,V_displayLayoutElementAssertion) displayLayoutElementAssertion;
@property (T@"NSHashTable",&,N,V_observers) observers;
@property (TB,N,G_isCoverSheetPresented,V_coversheetPresented) coversheetPresented;
@property (TB,N,G_isTransitioningToCoverSheetPresented,S_setTransitioningToCoverSheetPresented:,V_transitioningToCoverSheetPresented) transitioningToCoverSheetPresented;
@property (TB,N,V_shouldBeVisible) shouldBeVisible;
@property (T@"SBWindowScene",W,N,G_sbWindowScene,V_sbWindowScene) sbWindowScene;
@property (T@"SBWindowSceneManager",R,N,V_windowSceneManager) windowSceneManager;
@property (T@"SBBacklightController",R,N,V_backlightController) backlightController;
@property (T@"SBCoverSheetPresentationManager",R,N,V_presentationManager) presentationManager;
@property (T@"<SBExternalDisplayCoverSheetControllerWindowFactory>",R,N,V_windowFactory) windowFactory;
@property (T@"SBFMouseButtonDownGestureRecognizer",&,N,V_mouseButtonDownGesture) mouseButtonDownGesture;
@property (T@"SBFluidScrunchGestureRecognizer",&,N,V_scrunchDismissGestureRecognizer) scrunchDismissGestureRecognizer;
@property (TB,N,G_isScreenOn,S_setScreenOn:,V_screenOn) screenOn;
@property (TB,N,V_noAnimations) noAnimations;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,GisDisplayLayoutElementActive) displayLayoutElementActive;
```

## Instance methods

```
-[SBExternalDisplayCoverSheetController backlightController];
-[SBExternalDisplayCoverSheetController _setScreenOn:];
-[SBExternalDisplayCoverSheetController rootViewController];
-[SBExternalDisplayCoverSheetController setRootViewController:];
-[SBExternalDisplayCoverSheetController setDisplayLayoutElementActive:];
-[SBExternalDisplayCoverSheetController unlockWithRequest:completion:];
-[SBExternalDisplayCoverSheetController updateDisplayLayoutElementWithBuilder:];
-[SBExternalDisplayCoverSheetController backlightController:willAnimateBacklightToFactor:source:];
-[SBExternalDisplayCoverSheetController removeObserver:];
-[SBExternalDisplayCoverSheetController isUIUnlocking];
-[SBExternalDisplayCoverSheetController dealloc];
-[SBExternalDisplayCoverSheetController setScrunchDismissGestureRecognizer:];
-[SBExternalDisplayCoverSheetController _isScreenOn];
-[SBExternalDisplayCoverSheetController removeLockStateObserver:];
-[SBExternalDisplayCoverSheetController presentationManager];
-[SBExternalDisplayCoverSheetController viewForSystemGestureRecognizer:];
-[SBExternalDisplayCoverSheetController addObserver:];
-[SBExternalDisplayCoverSheetController invalidate];
-[SBExternalDisplayCoverSheetController windowSceneManager];
-[SBExternalDisplayCoverSheetController _sbWindowScene];
-[SBExternalDisplayCoverSheetController scrunchDismissGestureRecognizer];
-[SBExternalDisplayCoverSheetController setObservers:];
-[SBExternalDisplayCoverSheetController observers];
-[SBExternalDisplayCoverSheetController isUILocked];
-[SBExternalDisplayCoverSheetController isDisplayLayoutElementActive];
-[SBExternalDisplayCoverSheetController _wakeScreenForMouseButtonDown:];
-[SBExternalDisplayCoverSheetController addLockStateObserver:];
-[SBExternalDisplayCoverSheetController shouldBeVisible];
-[SBExternalDisplayCoverSheetController coverSheetPresentationManagerDidChangeDismissedSinceKeyBagLock:];
-[SBExternalDisplayCoverSheetController _embeddedLockStateDidChange:];
-[SBExternalDisplayCoverSheetController _handleScrunchGesture:];
-[SBExternalDisplayCoverSheetController _initWithWindowScene:windowSceneManager:backlightController:presentationManager:windowFactory:externalDisplayCoverSheetViewController:];
-[SBExternalDisplayCoverSheetController _isCoverSheetPresented];
-[SBExternalDisplayCoverSheetController _isTransitioningToCoverSheetPresented];
-[SBExternalDisplayCoverSheetController _notifyObserversDidUpdateExternalDisplayCoverSheetAppearance:];
-[SBExternalDisplayCoverSheetController _notifyObserversWillUpdateExternalDisplayCoverSheetAppearance:];
-[SBExternalDisplayCoverSheetController _postNotificationForExternalCoverSheetVisibilityDidChange:];
-[SBExternalDisplayCoverSheetController _setCoverSheetWindowVisible:fadeDuration:];
-[SBExternalDisplayCoverSheetController _setCoversheetPresented:];
-[SBExternalDisplayCoverSheetController _setTransitioningToCoverSheetPresented:];
-[SBExternalDisplayCoverSheetController _shouldIgnoreEmbeddedBacklightChangingSource:];
-[SBExternalDisplayCoverSheetController _shouldShowExternalCoverSheet];
-[SBExternalDisplayCoverSheetController _updateExternalDisplayCoverSheetExistence];
-[SBExternalDisplayCoverSheetController _updateLockStateObservers];
-[SBExternalDisplayCoverSheetController coversheetWindow];
-[SBExternalDisplayCoverSheetController displayLayoutElement];
-[SBExternalDisplayCoverSheetController displayLayoutElementAssertion];
-[SBExternalDisplayCoverSheetController initWithWindowScene:coverSheetPresentationManager:];
-[SBExternalDisplayCoverSheetController mouseButtonDownGesture];
-[SBExternalDisplayCoverSheetController newCoverSheetWindowForScene:];
-[SBExternalDisplayCoverSheetController noAnimations];
-[SBExternalDisplayCoverSheetController setCoversheetPresented:];
-[SBExternalDisplayCoverSheetController setCoversheetWindow:];
-[SBExternalDisplayCoverSheetController setDisplayLayoutElement:];
-[SBExternalDisplayCoverSheetController setDisplayLayoutElementAssertion:];
-[SBExternalDisplayCoverSheetController setMouseButtonDownGesture:];
-[SBExternalDisplayCoverSheetController setNoAnimations:];
-[SBExternalDisplayCoverSheetController setSbWindowScene:];
-[SBExternalDisplayCoverSheetController setShouldBeVisible:];
-[SBExternalDisplayCoverSheetController windowFactory];
```
