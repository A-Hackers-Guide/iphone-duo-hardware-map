# `SBInputUISceneController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSystemUISceneController`
- Protocols: `_UIKeyboardInputRehostingSceneHostObserver`, `FBSceneObserver`, `SBLayoutStateTransitionObserver`, `_UIKeyboardArbiterSceneDelegate`
- 9 instance variables, 9 properties, 38 instance methods, 2 class methods

## Instance variables

```
@"FBScene" _focusedScene;
I _focusedContextID;
@"SBTraitsPipelineManager" _currentTraitsPipelineManager;
@"<BSInvalidatable>" _hostingGraphObservationInvalidatable;
@"NSMutableDictionary" _inputUISceneControllerByDisplayIdentity;
@"NSHashTable" _observers;
B _focusedSceneResolvedFromEmbeddedRemoteAlert;
@"UIKBArbiterClientFocusContext" _rawKeyboardFocusContext;
@"SBResolvedKeyboardFocusContext" _resolvedKeyboardFocusContext;
```

## Properties

```
@property (T@"UIKBArbiterClientFocusContext",&,N,V_rawKeyboardFocusContext) rawKeyboardFocusContext;
@property (T@"SBResolvedKeyboardFocusContext",&,N,V_resolvedKeyboardFocusContext) resolvedKeyboardFocusContext;
@property (TB,R,N,GisHostedInSpringBoard) hostedInSpringBoard;
@property (TB,R,N,GisVisibleForSpringBoard) visibleForSpringBoard;
@property (T@"UIWindow",R,N) hostingWindow;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBInputUISceneController _setupInfo];
+[SBInputUISceneController _shouldControlInputUIScene];
```

## Instance methods

```
-[SBInputUISceneController terminateWithReason:];
-[SBInputUISceneController _setupDefaultPresentationForTargetHostingGraph:focusedScene:];
-[SBInputUISceneController initWithSceneWorkspaceIdentifier:clientProcessIdentity:sceneVendingPolicy:traitsRole:jobLabel:level:];
-[SBInputUISceneController keyboardInputRehostingSceneDidChangeKeyboardInTrackpadMode:];
-[SBInputUISceneController _currentTraitsPipelineManager];
-[SBInputUISceneController _didUpdateFocusContext:targetInputUISceneController:];
-[SBInputUISceneController _focusedContextIDForKeyboardFocusContext:focusedScene:];
-[SBInputUISceneController _userSwipedToKillFromSwitcher:];
-[SBInputUISceneController _focusedSceneForFocusedSceneTokenString:];
-[SBInputUISceneController removeObserver:];
-[SBInputUISceneController scene:didUpdateSettings:];
-[SBInputUISceneController windowSceneDidDisconnect:];
-[SBInputUISceneController _currentWindowScene];
-[SBInputUISceneController keyboardInTrackpadModeOnDisplay:];
-[SBInputUISceneController _updateDefaultPresenterForFocusedScene:contextID:];
-[SBInputUISceneController dealloc];
-[SBInputUISceneController _evaluateAvailablePresenters:forSceneControllers:];
-[SBInputUISceneController scenePresenter:willDismissScene:];
-[SBInputUISceneController focusContextDidChange:];
-[SBInputUISceneController _targetInputUISceneController];
-[SBInputUISceneController addObserver:];
-[SBInputUISceneController isHostedInSpringBoard];
-[SBInputUISceneController resolvedKeyboardFocusContext];
-[SBInputUISceneController layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:];
-[SBInputUISceneController scenePresenter:didPresentScene:];
-[SBInputUISceneController _backgroundInputUISceneController:forReason:];
-[SBInputUISceneController hostingWindow];
-[SBInputUISceneController rawKeyboardFocusContext];
-[SBInputUISceneController _focusedSceneForKeyboardFocusContext:];
-[SBInputUISceneController _isDefaultPresenterDelegate];
-[SBInputUISceneController isVisibleForSpringBoard];
-[SBInputUISceneController _foregroundInputUISceneController:];
-[SBInputUISceneController pointInScreenFixedCoordinateSpace:isInsideKeyboardContentOnDisplay:];
-[SBInputUISceneController windowSceneDidConnect:];
-[SBInputUISceneController keyboardInputRehostingSceneDidUpdate:];
-[SBInputUISceneController setResolvedKeyboardFocusContext:];
-[SBInputUISceneController descriptionBuilderWithMultilinePrefix:];
-[SBInputUISceneController setRawKeyboardFocusContext:];
```
