# `FigCaptureClientApplicationStateMonitorClient`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 19 instance variables, 19 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"FigCaptureProcessHandle" _processHandle;
{?="val"[8I]} _auditToken;
i _pid;
@"NSString" _applicationID;
@"NSString" _mediaEnvironment;
@"NSString" _mediaEnvironmentBundleID;
@"NSObject<OS_tcc_identity>" _mediaEnvironmentTCCIdentity;
i _clientType;
B _isForThirdPartyTorch;
B _isSwiftPlaygroundsDevelopmentApp;
B _isSecureCaptureExtension;
B _hasBackgroundCameraAccess;
B _isXPCService;
i _xpcServiceRootHostPID;
@"NSString" _xpcServiceRootHostApplicationID;
i _pidToInheritAppStateFrom;
@"NSString" _applicationIDToInheritAppStateFrom;
@"NSArray" _avconferenceClientApplicationIDs;
@? _applicationAndLayoutStateHandler;
```

## Properties

```
@property (T@"FigCaptureProcessHandle",R,N,V_processHandle) processHandle;
@property (T{?=[8I]},R,N,V_auditToken) auditToken;
@property (Ti,R,N,V_pid) pid;
@property (T@"NSString",R,N,V_applicationID) applicationID;
@property (T@"NSString",R,N,V_mediaEnvironment) mediaEnvironment;
@property (T@"NSString",&,N,V_mediaEnvironmentBundleID) mediaEnvironmentBundleID;
@property (T@"NSObject<OS_tcc_identity>",&,N,V_mediaEnvironmentTCCIdentity) mediaEnvironmentTCCIdentity;
@property (Ti,R,N,V_clientType) clientType;
@property (TB,R,N,GisForThirdPartyTorch,V_isForThirdPartyTorch) forThirdPartyTorch;
@property (TB,R,N,GisSwiftPlaygroundsDevelopmentApp,V_isSwiftPlaygroundsDevelopmentApp) swiftPlaygroundsDevelopmentApp;
@property (TB,R,N,GisSecureCaptureExtension,V_isSecureCaptureExtension) secureCaptureExtension;
@property (TB,R,N,GhasBackgroundCameraAccess,V_hasBackgroundCameraAccess) backgroundCameraAccess;
@property (TB,R,N,GisXPCService,V_isXPCService) xpcService;
@property (Ti,R,N,V_xpcServiceRootHostPID) xpcServiceRootHostPID;
@property (T@"NSString",R,N,V_xpcServiceRootHostApplicationID) xpcServiceRootHostApplicationID;
@property (Ti,N,V_pidToInheritAppStateFrom) pidToInheritAppStateFrom;
@property (T@"NSString",&,N,V_applicationIDToInheritAppStateFrom) applicationIDToInheritAppStateFrom;
@property (T@"NSArray",R,N,V_avconferenceClientApplicationIDs) avconferenceClientApplicationIDs;
@property (T@?,R,N,V_applicationAndLayoutStateHandler) applicationAndLayoutStateHandler;
```

## Instance methods

```
-[FigCaptureClientApplicationStateMonitorClient clientType];
-[FigCaptureClientApplicationStateMonitorClient applicationID];
-[FigCaptureClientApplicationStateMonitorClient isXPCService];
-[FigCaptureClientApplicationStateMonitorClient isForThirdPartyTorch];
-[FigCaptureClientApplicationStateMonitorClient debugDescription];
-[FigCaptureClientApplicationStateMonitorClient setMediaEnvironmentTCCIdentity:];
-[FigCaptureClientApplicationStateMonitorClient xpcServiceRootHostPID];
-[FigCaptureClientApplicationStateMonitorClient xpcServiceRootHostApplicationID];
-[FigCaptureClientApplicationStateMonitorClient mediaEnvironmentTCCIdentity];
-[FigCaptureClientApplicationStateMonitorClient dealloc];
-[FigCaptureClientApplicationStateMonitorClient pidToInheritAppStateFrom];
-[FigCaptureClientApplicationStateMonitorClient mediaEnvironment];
-[FigCaptureClientApplicationStateMonitorClient mediaEnvironmentBundleID];
-[FigCaptureClientApplicationStateMonitorClient applicationIDToInheritAppStateFrom];
-[FigCaptureClientApplicationStateMonitorClient avconferenceClientApplicationIDs];
-[FigCaptureClientApplicationStateMonitorClient hasBackgroundCameraAccess];
-[FigCaptureClientApplicationStateMonitorClient invalidate];
-[FigCaptureClientApplicationStateMonitorClient pid];
-[FigCaptureClientApplicationStateMonitorClient isSwiftPlaygroundsDevelopmentApp];
-[FigCaptureClientApplicationStateMonitorClient setApplicationIDToInheritAppStateFrom:];
-[FigCaptureClientApplicationStateMonitorClient isSecureCaptureExtension];
-[FigCaptureClientApplicationStateMonitorClient processHandle];
-[FigCaptureClientApplicationStateMonitorClient description];
-[FigCaptureClientApplicationStateMonitorClient setPidToInheritAppStateFrom:];
-[FigCaptureClientApplicationStateMonitorClient auditToken];
-[FigCaptureClientApplicationStateMonitorClient initWithAuditToken:mediaEnvironment:forThirdPartyTorch:applicationAndLayoutStateHandler:];
-[FigCaptureClientApplicationStateMonitorClient setMediaEnvironmentBundleID:];
-[FigCaptureClientApplicationStateMonitorClient applicationAndLayoutStateHandler];
```
