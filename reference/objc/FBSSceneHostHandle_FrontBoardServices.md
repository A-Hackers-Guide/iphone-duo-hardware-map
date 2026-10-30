# `FBSSceneHostHandle`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 3 instance methods, 2 class methods

## Instance variables

```
B _local;
@"BSAuditToken" _auditToken;
```

## Properties

```
@property (TB,R,N,GisLocal,V_local) local;
@property (T@"BSAuditToken",R,N,V_auditToken) auditToken;
```

## Class methods

```
+[FBSSceneHostHandle handleWithAuditToken:];
+[FBSSceneHostHandle localHandle];
```

## Instance methods

```
-[FBSSceneHostHandle isLocal];
-[FBSSceneHostHandle description];
-[FBSSceneHostHandle auditToken];
```
