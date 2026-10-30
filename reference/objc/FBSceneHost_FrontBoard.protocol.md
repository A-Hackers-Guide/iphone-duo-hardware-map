# `FBSceneHost` (protocol)

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"<FBSProcess>",R,C,N) hostProcess;
@property (T@"FBSSceneIdentityToken",R,C,N) identityToken;
@property (T@"FBSSceneDefinition",R,C,N) definition;
@property (T@"FBSSceneSpecification",R,C,N) specification;
```

## Instance methods

```
-[FBSceneHost definition];
-[FBSceneHost hostProcess];
-[FBSceneHost identityToken];
-[FBSceneHost specification];
-[FBSceneHost clientToken:didUpdateClientSettings:withDiff:transitionContext:];
-[FBSceneHost clientToken:deactivateWithContext:];
-[FBSceneHost clientToken:didInvalidateWithError:];
-[FBSceneHost clientToken:didReceiveActions:forExtension:];
-[FBSceneHost clientToken:handleInvocation:withReply:];
```
