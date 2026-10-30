# `QSSTextToSpeechVoice`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechVoice=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) language;
@property (T@"NSString",R,N) gender;
@property (T@"NSString",R,N) name;
@property (T@"NSString",R,N) version;
@property (T@"NSString",R,N) quality;
@property (T@"NSString",R,N) type;
```

## Instance methods

```
-[QSSTextToSpeechVoice language];
-[QSSTextToSpeechVoice quality];
-[QSSTextToSpeechVoice version];
-[QSSTextToSpeechVoice type];
-[QSSTextToSpeechVoice copyWithZone:];
-[QSSTextToSpeechVoice name];
-[QSSTextToSpeechVoice gender];
-[QSSTextToSpeechVoice addObjectToBuffer:];
-[QSSTextToSpeechVoice flatbuffData];
-[QSSTextToSpeechVoice initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechVoice initWithFlatbuffData:];
-[QSSTextToSpeechVoice initWithFlatbuffData:root:];
-[QSSTextToSpeechVoice initWithFlatbuffData:root:verify:];
```
