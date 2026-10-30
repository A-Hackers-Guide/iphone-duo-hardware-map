# `FBSWorkspaceSceneRequestOptions`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCSecureCoding`
- 8 instance variables, 12 properties, 18 instance methods, 1 class methods

## Instance variables

```
B _clientFuture;
@"NSString" _identifier;
@"NSString" _workspaceIdentifier;
@"FBSSceneClientIdentity" _clientIdentity;
@"FBSSceneSpecification" _specification;
@"FBSSceneClientSettings" _initialClientSettings;
@"FBSSceneTransitionContext" _transitionContext;
@"FBSSceneSettings" _initialSettings;
```

## Properties

```
@property (TB,N,GisClientFuture,V_clientFuture) clientFuture;
@property (T@"NSString",C,N,V_workspaceIdentifier) workspaceIdentifier;
@property (T@"FBSSceneClientIdentity",C,N,V_clientIdentity) clientIdentity;
@property (T@"FBSSceneSettings",&,N,V_initialSettings) initialSettings;
@property (T@"FBSSceneTransitionContext",&,N,V_transitionContext) transitionContext;
@property (T@"NSString",C,N,V_identifier) identifier;
@property (T@"FBSSceneSpecification",C,N,V_specification) specification;
@property (T@"FBSSceneClientSettings",C,N,V_initialClientSettings) initialClientSettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSWorkspaceSceneRequestOptions supportsBSXPCSecureCoding];
```

## Instance methods

```
-[FBSWorkspaceSceneRequestOptions isClientFuture];
-[FBSWorkspaceSceneRequestOptions identifier];
-[FBSWorkspaceSceneRequestOptions transitionContext];
-[FBSWorkspaceSceneRequestOptions setTransitionContext:];
-[FBSWorkspaceSceneRequestOptions setClientFuture:];
-[FBSWorkspaceSceneRequestOptions initialSettings];
-[FBSWorkspaceSceneRequestOptions setInitialClientSettings:];
-[FBSWorkspaceSceneRequestOptions setClientIdentity:];
-[FBSWorkspaceSceneRequestOptions setSpecification:];
-[FBSWorkspaceSceneRequestOptions workspaceIdentifier];
-[FBSWorkspaceSceneRequestOptions setIdentifier:];
-[FBSWorkspaceSceneRequestOptions initialClientSettings];
-[FBSWorkspaceSceneRequestOptions setInitialSettings:];
-[FBSWorkspaceSceneRequestOptions specification];
-[FBSWorkspaceSceneRequestOptions encodeWithBSXPCCoder:];
-[FBSWorkspaceSceneRequestOptions setWorkspaceIdentifier:];
-[FBSWorkspaceSceneRequestOptions initWithBSXPCCoder:];
-[FBSWorkspaceSceneRequestOptions clientIdentity];
```
