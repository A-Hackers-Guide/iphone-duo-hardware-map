# `FBWorkspaceEventDispatcher`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"FBWorkspaceDomain" _domain;
@"FBWorkspaceConnectionsStateStore" _store;
@"NSDictionary" _preregisteredWorkspaces;
@"NSMutableDictionary" _lock_sourcesByPidNumber;
@"NSMapTable" _lock_targetsByIdentifier;
@"NSCountedSet" _main_incompleteTargetRegistrations;
@"NSMutableDictionary" _lock_restartAssertionsByPidNumber;
@"FBMutableWorkspaceConnectionsState" _lock_mutableState;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Instance methods

```
-[FBWorkspaceEventDispatcher init];
-[FBWorkspaceEventDispatcher dealloc];
```
