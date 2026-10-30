# `FBSystemAppProxyServiceServer`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSServiceFacility`
- 1 instance variables, 0 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"FBServiceClientAuthenticator" _shutdownAuthenticator;
```

## Class methods

```
+[FBSystemAppProxyServiceServer sharedInstance];
+[FBSystemAppProxyServiceServer targetQueue];
```

## Instance methods

```
-[FBSystemAppProxyServiceServer _initWithQueue:];
-[FBSystemAppProxyServiceServer noteClientDidConnect:withMessage:];
-[FBSystemAppProxyServiceServer noteClientDidDisconnect:];
-[FBSystemAppProxyServiceServer noteDidReceiveMessage:withType:fromClient:];
-[FBSystemAppProxyServiceServer _handleActions:forClient:];
-[FBSystemAppProxyServiceServer _handleGetPasscodeLockedOrBlockedStatus:forClient:];
-[FBSystemAppProxyServiceServer _handleGetProcessHandle:forClient:];
-[FBSystemAppProxyServiceServer _handleShutdown:forClient:];
-[FBSystemAppProxyServiceServer _handleSystemApplicationBundleIdentifier:forClient:];
-[FBSystemAppProxyServiceServer _handleTerminateApplication:forClient:];
-[FBSystemAppProxyServiceServer _handleTerminateApplicationGroup:forClient:];
```
