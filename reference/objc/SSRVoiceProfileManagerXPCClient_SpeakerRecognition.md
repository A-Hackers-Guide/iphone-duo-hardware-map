# `SSRVoiceProfileManagerXPCClient`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
```

## Class methods

```
+[SSRVoiceProfileManagerXPCClient sharedClient];
+[SSRVoiceProfileManagerXPCClient createVoiceProfileManagerXPCConnection];
```

## Instance methods

```
-[SSRVoiceProfileManagerXPCClient init];
-[SSRVoiceProfileManagerXPCClient queue];
-[SSRVoiceProfileManagerXPCClient setQueue:];
-[SSRVoiceProfileManagerXPCClient importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:];
-[SSRVoiceProfileManagerXPCClient markSATEnrollmentSuccessForVoiceProfile:completion:];
```
