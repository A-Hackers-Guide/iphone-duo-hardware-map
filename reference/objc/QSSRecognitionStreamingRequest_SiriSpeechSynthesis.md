# `QSSRecognitionStreamingRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 12 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{RecognitionStreamingRequest=[1C]} _root;
```

## Properties

```
@property (Tq,R,N) content_type;
@property (T@"QSSStartSpeechRequest",R,N) contentAsQSSStartSpeechRequest;
@property (T@"QSSUpdateAudioInfo",R,N) contentAsQSSUpdateAudioInfo;
@property (T@"QSSSetRequestOrigin",R,N) contentAsQSSSetRequestOrigin;
@property (T@"QSSSetSpeechContext",R,N) contentAsQSSSetSpeechContext;
@property (T@"QSSSetSpeechProfile",R,N) contentAsQSSSetSpeechProfile;
@property (T@"QSSSetEndpointerState",R,N) contentAsQSSSetEndpointerState;
@property (T@"QSSAudioPacket",R,N) contentAsQSSAudioPacket;
@property (T@"QSSFinishAudio",R,N) contentAsQSSFinishAudio;
@property (T@"QSSResetServerEndpointer",R,N) contentAsQSSResetServerEndpointer;
@property (T@"QSSCheckForSpeechRequest",R,N) contentAsQSSCheckForSpeechRequest;
@property (T@"QSSSetAlternateRecognitionSausage",R,N) contentAsQSSSetAlternateRecognitionSausage;
```

## Instance methods

```
-[QSSRecognitionStreamingRequest copyWithZone:];
-[QSSRecognitionStreamingRequest addObjectToBuffer:];
-[QSSRecognitionStreamingRequest content_type];
-[QSSRecognitionStreamingRequest flatbuffData];
-[QSSRecognitionStreamingRequest initAndVerifyWithFlatbuffData:];
-[QSSRecognitionStreamingRequest initWithFlatbuffData:];
-[QSSRecognitionStreamingRequest initWithFlatbuffData:root:];
-[QSSRecognitionStreamingRequest initWithFlatbuffData:root:verify:];
-[QSSRecognitionStreamingRequest contentAsQSSAudioPacket];
-[QSSRecognitionStreamingRequest contentAsQSSCheckForSpeechRequest];
-[QSSRecognitionStreamingRequest contentAsQSSFinishAudio];
-[QSSRecognitionStreamingRequest contentAsQSSResetServerEndpointer];
-[QSSRecognitionStreamingRequest contentAsQSSSetAlternateRecognitionSausage];
-[QSSRecognitionStreamingRequest contentAsQSSSetEndpointerState];
-[QSSRecognitionStreamingRequest contentAsQSSSetRequestOrigin];
-[QSSRecognitionStreamingRequest contentAsQSSSetSpeechContext];
-[QSSRecognitionStreamingRequest contentAsQSSSetSpeechProfile];
-[QSSRecognitionStreamingRequest contentAsQSSStartSpeechRequest];
-[QSSRecognitionStreamingRequest contentAsQSSUpdateAudioInfo];
```
