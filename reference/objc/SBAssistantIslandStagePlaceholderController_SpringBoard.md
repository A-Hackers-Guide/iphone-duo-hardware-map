# `SBAssistantIslandStagePlaceholderController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneObserver`, `BSInvalidatable`
- 22 instance variables, 11 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"FBScene" _scene;
B _invalidated;
@"SBAssistantIslandSettings" _settings;
@"SBAppSwitcherSettings" _switcherSettings;
q _outsandingAnimations;
B _isContentReady;
q _stageState;
q _stageQuiescentPresentationState;
{?="nanostamp"Q"isPointerTouch"B"isCanceled"B"touchTimestamp"d"location"{CGPoint="x"d"y"d}"translation"{CGPoint="x"d"y"d}"velocity"{CGPoint="x"d"y"d}"hysteresis"d} _initialGestureState;
{?="nanostamp"Q"isPointerTouch"B"isCanceled"B"touchTimestamp"d"location"{CGPoint="x"d"y"d}"translation"{CGPoint="x"d"y"d}"velocity"{CGPoint="x"d"y"d}"hysteresis"d} _currentGestureState;
{?="nanostamp"Q"isPointerTouch"B"isCanceled"B"touchTimestamp"d"location"{CGPoint="x"d"y"d}"translation"{CGPoint="x"d"y"d}"velocity"{CGPoint="x"d"y"d}"hysteresis"d} _finalGestureState;
q _isPresented;
B _exceededExtendedGraceForProcessLaunch;
B _hasPerformedInitialLayout;
B _isActivityResignedActive;
@"UIViewFloatAnimatableProperty" _rampingProperty;
@"SBAssistantIslandStagePlaceholderWindow" _window;
@"<SBAssistantIslandStagePlaceholderControllerDelegate>" _delegate;
@"UIView" _coverView;
@"UIView" _searchGlassView;
@"UIView" _searchContentView;
@"UIView" _searchAccessoryView;
```

## Properties

```
@property (T@"FBScene",R,N,V_scene) scene;
@property (T@"SBAssistantIslandStagePlaceholderWindow",R,N,V_window) window;
@property (T@"<SBAssistantIslandStagePlaceholderControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"UIView",R,N,V_coverView) coverView;
@property (T@"UIView",R,N,V_searchGlassView) searchGlassView;
@property (T@"UIView",R,N,V_searchContentView) searchContentView;
@property (T@"UIView",R,N,V_searchAccessoryView) searchAccessoryView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAssistantIslandStagePlaceholderController _settings];
-[SBAssistantIslandStagePlaceholderController scene:didUpdateSettings:];
-[SBAssistantIslandStagePlaceholderController sceneContentStateDidChange:];
-[SBAssistantIslandStagePlaceholderController window];
-[SBAssistantIslandStagePlaceholderController _rubberband:fromMinV:maxV:range:factor:];
-[SBAssistantIslandStagePlaceholderController sceneDidInvalidate:];
-[SBAssistantIslandStagePlaceholderController invalidate];
-[SBAssistantIslandStagePlaceholderController setDelegate:];
-[SBAssistantIslandStagePlaceholderController scene];
-[SBAssistantIslandStagePlaceholderController delegate];
-[SBAssistantIslandStagePlaceholderController _clientSettings];
-[SBAssistantIslandStagePlaceholderController didUpdateGesture:];
-[SBAssistantIslandStagePlaceholderController didEndGesture:];
-[SBAssistantIslandStagePlaceholderController scene:didUpdateClientSettings:];
-[SBAssistantIslandStagePlaceholderController coverView];
-[SBAssistantIslandStagePlaceholderController _updatePlaceholder];
-[SBAssistantIslandStagePlaceholderController searchGlassView];
-[SBAssistantIslandStagePlaceholderController _updatePlaceholderSceneSettings];
-[SBAssistantIslandStagePlaceholderController _beginAnimatingRampingPropertyWithSettings:];
-[SBAssistantIslandStagePlaceholderController _createPlaceholderViews];
-[SBAssistantIslandStagePlaceholderController _evaluateContentReady];
-[SBAssistantIslandStagePlaceholderController _evaluatePlaceholder];
-[SBAssistantIslandStagePlaceholderController _evaluateStageState];
-[SBAssistantIslandStagePlaceholderController _updatePlaceholderIgnoreEvaluation:];
-[SBAssistantIslandStagePlaceholderController didBeginGesture:];
-[SBAssistantIslandStagePlaceholderController initWithScene:window:];
-[SBAssistantIslandStagePlaceholderController searchAccessoryView];
-[SBAssistantIslandStagePlaceholderController searchContentView];
```
