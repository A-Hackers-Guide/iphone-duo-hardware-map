# `QSSTTSRequestFeatureFlags`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TTSRequestFeatureFlags=[1C]} _root;
```

## Properties

```
@property (TB,R,N) fe_feature;
@property (TB,R,N) fe_feature_only;
@property (TB,R,N) disable_prompts;
@property (TB,R,N) cache_only;
@property (Tq,R,N) phoneset_type;
```

## Instance methods

```
-[QSSTTSRequestFeatureFlags copyWithZone:];
-[QSSTTSRequestFeatureFlags fe_feature_only];
-[QSSTTSRequestFeatureFlags addObjectToBuffer:];
-[QSSTTSRequestFeatureFlags fe_feature];
-[QSSTTSRequestFeatureFlags flatbuffData];
-[QSSTTSRequestFeatureFlags initAndVerifyWithFlatbuffData:];
-[QSSTTSRequestFeatureFlags initWithFlatbuffData:];
-[QSSTTSRequestFeatureFlags initWithFlatbuffData:root:];
-[QSSTTSRequestFeatureFlags initWithFlatbuffData:root:verify:];
-[QSSTTSRequestFeatureFlags disable_prompts];
-[QSSTTSRequestFeatureFlags cache_only];
-[QSSTTSRequestFeatureFlags phoneset_type];
```
