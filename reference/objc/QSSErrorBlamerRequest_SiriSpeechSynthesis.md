# `QSSErrorBlamerRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 10 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{ErrorBlamerRequest=[1C]} _root;
```

## Properties

```
@property (T@"QSSStartSpeechRequest",R,N) start_speech_request;
@property (T@"NSArray",R,N) contextual_text;
@property (T@"NSString",R,N) left_context;
@property (T@"NSString",R,N) right_context;
@property (T@"QSSUserLanguageProfile",R,N) user_language_profile;
@property (T@"QSSUserAcousticProfile",R,N) user_acoustic_profile;
@property (Td,R,N) latitude;
@property (Td,R,N) longitude;
@property (T@"NSArray",R,N) audio_packets;
@property (T@"NSString",R,N) ref_transcript;
```

## Instance methods

```
-[QSSErrorBlamerRequest latitude];
-[QSSErrorBlamerRequest longitude];
-[QSSErrorBlamerRequest copyWithZone:];
-[QSSErrorBlamerRequest addObjectToBuffer:];
-[QSSErrorBlamerRequest flatbuffData];
-[QSSErrorBlamerRequest initAndVerifyWithFlatbuffData:];
-[QSSErrorBlamerRequest initWithFlatbuffData:];
-[QSSErrorBlamerRequest initWithFlatbuffData:root:];
-[QSSErrorBlamerRequest initWithFlatbuffData:root:verify:];
-[QSSErrorBlamerRequest contextual_text];
-[QSSErrorBlamerRequest audio_packets];
-[QSSErrorBlamerRequest left_context];
-[QSSErrorBlamerRequest ref_transcript];
-[QSSErrorBlamerRequest right_context];
-[QSSErrorBlamerRequest start_speech_request];
-[QSSErrorBlamerRequest user_acoustic_profile];
-[QSSErrorBlamerRequest user_language_profile];
```
