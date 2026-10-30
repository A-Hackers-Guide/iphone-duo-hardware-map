# `FBSWorkspaceService`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"<FBSWorkspaceServiceTarget>" _target;
@"NSString" _identifier;
```

## Properties

```
@property (T@"NSString",R,C,N,V_identifier) identifier;
```

## Class methods

```
+[FBSWorkspaceService localService];
+[FBSWorkspaceService localServiceWithIdentifier:];
```

## Instance methods

```
-[FBSWorkspaceService createScene:completion:];
-[FBSWorkspaceService sendActions:];
-[FBSWorkspaceService sendActions:completion:];
-[FBSWorkspaceService identifier];
-[FBSWorkspaceService init];
-[FBSWorkspaceService _initWithTarget:identifier:];
-[FBSWorkspaceService description];
-[FBSWorkspaceService requestSceneWithOptions:completion:];
-[FBSWorkspaceService createScene:];
```
