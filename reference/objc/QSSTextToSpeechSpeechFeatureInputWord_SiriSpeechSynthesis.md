# `QSSTextToSpeechSpeechFeatureInputWord`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechSpeechFeatureInputWord=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) word;
@property (T@"NSArray",R,N) phonemes;
```

## Instance methods

```
-[QSSTextToSpeechSpeechFeatureInputWord word];
-[QSSTextToSpeechSpeechFeatureInputWord copyWithZone:];
-[QSSTextToSpeechSpeechFeatureInputWord phonemes];
-[QSSTextToSpeechSpeechFeatureInputWord addObjectToBuffer:];
-[QSSTextToSpeechSpeechFeatureInputWord flatbuffData];
-[QSSTextToSpeechSpeechFeatureInputWord initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechSpeechFeatureInputWord initWithFlatbuffData:];
-[QSSTextToSpeechSpeechFeatureInputWord initWithFlatbuffData:root:];
-[QSSTextToSpeechSpeechFeatureInputWord initWithFlatbuffData:root:verify:];
```
