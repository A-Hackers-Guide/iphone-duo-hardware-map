# `QSSMutableErrorBlamerRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSErrorBlamerRequest`
- 0 instance variables, 10 properties, 22 instance methods, 0 class methods

## Properties

```
@property (T@"QSSStartSpeechRequest",C,N) start_speech_request;
@property (T@"NSArray",C,N) contextual_text;
@property (T@"NSString",C,N) left_context;
@property (T@"NSString",C,N) right_context;
@property (T@"QSSUserLanguageProfile",C,N) user_language_profile;
@property (T@"QSSUserAcousticProfile",C,N) user_acoustic_profile;
@property (Td,N) latitude;
@property (Td,N) longitude;
@property (T@"NSArray",C,N) audio_packets;
@property (T@"NSString",C,N) ref_transcript;
```

## Instance methods

```
-[QSSMutableErrorBlamerRequest init];
-[QSSMutableErrorBlamerRequest setLatitude:];
-[QSSMutableErrorBlamerRequest latitude];
-[QSSMutableErrorBlamerRequest longitude];
-[QSSMutableErrorBlamerRequest setLongitude:];
-[QSSMutableErrorBlamerRequest copyWithZone:];
-[QSSMutableErrorBlamerRequest contextual_text];
-[QSSMutableErrorBlamerRequest audio_packets];
-[QSSMutableErrorBlamerRequest left_context];
-[QSSMutableErrorBlamerRequest ref_transcript];
-[QSSMutableErrorBlamerRequest right_context];
-[QSSMutableErrorBlamerRequest setAudio_packets:];
-[QSSMutableErrorBlamerRequest setContextual_text:];
-[QSSMutableErrorBlamerRequest setLeft_context:];
-[QSSMutableErrorBlamerRequest setRef_transcript:];
-[QSSMutableErrorBlamerRequest setRight_context:];
-[QSSMutableErrorBlamerRequest setStart_speech_request:];
-[QSSMutableErrorBlamerRequest setUser_acoustic_profile:];
-[QSSMutableErrorBlamerRequest setUser_language_profile:];
-[QSSMutableErrorBlamerRequest start_speech_request];
-[QSSMutableErrorBlamerRequest user_acoustic_profile];
-[QSSMutableErrorBlamerRequest user_language_profile];
```
