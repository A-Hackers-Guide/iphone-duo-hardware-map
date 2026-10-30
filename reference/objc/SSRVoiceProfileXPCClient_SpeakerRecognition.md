# `SSRVoiceProfileXPCClient`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<SSRVoiceProfileXPCClientDelegate>" _delegate;
@"NSObject<OS_xpc_object>" _xpcConnection;
```

## Properties

```
@property (T@"NSObject<OS_xpc_object>",&,N,V_xpcConnection) xpcConnection;
@property (T@"<SSRVoiceProfileXPCClientDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[SSRVoiceProfileXPCClient connect];
-[SSRVoiceProfileXPCClient init];
-[SSRVoiceProfileXPCClient setXpcConnection:];
-[SSRVoiceProfileXPCClient dealloc];
-[SSRVoiceProfileXPCClient xpcConnection];
-[SSRVoiceProfileXPCClient setDelegate:];
-[SSRVoiceProfileXPCClient delegate];
-[SSRVoiceProfileXPCClient _handleListenerDisconnectedError:];
-[SSRVoiceProfileXPCClient _handleListenerError:];
-[SSRVoiceProfileXPCClient _handleListenerEvent:];
-[SSRVoiceProfileXPCClient fetchEnrollmentStatusForSiriProfileId:forLanguageCode:completion:];
```
