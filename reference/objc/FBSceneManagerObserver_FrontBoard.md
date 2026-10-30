# `FBSceneManagerObserver`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `FBSceneWorkspaceDelegate_Internal`, `FBSceneManagerObserver`, `FBSceneManagerDelegate_Private`
- 20 instance variables, 6 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"<FBSceneManagerObserver>" _observer;
Q _observerAddress;
# _observerClass;
B _isDelegate;
B _privateDelegate;
B _didDestroyDEPRECATED;
B _willUpdateSceneDEPRECATED;
B _willCommitDEPRECATED;
B _didCommitDEPRECATED;
B _didAddLEGACY;
B _willRemoveLEGACY;
B _interceptSceneUpdatesLEGACY;
B _clientDidConnectLEGACY;
B _didReceiveSceneRequestLEGACY;
B _didAdd;
B _willRemove;
B _clientDidConnect;
B _didReceiveSceneRequest;
B _didReceiveScene;
B _didReceiveActions;
```

## Properties

```
@property (T@,R,W,N,V_observer) observer;
@property (T@,R,W,N) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSceneManagerObserver isDelegate];
-[FBSceneManagerObserver sceneManager:didCommitUpdateForScene:transactionID:];
-[FBSceneManagerObserver workspace:clientDidConnectWithHandshake:];
-[FBSceneManagerObserver workspace:didReceiveSceneRequestWithOptions:fromProcess:completion:];
-[FBSceneManagerObserver observer];
-[FBSceneManagerObserver delegateReceivesActions];
-[FBSceneManagerObserver succinctDescriptionBuilder];
-[FBSceneManagerObserver initWithDelegate:workspace:];
-[FBSceneManagerObserver delegateHandlesClientScenes];
-[FBSceneManagerObserver workspace:didReceiveScene:withContext:fromProcess:];
-[FBSceneManagerObserver workspace:willRemoveScene:];
-[FBSceneManagerObserver sceneManager:didDestroyScene:];
-[FBSceneManagerObserver _initWithObserver:workspace:];
-[FBSceneManagerObserver delegateHandlesLegacyInterception];
-[FBSceneManagerObserver workspace:didAddScene:];
-[FBSceneManagerObserver _privateDelegate];
-[FBSceneManagerObserver descriptionWithMultilinePrefix:];
-[FBSceneManagerObserver sceneManager:didCreateScene:];
-[FBSceneManagerObserver succinctDescription];
-[FBSceneManagerObserver delegate];
-[FBSceneManagerObserver sceneManager:willCommitUpdateForScene:transactionID:];
-[FBSceneManagerObserver hash];
-[FBSceneManagerObserver description];
-[FBSceneManagerObserver sceneManager:interceptUpdateForScene:withNewSettings:];
-[FBSceneManagerObserver sceneManager:clientDidConnectWithHandshake:];
-[FBSceneManagerObserver sceneManager:willRemoveScene:];
-[FBSceneManagerObserver workspace:didReceiveActions:];
-[FBSceneManagerObserver isEqual:];
-[FBSceneManagerObserver sceneManager:willUpdateScene:withSettings:transitionContext:];
-[FBSceneManagerObserver initWithObserver:workspace:];
-[FBSceneManagerObserver sceneManager:didAddScene:];
-[FBSceneManagerObserver descriptionBuilderWithMultilinePrefix:];
```
