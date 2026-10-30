# `_SBSceneHandleObserverBehavior`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _didCreateScene;
B _clientConnectedForScene;
B _didDestroyScene;
B _didUpdateContentState;
B _didUpdateSettingsWithDiff;
B _didUpdateClientSettings;
@"<SBSceneHandleObserver>" _observer;
```

## Properties

```
@property (T@"<SBSceneHandleObserver>",R,W,N,V_observer) observer;
@property (TB,N,V_didCreateScene) didCreateScene;
@property (TB,N,V_clientConnectedForScene) clientConnectedForScene;
@property (TB,N,V_didDestroyScene) didDestroyScene;
@property (TB,N,V_didUpdateContentState) didUpdateContentState;
@property (TB,N,V_didUpdateSettingsWithDiff) didUpdateSettingsWithDiff;
@property (TB,N,V_didUpdateClientSettings) didUpdateClientSettings;
```

## Class methods

```
+[_SBSceneHandleObserverBehavior behaviorFromObserver:];
```

## Instance methods

```
-[_SBSceneHandleObserverBehavior observer];
-[_SBSceneHandleObserverBehavior initWithObserver:];
-[_SBSceneHandleObserverBehavior didDestroyScene];
-[_SBSceneHandleObserverBehavior clientConnectedForScene];
-[_SBSceneHandleObserverBehavior didCreateScene];
-[_SBSceneHandleObserverBehavior didUpdateClientSettings];
-[_SBSceneHandleObserverBehavior didUpdateContentState];
-[_SBSceneHandleObserverBehavior didUpdateSettingsWithDiff];
-[_SBSceneHandleObserverBehavior setClientConnectedForScene:];
-[_SBSceneHandleObserverBehavior setDidCreateScene:];
-[_SBSceneHandleObserverBehavior setDidDestroyScene:];
-[_SBSceneHandleObserverBehavior setDidUpdateClientSettings:];
-[_SBSceneHandleObserverBehavior setDidUpdateContentState:];
-[_SBSceneHandleObserverBehavior setDidUpdateSettingsWithDiff:];
```
