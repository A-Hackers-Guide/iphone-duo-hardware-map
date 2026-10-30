# `SSRVoiceProfileXPCService`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SSRVoiceProfileXPCClientDelegate`
- 2 instance variables, 6 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"SSRVoiceProfileXPCClient" _xpcClient;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"SSRVoiceProfileXPCClient",&,N,V_xpcClient) xpcClient;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SSRVoiceProfileXPCService sharedService];
```

## Instance methods

```
-[SSRVoiceProfileXPCService xpcClient];
-[SSRVoiceProfileXPCService init];
-[SSRVoiceProfileXPCService queue];
-[SSRVoiceProfileXPCService setXpcClient:];
-[SSRVoiceProfileXPCService setQueue:];
-[SSRVoiceProfileXPCService _createXPCClientConnectionIfNeeded:];
-[SSRVoiceProfileXPCService _teardownXPCClientIfNeeded];
-[SSRVoiceProfileXPCService fetchEnrollmentStatusForSiriProfileId:forLanguageCode:completion:];
-[SSRVoiceProfileXPCService ssrVoiceProfileXPCClient:didDisconnect:];
```
