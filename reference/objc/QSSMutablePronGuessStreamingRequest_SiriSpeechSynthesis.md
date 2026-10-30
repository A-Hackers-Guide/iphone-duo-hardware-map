# `QSSMutablePronGuessStreamingRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSPronGuessStreamingRequest`
- 0 instance variables, 5 properties, 12 instance methods, 0 class methods

## Properties

```
@property (Tq,N) content_type;
@property (T@"QSSStartPronGuessRequest",C,N) contentAsQSSStartPronGuessRequest;
@property (T@"QSSAudioPacket",C,N) contentAsQSSAudioPacket;
@property (T@"QSSFinishAudio",C,N) contentAsQSSFinishAudio;
@property (T@"QSSCancelRequest",C,N) contentAsQSSCancelRequest;
```

## Instance methods

```
-[QSSMutablePronGuessStreamingRequest init];
-[QSSMutablePronGuessStreamingRequest copyWithZone:];
-[QSSMutablePronGuessStreamingRequest content_type];
-[QSSMutablePronGuessStreamingRequest setContent_type:];
-[QSSMutablePronGuessStreamingRequest contentAsQSSAudioPacket];
-[QSSMutablePronGuessStreamingRequest contentAsQSSCancelRequest];
-[QSSMutablePronGuessStreamingRequest contentAsQSSFinishAudio];
-[QSSMutablePronGuessStreamingRequest contentAsQSSStartPronGuessRequest];
-[QSSMutablePronGuessStreamingRequest setContentAsQSSAudioPacket:];
-[QSSMutablePronGuessStreamingRequest setContentAsQSSCancelRequest:];
-[QSSMutablePronGuessStreamingRequest setContentAsQSSFinishAudio:];
-[QSSMutablePronGuessStreamingRequest setContentAsQSSStartPronGuessRequest:];
```
