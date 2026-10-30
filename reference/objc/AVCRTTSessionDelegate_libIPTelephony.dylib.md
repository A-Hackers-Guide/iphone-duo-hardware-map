# `AVCRTTSessionDelegate`

- Image: [`/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`](../userland/System__Library__PrivateFrameworks__IPTelephony.framework__Support__libIPTelephony.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TATextStreamDelegate`
- 2 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
{weak_ptr<AVCRTTSession>="__ptr_"^{AVCRTTSession}"__cntrl_"^{__shared_weak_count}} owner;
{shared_ptr<AVCRTPStackController>="__ptr_"^{AVCRTPStackController}"__cntrl_"^{__shared_weak_count}} stackController;
```

## Properties

```
@property (T{weak_ptr<AVCRTTSession>=^{AVCRTTSession}^{__shared_weak_count}},N,Vowner) owner;
@property (T{shared_ptr<AVCRTPStackController>=^{AVCRTPStackController}^{__shared_weak_count}},N,VstackController) stackController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVCRTTSessionDelegate owner];
-[AVCRTTSessionDelegate setOwner:];
-[AVCRTTSessionDelegate stackController];
-[AVCRTTSessionDelegate setStackController:];
-[AVCRTTSessionDelegate callAudioServiceDidCrash:];
-[AVCRTTSessionDelegate initWithOwner:andStackController:];
-[AVCRTTSessionDelegate textStream:didPause:error:];
-[AVCRTTSessionDelegate textStream:didReceiveRTCPPackets:];
-[AVCRTTSessionDelegate textStream:didResume:error:];
-[AVCRTTSessionDelegate textStream:didStart:error:];
-[AVCRTTSessionDelegate textStreamDidRTCPTimeOut:];
-[AVCRTTSessionDelegate textStreamDidRTPTimeOut:];
-[AVCRTTSessionDelegate textStreamDidServerDie:];
-[AVCRTTSessionDelegate textStreamDidStop:];
```
