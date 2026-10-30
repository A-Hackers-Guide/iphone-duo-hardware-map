# `SBInCallSceneUpdateWorkspaceTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBMainWorkspaceTransaction`
- 2 instance variables, 1 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"SBApplicationSceneEntity" _applicationSceneEntity;
@? _postSceneUpdateHandler;
```

## Properties

```
@property (T@?,C,N,V_postSceneUpdateHandler) postSceneUpdateHandler;
```

## Instance methods

```
-[SBInCallSceneUpdateWorkspaceTransaction _begin];
-[SBInCallSceneUpdateWorkspaceTransaction initWithApplicationSceneEntity:transitionRequest:];
-[SBInCallSceneUpdateWorkspaceTransaction postSceneUpdateHandler];
-[SBInCallSceneUpdateWorkspaceTransaction setPostSceneUpdateHandler:];
```
