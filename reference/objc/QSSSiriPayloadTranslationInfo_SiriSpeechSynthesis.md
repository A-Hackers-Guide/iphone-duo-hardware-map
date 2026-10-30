# `QSSSiriPayloadTranslationInfo`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{SiriPayloadTranslationInfo=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) pre_itn_payload;
@property (T@"NSString",R,N) post_itn_payload;
@property (T@"QSSRecognitionSausage",R,N) pre_sausage_payload;
```

## Instance methods

```
-[QSSSiriPayloadTranslationInfo copyWithZone:];
-[QSSSiriPayloadTranslationInfo addObjectToBuffer:];
-[QSSSiriPayloadTranslationInfo flatbuffData];
-[QSSSiriPayloadTranslationInfo initAndVerifyWithFlatbuffData:];
-[QSSSiriPayloadTranslationInfo initWithFlatbuffData:];
-[QSSSiriPayloadTranslationInfo initWithFlatbuffData:root:];
-[QSSSiriPayloadTranslationInfo initWithFlatbuffData:root:verify:];
-[QSSSiriPayloadTranslationInfo pre_itn_payload];
-[QSSSiriPayloadTranslationInfo post_itn_payload];
-[QSSSiriPayloadTranslationInfo pre_sausage_payload];
```
