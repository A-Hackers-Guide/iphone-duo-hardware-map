# `QSSSpeechTranslationServerEndpointFeatures`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{SpeechTranslationServerEndpointFeatures=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) conversation_id;
@property (T@"NSString",R,N) request_id;
@property (T@"NSString",R,N) source_locale;
@property (T@"QSSServerEndpointFeatures",R,N) server_endpoint_features;
```

## Instance methods

```
-[QSSSpeechTranslationServerEndpointFeatures copyWithZone:];
-[QSSSpeechTranslationServerEndpointFeatures addObjectToBuffer:];
-[QSSSpeechTranslationServerEndpointFeatures flatbuffData];
-[QSSSpeechTranslationServerEndpointFeatures initAndVerifyWithFlatbuffData:];
-[QSSSpeechTranslationServerEndpointFeatures initWithFlatbuffData:];
-[QSSSpeechTranslationServerEndpointFeatures initWithFlatbuffData:root:];
-[QSSSpeechTranslationServerEndpointFeatures initWithFlatbuffData:root:verify:];
-[QSSSpeechTranslationServerEndpointFeatures conversation_id];
-[QSSSpeechTranslationServerEndpointFeatures request_id];
-[QSSSpeechTranslationServerEndpointFeatures server_endpoint_features];
-[QSSSpeechTranslationServerEndpointFeatures source_locale];
```
