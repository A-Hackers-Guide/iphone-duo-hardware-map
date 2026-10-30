# `FBExtensionProcess`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBProcess`
- 4 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"FBSExtensionInfo" _extensionInfo;
i _hostPID;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _hostProcessLock;
@"FBProcess" _lock_hostProcess;
```

## Properties

```
@property (T@"FBSExtensionInfo",R,N,V_extensionInfo) extensionInfo;
@property (T@"FBProcess",R,N) hostProcess;
@property (Ti,R,N,V_hostPID) hostPID;
```

## Instance methods

```
-[FBExtensionProcess hostProcess];
-[FBExtensionProcess succinctDescriptionBuilder];
-[FBExtensionProcess hostPID];
-[FBExtensionProcess _finishInit];
-[FBExtensionProcess extensionInfo];
-[FBExtensionProcess isExtensionProcess];
```
