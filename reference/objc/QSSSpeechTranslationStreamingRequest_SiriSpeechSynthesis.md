# `QSSSpeechTranslationStreamingRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 9 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{SpeechTranslationStreamingRequest=[1C]} _root;
```

## Properties

```
@property (Tq,R,N) content_type;
@property (T@"QSSStartSpeechTranslationRequest",R,N) contentAsQSSStartSpeechTranslationRequest;
@property (T@"QSSLanguageDetected",R,N) contentAsQSSLanguageDetected;
@property (T@"QSSAudioPacket",R,N) contentAsQSSAudioPacket;
@property (T@"QSSSpeechTranslationAudioPacket",R,N) contentAsQSSSpeechTranslationAudioPacket;
@property (T@"QSSFinishAudio",R,N) contentAsQSSFinishAudio;
@property (T@"QSSSetEndpointerState",R,N) contentAsQSSSetEndpointerState;
@property (T@"QSSResetServerEndpointer",R,N) contentAsQSSResetServerEndpointer;
@property (T@"QSSStartSpeechTranslationLoggingRequest",R,N) contentAsQSSStartSpeechTranslationLoggingRequest;
```

## Instance methods

```
-[QSSSpeechTranslationStreamingRequest copyWithZone:];
-[QSSSpeechTranslationStreamingRequest addObjectToBuffer:];
-[QSSSpeechTranslationStreamingRequest content_type];
-[QSSSpeechTranslationStreamingRequest flatbuffData];
-[QSSSpeechTranslationStreamingRequest initAndVerifyWithFlatbuffData:];
-[QSSSpeechTranslationStreamingRequest initWithFlatbuffData:];
-[QSSSpeechTranslationStreamingRequest initWithFlatbuffData:root:];
-[QSSSpeechTranslationStreamingRequest initWithFlatbuffData:root:verify:];
-[QSSSpeechTranslationStreamingRequest contentAsQSSAudioPacket];
-[QSSSpeechTranslationStreamingRequest contentAsQSSFinishAudio];
-[QSSSpeechTranslationStreamingRequest contentAsQSSLanguageDetected];
-[QSSSpeechTranslationStreamingRequest contentAsQSSResetServerEndpointer];
-[QSSSpeechTranslationStreamingRequest contentAsQSSSetEndpointerState];
-[QSSSpeechTranslationStreamingRequest contentAsQSSSpeechTranslationAudioPacket];
-[QSSSpeechTranslationStreamingRequest contentAsQSSStartSpeechTranslationLoggingRequest];
-[QSSSpeechTranslationStreamingRequest contentAsQSSStartSpeechTranslationRequest];
```
