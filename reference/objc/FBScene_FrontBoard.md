# `FBScene`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSSceneObserver`, `FBSComponentSceneSupport`, `FBSInvocationReceiving`, `FBSceneHost`, `BSDescriptionProviding`, `FBSSceneExtensible`
- 44 instance variables, 24 properties, 84 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"FBSceneLayerManager" _layerManager;
@"FBSceneObserver" _delegateProxy;
@"NSMutableOrderedSet" _lock_observerProxies;
@"<BSInvalidatable>" _stateCaptureAssertion;
@"FBSceneEventQueue" _eventQueue;
@"<NSObject>" _clientToken;
@"<FBSceneClient>" _client;
@"FBProcess" _clientProcess;
@"NSString" _identifier;
@"NSString" _workspaceIdentifier;
@"FBSSceneIdentityToken" _identityToken;
@"FBSSceneSettings" _settings;
@"FBSSceneClientSettings" _clientSettings;
@"FBSSceneDefinition" _definition;
@"FBSceneRemnant" _remnant;
@"FBSSceneSettings" _settingsAtDeactivation;
@"NSMapTable" _components;
@"NSMutableArray" _orderedComponents;
@"FBSScene" _parentScene;
@"FBSSceneUpdate" _settingsUpdate;
@? _updateCompletion;
@"<BSInvalidatable>" _updateSuspendIdleWork;
Q _activationID;
Q _transactionID;
Q _lastForegroundingTransitionID;
C _updateDepth;
B _contentStateIsChanging;
B _legacy;
B _active;
B _deactivating;
B _invalidated;
B _legacyActivated;
B _midUpdate;
B _finishedInit;
B _newlyReparented;
B _updateShouldActivate;
B _componentInit;
B _configuringParameters;
B _updatePendingFinalize;
B _inTransaction;
@"FBSceneClientHandle" _clientHandle;
q _contentState;
@"FBSceneWorkspace" _workspace;
```

## Properties

```
@property (TQ,R,N,V_transactionID) _transactionID;
@property (TB,R,N,G_isInTransaction,V_inTransaction) _inTransaction;
@property (T@"FBProcess",R,N,V_clientProcess) clientProcess;
@property (T@"<FBSceneDelegate>",W,N) delegate;
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T@"NSString",R,C,N,V_workspaceIdentifier) workspaceIdentifier;
@property (T@"FBSSceneDefinition",R,C,N,V_definition) definition;
@property (T@"FBSSceneIdentity",R,C,N) identity;
@property (T@"FBSSceneIdentityToken",R,C,N,V_identityToken) identityToken;
@property (T@"FBSSceneSettings",R,N,V_settings) settings;
@property (T@"FBSSceneClientSettings",R,N,V_clientSettings) clientSettings;
@property (T@"FBSSceneParameters",R,C,N) parameters;
@property (Tq,R,N,V_contentState) contentState;
@property (T@"FBSceneLayerManager",R,N,V_layerManager) layerManager;
@property (TB,R,N,GisValid) valid;
@property (TB,R,N,GisActive,V_active) active;
@property (T@"FBSceneClientHandle",R,N,V_clientHandle) clientHandle;
@property (T@"FBSScene",W,N,V_parentScene) parentScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<FBSProcess>",R,C,N) hostProcess;
@property (T@"FBSSceneSpecification",R,C,N) specification;
```

## Instance methods

```
-[FBScene invalidate:];
-[FBScene _objc_initiateDealloc];
-[FBScene definition];
-[FBScene hostProcess];
-[FBScene parameters];
-[FBScene display];
-[FBScene clientProcess];
-[FBScene performUpdate:];
-[FBScene sendActions:];
-[FBScene debugDescription];
-[FBScene loggingIdentifier];
-[FBScene identifier];
-[FBScene succinctDescriptionBuilder];
-[FBScene removeObserver:];
-[FBScene scene:didUpdateSettings:];
-[FBScene deactivate:];
-[FBScene settings];
-[FBScene add:];
-[FBScene remove:];
-[FBScene dealloc];
-[FBScene addExtension:];
-[FBScene addExtensions:];
-[FBScene descriptionWithMultilinePrefix:];
-[FBScene isMutable];
-[FBScene _createTransitionContext];
-[FBScene currentInterfaceOrientation];
-[FBScene succinctDescription];
-[FBScene workspaceIdentifier];
-[FBScene identityToken];
-[FBScene addObserver:];
-[FBScene invalidate];
-[FBScene setDelegate:];
-[FBScene snapshotContext];
-[FBScene isValid];
-[FBScene conformsToExtension:];
-[FBScene delegate];
-[FBScene identity];
-[FBScene description];
-[FBScene specification];
-[FBScene updateSettingsWithBlock:];
-[FBScene clientSettings];
-[FBScene isActive];
-[FBScene activate:];
-[FBScene isEqual:];
-[FBScene sceneWillInvalidate:];
-[FBScene descriptionBuilderWithMultilinePrefix:];
-[FBScene updateSettings:];
-[FBScene setParentScene:];
-[FBScene activateWithTransitionContext:];
-[FBScene clientHandle];
-[FBScene componentForExtension:ofClass:];
-[FBScene configureParameters:];
-[FBScene contentState];
-[FBScene createSnapshotWithContext:];
-[FBScene executeWhenMutable:];
-[FBScene isLegacy];
-[FBScene layerManager];
-[FBScene parentScene];
-[FBScene prepareSnapshotWithConfigurator:];
-[FBScene removeExtension:];
-[FBScene removeExtensions:];
-[FBScene uiClientSettings];
-[FBScene uiSettings];
-[FBScene updateUISettingsWithTransitionBlock:];
-[FBScene createSnapshot];
-[FBScene prepareSnapshot];
-[FBScene sendInvocation:];
-[FBScene sendActions:toExtension:];
-[FBScene targetForInvocation:];
-[FBScene updateSettingsWithTransitionBlock:];
-[FBScene updateSettings:withTransitionContext:];
-[FBScene performUpdate:withCompletion:];
-[FBScene clientToken:didUpdateClientSettings:withDiff:transitionContext:];
-[FBScene _isInTransaction];
-[FBScene _transactionID];
-[FBScene activateWithTransitionContext:completion:];
-[FBScene clientToken:deactivateWithContext:];
-[FBScene clientToken:didInvalidateWithError:];
-[FBScene clientToken:didReceiveActions:forExtension:];
-[FBScene clientToken:handleInvocation:withReply:];
-[FBScene deactivateWithTransitionContext:];
-[FBScene updateSettings:withTransitionContext:completion:];
-[FBScene updateUISettingsWithBlock:];
-[FBScene updateWhenMutable:];
```
