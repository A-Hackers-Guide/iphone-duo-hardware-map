# `AUServiceAdapter`

- Image: [`/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/MobileAccessoryUpdater`](../userland/System__Library__PrivateFrameworks__MobileAccessoryUpdater.framework__MobileAccessoryUpdater.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AUServiceProtocol`, `FudPluginDelegate`
- 2 instance variables, 6 properties, 27 instance methods, 1 class methods

## Instance variables

```
@"<FudPlugin>" _updater;
@"NSXPCConnection" _activeConnection;
```

## Properties

```
@property (T@"<FudPlugin>",R,N,V_updater) updater;
@property (T@"NSXPCConnection",N,V_activeConnection) activeConnection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AUServiceAdapter sharedInstance];
```

## Instance methods

```
-[AUServiceAdapter updater];
-[AUServiceAdapter _init];
-[AUServiceAdapter activeConnection];
-[AUServiceAdapter setActiveConnection:];
-[AUServiceAdapter hasActiveConnection];
-[AUServiceAdapter progress:];
-[AUServiceAdapter accessoryDisconnected:];
-[AUServiceAdapter log:format:];
-[AUServiceAdapter findFirmwareWithOptions:remote:];
-[AUServiceAdapter applyFirmwareWithOptions:];
-[AUServiceAdapter bootstrapWithOptions:];
-[AUServiceAdapter deviceClassAttached:options:withReply:];
-[AUServiceAdapter didApply:info:error:];
-[AUServiceAdapter didBootstrap:info:error:];
-[AUServiceAdapter didDownload:info:error:];
-[AUServiceAdapter didFind:info:updateAvailable:needsDownload:error:];
-[AUServiceAdapter didFinish:info:error:];
-[AUServiceAdapter didPrepare:info:error:];
-[AUServiceAdapter downloadFirmwareWithOptions:];
-[AUServiceAdapter finishWithOptions:];
-[AUServiceAdapter issueNotification:];
-[AUServiceAdapter logv:format:arguments:];
-[AUServiceAdapter personalizationRequest:];
-[AUServiceAdapter personalizationResponse:response:status:];
-[AUServiceAdapter prepareFirmwareWithOptions:];
-[AUServiceAdapter queryDeviceList:];
-[AUServiceAdapter reportAnalytics:info:];
```
