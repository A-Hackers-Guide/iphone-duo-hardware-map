# `QSSMultiUserStreamingRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 11 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{MultiUserStreamingRequest=[1C]} _root;
```

## Properties

```
@property (Tq,R,N) content_type;
@property (T@"QSSMultiUserStartSpeechRequest",R,N) contentAsQSSMultiUserStartSpeechRequest;
@property (T@"QSSUpdateAudioInfo",R,N) contentAsQSSUpdateAudioInfo;
@property (T@"QSSSetRequestOrigin",R,N) contentAsQSSSetRequestOrigin;
@property (T@"QSSSetSpeechContext",R,N) contentAsQSSSetSpeechContext;
@property (T@"QSSSetSpeechProfile",R,N) contentAsQSSSetSpeechProfile;
@property (T@"QSSSetEndpointerState",R,N) contentAsQSSSetEndpointerState;
@property (T@"QSSAudioPacket",R,N) contentAsQSSAudioPacket;
@property (T@"QSSFinishAudio",R,N) contentAsQSSFinishAudio;
@property (T@"QSSResetServerEndpointer",R,N) contentAsQSSResetServerEndpointer;
@property (T@"QSSSetAlternateRecognitionSausage",R,N) contentAsQSSSetAlternateRecognitionSausage;
```

## Instance methods

```
-[QSSMultiUserStreamingRequest copyWithZone:];
-[QSSMultiUserStreamingRequest addObjectToBuffer:];
-[QSSMultiUserStreamingRequest content_type];
-[QSSMultiUserStreamingRequest flatbuffData];
-[QSSMultiUserStreamingRequest initAndVerifyWithFlatbuffData:];
-[QSSMultiUserStreamingRequest initWithFlatbuffData:];
-[QSSMultiUserStreamingRequest initWithFlatbuffData:root:];
-[QSSMultiUserStreamingRequest initWithFlatbuffData:root:verify:];
-[QSSMultiUserStreamingRequest contentAsQSSAudioPacket];
-[QSSMultiUserStreamingRequest contentAsQSSFinishAudio];
-[QSSMultiUserStreamingRequest contentAsQSSMultiUserStartSpeechRequest];
-[QSSMultiUserStreamingRequest contentAsQSSResetServerEndpointer];
-[QSSMultiUserStreamingRequest contentAsQSSSetAlternateRecognitionSausage];
-[QSSMultiUserStreamingRequest contentAsQSSSetEndpointerState];
-[QSSMultiUserStreamingRequest contentAsQSSSetRequestOrigin];
-[QSSMultiUserStreamingRequest contentAsQSSSetSpeechContext];
-[QSSMultiUserStreamingRequest contentAsQSSSetSpeechProfile];
-[QSSMultiUserStreamingRequest contentAsQSSUpdateAudioInfo];
```
