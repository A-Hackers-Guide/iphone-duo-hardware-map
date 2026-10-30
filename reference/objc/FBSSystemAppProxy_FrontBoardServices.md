# `FBSSystemAppProxy`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSServiceFacilityClient`
- 3 instance variables, 0 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"BSServiceConnectionEndpoint" _endpoint;
Q _checkoutCount;
@"BSProcessHandle" _processHandle;
```

## Class methods

```
+[FBSSystemAppProxy checkoutProxyWithEndpoint:];
```

## Instance methods

```
-[FBSSystemAppProxy terminateApplication:forReason:andReport:withDescription:completion:];
-[FBSSystemAppProxy checkin];
-[FBSSystemAppProxy clientCallbackQueue];
-[FBSSystemAppProxy setKeyboardFocusApplication:deferringToken:completion:];
-[FBSSystemAppProxy systemApplicationBundleIdentifier];
-[FBSSystemAppProxy handleMessage:withType:];
-[FBSSystemAppProxy _handleTerminationReply:targetDescription:withCompletion:];
-[FBSSystemAppProxy isPasscodeLockedOrBlocked];
-[FBSSystemAppProxy shutdownWithOptions:];
-[FBSSystemAppProxy fireCompletion:error:];
-[FBSSystemAppProxy sendActions:withResult:];
-[FBSSystemAppProxy terminateApplicationGroup:forReason:andReport:withDescription:completion:];
-[FBSSystemAppProxy fireCompletion:openAppErrorCode:];
-[FBSSystemAppProxy _sendMessageType:withMessage:withReplyHandler:waitForReply:];
-[FBSSystemAppProxy _handleConnect:];
-[FBSSystemAppProxy processHandleForBundleID:];
```
