# `SBSceneHandle`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneObserver`, `BSDescriptionProviding`
- 11 instance variables, 15 properties, 59 instance methods, 0 class methods

## Instance variables

```
@"FBSSceneDefinition" _definition;
@"FBScene" _scene;
@"FBSDisplayIdentity" _displayIdentity;
@"NSHashTable" _observers;
@"NSMapTable" _observersToObserverBehaviors;
@"NSHashTable" _actionConsumers;
Q _hash;
B _skipSceneActivationCallback;
B _skipClientDidConnectCallback;
B _hasSentDidCreate;
B _hasSentClientConnected;
```

## Properties

```
@property (TB,R,N,GisEffectivelyForeground) effectivelyForeground;
@property (T@"FBSSceneDefinition",R,N,G_definition,V_definition) definition;
@property (T@"FBSSceneIdentity",R,N,G_sceneIdentity) sceneIdentity;
@property (T@"FBSDisplayIdentity",&,N,S_setDisplayIdentity:) displayIdentity;
@property (T@"NSString",R,C,N) sceneIdentifier;
@property (T@"FBScene",R,N) scene;
@property (T@"FBScene",R,N,V_scene) sceneIfExists;
@property (T@"FBSDisplayConfiguration",R,N) displayConfiguration;
@property (Tq,R,N) contentState;
@property (TB,R,N,GisContentReady) contentReady;
@property (TB,R,N,GisClientConnected) clientConnected;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSceneHandle _commonInit];
-[SBSceneHandle isContentReady];
-[SBSceneHandle scene:clientDidConnect:];
-[SBSceneHandle displayConfiguration];
-[SBSceneHandle _didUpdateClientSettings:];
-[SBSceneHandle succinctDescriptionBuilder];
-[SBSceneHandle removeObserver:];
-[SBSceneHandle scene:didUpdateSettings:];
-[SBSceneHandle scene:handleActions:];
-[SBSceneHandle init];
-[SBSceneHandle sceneDidActivate:];
-[SBSceneHandle isDeviceApplicationSceneHandle];
-[SBSceneHandle isEffectivelyForeground];
-[SBSceneHandle dealloc];
-[SBSceneHandle sceneContentStateDidChange:];
-[SBSceneHandle descriptionWithMultilinePrefix:];
-[SBSceneHandle _didDestroyScene:];
-[SBSceneHandle succinctDescription];
-[SBSceneHandle _didCreateScene:];
-[SBSceneHandle addObserver:];
-[SBSceneHandle sceneIdentifier];
-[SBSceneHandle newSceneViewController];
-[SBSceneHandle _noteDidMoveFromDisplay:];
-[SBSceneHandle scene];
-[SBSceneHandle _clientConnectedForScene:];
-[SBSceneHandle newScenePlaceholderContentContextWithActivationSettings:];
-[SBSceneHandle hash];
-[SBSceneHandle _didUpdateSettingsWithDiff:previousSettings:];
-[SBSceneHandle description];
-[SBSceneHandle newSceneViewWithReferenceSize:contentOrientation:containerOrientation:hostRequester:];
-[SBSceneHandle _setScene:];
-[SBSceneHandle isEqual:];
-[SBSceneHandle displayIdentity];
-[SBSceneHandle scene:didUpdateClientSettings:];
-[SBSceneHandle descriptionBuilderWithMultilinePrefix:];
-[SBSceneHandle _enumerateObserversWithBlock:];
-[SBSceneHandle contentState];
-[SBSceneHandle _definition];
-[SBSceneHandle isClientConnected];
-[SBSceneHandle _initWithScene:displayIdentity:];
-[SBSceneHandle _didUpdateContentState:];
-[SBSceneHandle _initWithDefinition:displayIdentity:];
-[SBSceneHandle _initWithDefinition:scene:displayIdentity:];
-[SBSceneHandle _noteClientConnectedForScene:];
-[SBSceneHandle _noteSceneCreated:];
-[SBSceneHandle _noteSceneDestroyed:];
-[SBSceneHandle _noteSceneWillDeactivate:];
-[SBSceneHandle _resetFutureActivationCallbacksForScene:];
-[SBSceneHandle _sceneIdentity];
-[SBSceneHandle _seedSystemDisplayIdentifierForDisplayIdentityIfNeeded:];
-[SBSceneHandle _setDisplayIdentity:];
-[SBSceneHandle _willDeactivateScene:];
-[SBSceneHandle addActionConsumer:];
-[SBSceneHandle hasSentClientConnected];
-[SBSceneHandle hasSentSceneDidCreate];
-[SBSceneHandle removeActionConsumer:];
-[SBSceneHandle sceneIfExists];
-[SBSceneHandle skipSceneActivationCallback];
-[SBSceneHandle skipSceneClientConnectionCallback];
```
