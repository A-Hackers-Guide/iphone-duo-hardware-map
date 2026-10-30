# `FBSceneRemnant`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 6 instance variables, 10 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"FBWorkspace" _workspace;
@"FBSSceneDefinition" _definition;
@"FBSSceneParameters" _parameters;
@"NSObject<OS_dispatch_queue>" _assertionQueue;
@"BSSimpleAssertion" _assertion;
@"BSAtomicSignal" _invalidated;
```

## Properties

```
@property (T@"FBWorkspace",R,W,N,V_workspace) _workspace;
@property (TB,R,N,G_hasBeenInvalidated) _invalidated;
@property (T@"FBSSceneClientSettings",R,C,N) _clientSettings;
@property (T@"BSSimpleAssertion",R,N,V_assertion) _assertion;
@property (T@"FBSSceneDefinition",R,C,N,V_definition) definition;
@property (T@"FBSSceneSettings",R,C,N) lastSettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSceneRemnant definition];
-[FBSceneRemnant init];
-[FBSceneRemnant dealloc];
-[FBSceneRemnant invalidate];
-[FBSceneRemnant _clientSettings];
-[FBSceneRemnant description];
-[FBSceneRemnant _workspace];
-[FBSceneRemnant lastSettings];
-[FBSceneRemnant _assertion];
-[FBSceneRemnant _hasBeenInvalidated];
-[FBSceneRemnant _initWithIdentity:client:workspace:parameters:assertionQueue:assertion:];
```
