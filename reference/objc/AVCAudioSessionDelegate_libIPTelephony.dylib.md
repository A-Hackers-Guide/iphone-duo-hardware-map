# `AVCAudioSessionDelegate`

- Image: [`/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`](../userland/System__Library__PrivateFrameworks__IPTelephony.framework__Support__libIPTelephony.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TAAudioStreamDelegate`
- 2 instance variables, 6 properties, 19 instance methods, 0 class methods

## Instance variables

```
{weak_ptr<AVCAudioSession>="__ptr_"^{AVCAudioSession}"__cntrl_"^{__shared_weak_count}} owner;
{shared_ptr<AVCRTPStackController>="__ptr_"^{AVCRTPStackController}"__cntrl_"^{__shared_weak_count}} stackController;
```

## Properties

```
@property (T{weak_ptr<AVCAudioSession>=^{AVCAudioSession}^{__shared_weak_count}},N,Vowner) owner;
@property (T{shared_ptr<AVCRTPStackController>=^{AVCRTPStackController}^{__shared_weak_count}},N,VstackController) stackController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVCAudioSessionDelegate owner];
-[AVCAudioSessionDelegate setOwner:];
-[AVCAudioSessionDelegate stackController];
-[AVCAudioSessionDelegate setStackController:];
-[AVCAudioSessionDelegate audioStream:didPause:error:];
-[AVCAudioSessionDelegate audioStream:didReceiveDTMFEventWithDigit:];
-[AVCAudioSessionDelegate audioStream:didReceiveRTCPPackets:];
-[AVCAudioSessionDelegate audioStream:didResume:error:];
-[AVCAudioSessionDelegate audioStream:didStart:error:];
-[AVCAudioSessionDelegate audioStream:updateInputFrequencyLevel:];
-[AVCAudioSessionDelegate audioStream:updateOutputFrequencyLevel:];
-[AVCAudioSessionDelegate audioStreamDidRTCPTimeOut:];
-[AVCAudioSessionDelegate audioStreamDidRTPTimeOut:];
-[AVCAudioSessionDelegate audioStreamDidRecoverFromRTCPTimeOut:];
-[AVCAudioSessionDelegate audioStreamDidServerDie:];
-[AVCAudioSessionDelegate audioStreamDidStop:];
-[AVCAudioSessionDelegate callAudioServiceDidCrash:];
-[AVCAudioSessionDelegate handleRTCPPacketWithBlock:];
-[AVCAudioSessionDelegate initWithOwner:andStackController:];
```
