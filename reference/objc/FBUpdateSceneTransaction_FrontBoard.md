# `FBUpdateSceneTransaction`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBTransaction`
- Protocols: `FBSceneObserver`, `FBSynchronizedTransaction`
- 12 instance variables, 13 properties, 37 instance methods, 0 class methods

## Instance variables

```
@"FBSceneManager" _sceneManager;
@"NSString" _sceneID;
@"FBSSceneDefinition" _definition;
@"FBSSceneParameters" _parameters;
@"FBSSceneTransitionContext" _transitionContext;
@"FBWaitForSceneDestructionTransaction" _destructionTransaction;
@"<FBSynchronizedTransactionDelegate>" _synchronizationDelegate;
Q _transactionID;
B _waitsForSceneCommit;
B _readyToCommit;
B _didCommit;
B _destroyed;
```

## Properties

```
@property (T@"FBScene",R,D,N) scene;
@property (T@"NSString",R,N,V_sceneID) sceneIdentifier;
@property (T@"FBSSceneSettings",R,D,N) settings;
@property (T@"FBSSceneSpecification",R,D,N) specification;
@property (T@"FBSSceneTransitionContext",R,N,V_transitionContext) transitionContext;
@property (TB,R,N,V_destroyed) destroyed;
@property (TB,N,V_waitsForSceneCommit) waitsForSceneCommit;
@property (T@"FBSSceneSettings",R,D,N) newSettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<FBSynchronizedTransactionDelegate>",W,N,V_synchronizationDelegate) synchronizationDelegate;
```

## Instance methods

```
-[FBUpdateSceneTransaction _childTransactionDidComplete:];
-[FBUpdateSceneTransaction isReadyForSynchronizedCommit];
-[FBUpdateSceneTransaction performSynchronizedCommit];
-[FBUpdateSceneTransaction _canBeInterrupted];
-[FBUpdateSceneTransaction _didComplete];
-[FBUpdateSceneTransaction _begin];
-[FBUpdateSceneTransaction setSynchronizationDelegate:];
-[FBUpdateSceneTransaction synchronizationDelegate];
-[FBUpdateSceneTransaction _customizedDescriptionProperties];
-[FBUpdateSceneTransaction transitionContext];
-[FBUpdateSceneTransaction removeObserver:];
-[FBUpdateSceneTransaction settings];
-[FBUpdateSceneTransaction add:];
-[FBUpdateSceneTransaction remove:];
-[FBUpdateSceneTransaction dealloc];
-[FBUpdateSceneTransaction sceneDidInvalidate:];
-[FBUpdateSceneTransaction addObserver:];
-[FBUpdateSceneTransaction sceneIdentifier];
-[FBUpdateSceneTransaction scene];
-[FBUpdateSceneTransaction specification];
-[FBUpdateSceneTransaction _performCommit];
-[FBUpdateSceneTransaction _noteDidCommit:];
-[FBUpdateSceneTransaction _noteWillCommit];
-[FBUpdateSceneTransaction _noteWillUpdate];
-[FBUpdateSceneTransaction _commitSceneOrWait];
-[FBUpdateSceneTransaction _commitSceneUpdate:];
-[FBUpdateSceneTransaction _createScene];
-[FBUpdateSceneTransaction _initWithSceneDefinition:parameters:transitionContext:];
-[FBUpdateSceneTransaction _noteDidCreate];
-[FBUpdateSceneTransaction _updateScene];
-[FBUpdateSceneTransaction destroyed];
-[FBUpdateSceneTransaction initWithSceneDefinition:parameters:transitionContext:];
-[FBUpdateSceneTransaction initWithSceneIdentifier:process:parameters:transitionContext:];
-[FBUpdateSceneTransaction initWithSceneToUpdate:newSettings:transitionContext:];
-[FBUpdateSceneTransaction newSettings];
-[FBUpdateSceneTransaction setWaitsForSceneCommit:];
-[FBUpdateSceneTransaction waitsForSceneCommit];
```
