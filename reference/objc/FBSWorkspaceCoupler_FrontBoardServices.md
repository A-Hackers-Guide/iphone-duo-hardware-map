# `FBSWorkspaceCoupler`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 4 instance variables, 4 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"FBSWorkspace" _lock_workspace;
@"NSMutableArray" _lock_clientConnectionBlocks;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_invalidated;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSWorkspaceCoupler _sharedInstance];
```

## Instance methods

```
-[FBSWorkspaceCoupler init];
-[FBSWorkspaceCoupler dealloc];
-[FBSWorkspaceCoupler invalidate];
-[FBSWorkspaceCoupler _workspace];
-[FBSWorkspaceCoupler _enqueueClientConnectionBlock:];
-[FBSWorkspaceCoupler _isSharedInstance];
```
