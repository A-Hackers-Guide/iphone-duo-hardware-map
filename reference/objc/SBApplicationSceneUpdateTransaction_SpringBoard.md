# `SBApplicationSceneUpdateTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSynchronizedTransactionGroup`
- Protocols: `FBSceneObserver`, `FBProcessObserver`, `FBSceneManagerObserver`
- 17 instance variables, 11 properties, 39 instance methods, 0 class methods

## Instance variables

```
@"SBApplicationSceneEntity" _applicationSceneEntity;
@"SBApplicationSceneHandle" _sceneHandle;
@"LSApplicationIdentity" _applicationIdentity;
@"SBWorkspaceTransitionRequest" _request;
@"SBWorkspaceApplicationSceneTransitionContext" _transitionContext;
@"NSString" _sceneIdentifier;
@"FBSMutableSceneParameters" _sceneParameters;
@"FBProcess" _exitedProcess;
B _suspendedActivation;
B _shouldSendActivationResult;
B _announcesMoveToNewDisplayOnSceneCommit;
@"FBScene" _scene;
@"SBPreflightController" _preflightController;
B _requiresPreflight;
@"<SBApplicationSceneUpdateTransactionDelegate>" _delegate;
B _waitsForSceneCommits;
B _isInPreflight;
```

## Properties

```
@property (T@"SBApplicationSceneEntity",R,N,V_applicationSceneEntity) applicationSceneEntity;
@property (T@"NSString",R,N,V_sceneIdentifier) sceneIdentifier;
@property (T@"UIApplicationSceneSettings",R,N) sceneSettings;
@property (TB,N,V_shouldSendActivationResult) shouldSendActivationResult;
@property (TB,N,V_waitsForSceneCommits) waitsForSceneCommits;
@property (T@"FBApplicationProcess",R,N) process;
@property (TB,R,N,V_isInPreflight) isInPreflight;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBApplicationSceneUpdateTransaction sceneSettings];
-[SBApplicationSceneUpdateTransaction performSynchronizedCommit];
-[SBApplicationSceneUpdateTransaction _willBegin];
-[SBApplicationSceneUpdateTransaction _canBeInterrupted];
-[SBApplicationSceneUpdateTransaction _didComplete];
-[SBApplicationSceneUpdateTransaction _begin];
-[SBApplicationSceneUpdateTransaction scene:clientDidConnect:];
-[SBApplicationSceneUpdateTransaction _willFailWithReason:];
-[SBApplicationSceneUpdateTransaction _performSynchronizedCommit:];
-[SBApplicationSceneUpdateTransaction sceneDidInvalidate:withContext:];
-[SBApplicationSceneUpdateTransaction _addCATransactionSynchronizedActionToContext:];
-[SBApplicationSceneUpdateTransaction setShouldSendActivationResult:];
-[SBApplicationSceneUpdateTransaction _customizedDescriptionProperties];
-[SBApplicationSceneUpdateTransaction removeObserver:];
-[SBApplicationSceneUpdateTransaction _createSceneIfNecessary];
-[SBApplicationSceneUpdateTransaction applicationSceneEntity];
-[SBApplicationSceneUpdateTransaction sceneDidActivate:];
-[SBApplicationSceneUpdateTransaction initWithApplicationSceneEntity:transitionRequest:delegate:];
-[SBApplicationSceneUpdateTransaction process];
-[SBApplicationSceneUpdateTransaction _noteScene:didCommitSuccessfully:];
-[SBApplicationSceneUpdateTransaction _notifyObserversOfClientConnection:];
-[SBApplicationSceneUpdateTransaction addObserver:];
-[SBApplicationSceneUpdateTransaction sceneIdentifier];
-[SBApplicationSceneUpdateTransaction _createSceneAndRunPreflight];
-[SBApplicationSceneUpdateTransaction processDidExit:];
-[SBApplicationSceneUpdateTransaction setWaitsForSceneCommits:];
-[SBApplicationSceneUpdateTransaction _createUpdateTransactionForPreflightCompletion];
-[SBApplicationSceneUpdateTransaction _willInterruptWithReason:];
-[SBApplicationSceneUpdateTransaction _shouldRequirePreflightForRequest:];
-[SBApplicationSceneUpdateTransaction sceneManager:willRemoveScene:];
-[SBApplicationSceneUpdateTransaction _sendActivationResultWithError:];
-[SBApplicationSceneUpdateTransaction waitsForSceneCommits];
-[SBApplicationSceneUpdateTransaction _isScenePendingRemovalFromWorkspace];
-[SBApplicationSceneUpdateTransaction _kickOffSynchronizedCommit];
-[SBApplicationSceneUpdateTransaction _performCommit];
-[SBApplicationSceneUpdateTransaction isInPreflight];
-[SBApplicationSceneUpdateTransaction _sceneResizeLayoutDidFinish:];
-[SBApplicationSceneUpdateTransaction initWithApplicationSceneEntity:transitionRequest:];
-[SBApplicationSceneUpdateTransaction shouldSendActivationResult];
```
