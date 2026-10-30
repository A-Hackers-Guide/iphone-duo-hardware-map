# `QSSRecognitionChoice`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{RecognitionChoice=[1C]} _root;
```

## Properties

```
@property (T@"NSArray",R,N) alternative_index;
@property (Ti,R,N) confidence;
```

## Instance methods

```
-[QSSRecognitionChoice copyWithZone:];
-[QSSRecognitionChoice confidence];
-[QSSRecognitionChoice addObjectToBuffer:];
-[QSSRecognitionChoice flatbuffData];
-[QSSRecognitionChoice initAndVerifyWithFlatbuffData:];
-[QSSRecognitionChoice initWithFlatbuffData:];
-[QSSRecognitionChoice initWithFlatbuffData:root:];
-[QSSRecognitionChoice initWithFlatbuffData:root:verify:];
-[QSSRecognitionChoice alternative_index];
```
