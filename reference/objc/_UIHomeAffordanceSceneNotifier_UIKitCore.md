# `_UIHomeAffordanceSceneNotifier`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIHomeAffordanceNotifyingInternal`, `_UIHomeAffordanceNotifying`
- 9 instance variables, 8 properties, 22 instance methods, 0 class methods

## Instance variables

```
{?="hasInvalidated"b1"expectsLegacyViewServiceObservers"b1} _flags;
@"<BSInvalidatable>" _stateCaptureToken;
B _hasInvalidated;
@"UIScene" _scene;
@"NSMutableSet" _registeredObserverRecords;
@"NSMutableArray" _trackedLegacyViewServiceSessions;
@"NSMapTable" _hostedWindowToLegacyViewServiceSessions;
@"NSMapTable" _legacyViewServiceSessionToHomeAffordanceSceneReferenceFrames;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _homeAffordanceSceneReferenceFrameForScene;
```

## Properties

```
@property (TB,R,N,V_hasInvalidated) _hasInvalidated;
@property (T@"NSMutableSet",R,C,N,V_registeredObserverRecords) _registeredObserverRecords;
@property (T@"UIScene<_UISceneUIWindowHosting>",R,W,N) windowHostingScene;
@property (T@"UIScene",W,N,G_scene,S_setScene:,V_scene) _scene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIHomeAffordanceSceneNotifier _reset];
-[_UIHomeAffordanceSceneNotifier _legacyViewServiceSessionDidAssociateWithWindow:];
-[_UIHomeAffordanceSceneNotifier _scene];
-[_UIHomeAffordanceSceneNotifier debugDescription];
-[_UIHomeAffordanceSceneNotifier cleanupForDetachingWindow:];
-[_UIHomeAffordanceSceneNotifier init];
-[_UIHomeAffordanceSceneNotifier _registeredObserverRecords];
-[_UIHomeAffordanceSceneNotifier _sceneWillInvalidate:];
-[_UIHomeAffordanceSceneNotifier dealloc];
-[_UIHomeAffordanceSceneNotifier initWithScene:];
-[_UIHomeAffordanceSceneNotifier homeAffordanceSceneReferenceFrameForWindow:];
-[_UIHomeAffordanceSceneNotifier _legacyViewServiceSessionDidInvalidate:];
-[_UIHomeAffordanceSceneNotifier _legacyViewServiceSessionWasCreated:];
-[_UIHomeAffordanceSceneNotifier succinctDescription];
-[_UIHomeAffordanceSceneNotifier _hasInvalidated];
-[_UIHomeAffordanceSceneNotifier windowHostingScene];
-[_UIHomeAffordanceSceneNotifier description];
-[_UIHomeAffordanceSceneNotifier registerHomeAffordanceObserver:inWindow:];
-[_UIHomeAffordanceSceneNotifier appendDescriptionToStream:];
-[_UIHomeAffordanceSceneNotifier _setScene:];
-[_UIHomeAffordanceSceneNotifier _unregisterHomeAffordanceObserverForRecord:];
-[_UIHomeAffordanceSceneNotifier _legacyViewServiceSessionDidDisassociateFromWindow:];
```
