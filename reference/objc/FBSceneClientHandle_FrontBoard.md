# `FBSceneClientHandle`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 4 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"FBSSceneClientIdentity" _identity;
@"FBProcess" _legacyProcess;
```

## Properties

```
@property (T@"FBProcess",R,N,V_legacyProcess) legacyProcess;
@property (T@"FBSSceneClientIdentity",R,N,V_identity) identity;
@property (T@"RBSProcessHandle",R,N) processHandle;
@property (T@"NSString",R,N) bundleIdentifier;
```

## Class methods

```
+[FBSceneClientHandle handleForScene:clientProcess:];
```

## Instance methods

```
-[FBSceneClientHandle bundleIdentifier];
-[FBSceneClientHandle legacyProcess];
-[FBSceneClientHandle processHandle];
-[FBSceneClientHandle identity];
-[FBSceneClientHandle description];
```
