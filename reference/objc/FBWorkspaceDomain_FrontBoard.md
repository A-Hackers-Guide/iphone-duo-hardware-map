# `FBWorkspaceDomain`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 24 instance variables, 0 properties, 3 instance methods, 3 class methods

## Instance variables

```
@"FBSWorkspaceCoupler" _coupler;
@"BSServiceDomainSpecification" _specification;
@"FBWorkspaceEndpointPromise" _endpointPromise;
@"<BSInvalidatable>" _lock_registration;
@"BSServiceConnectionListener" _lock_listener;
@"<BSInvalidatable>" _lock_activation;
@"<FBWorkspaceDomainConnectionDelegate>" _icdLock_indirectConnectionDelegate;
@"NSMutableSet" _icdLock_pendingIndirectConnectionBlocks;
@"NSDictionary" _preregisteredWorkspaces;
@"NSString" _defaultWorkspace;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _icdLock;
b2 _selfAssertRuntime;
B _usesDefaultShellEndpoint;
B _allowsTerminatingOnWatchdogViolations;
B _injectorEnabled;
B _assertsVisibility;
B _monitorAllSuspendableProcesses;
B _allowsDirectConnections;
B _defaultWorkspaceDisabled;
B _lock_injectEndpointToFBSWorkspace;
B _lock_invalidated;
@"NSString" _reconnectShmemIdentifier;
@"NSSet" _reconnectableWorkspaces;
```

## Class methods

```
+[FBWorkspaceDomain debugDescription];
+[FBWorkspaceDomain startWorkspaceDomainListener];
+[FBWorkspaceDomain backgroundUserInitiatedBootstrapAttributes];
```

## Instance methods

```
-[FBWorkspaceDomain init];
-[FBWorkspaceDomain dealloc];
-[FBWorkspaceDomain description];
```
