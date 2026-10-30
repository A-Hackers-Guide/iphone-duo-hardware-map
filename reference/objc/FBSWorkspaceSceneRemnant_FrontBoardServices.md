# `FBSWorkspaceSceneRemnant`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCSecureCoding`
- 2 instance variables, 6 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"FBSSceneIdentity" _identity;
@"FBSSceneParameters" _parameters;
```

## Properties

```
@property (T@"FBSSceneIdentity",R,C,N,V_identity) identity;
@property (T@"FBSSceneParameters",R,C,N,V_parameters) parameters;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSWorkspaceSceneRemnant supportsBSXPCSecureCoding];
```

## Instance methods

```
-[FBSWorkspaceSceneRemnant parameters];
-[FBSWorkspaceSceneRemnant init];
-[FBSWorkspaceSceneRemnant identity];
-[FBSWorkspaceSceneRemnant encodeWithBSXPCCoder:];
-[FBSWorkspaceSceneRemnant initWithBSXPCCoder:];
-[FBSWorkspaceSceneRemnant _initWithIdentity:parameters:];
```
