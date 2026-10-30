# `QSSLmScorerRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{LmScorerRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) language;
@property (T@"NSString",R,N) task_name;
@property (T@"NSString",R,N) transcript;
```

## Instance methods

```
-[QSSLmScorerRequest language];
-[QSSLmScorerRequest copyWithZone:];
-[QSSLmScorerRequest addObjectToBuffer:];
-[QSSLmScorerRequest flatbuffData];
-[QSSLmScorerRequest initAndVerifyWithFlatbuffData:];
-[QSSLmScorerRequest initWithFlatbuffData:];
-[QSSLmScorerRequest initWithFlatbuffData:root:];
-[QSSLmScorerRequest initWithFlatbuffData:root:verify:];
-[QSSLmScorerRequest transcript];
-[QSSLmScorerRequest task_name];
```
