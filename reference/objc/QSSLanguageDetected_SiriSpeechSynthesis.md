# `QSSLanguageDetected`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{LanguageDetected=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) detected_locale;
@property (T@"NSArray",R,N) predictions;
```

## Instance methods

```
-[QSSLanguageDetected predictions];
-[QSSLanguageDetected copyWithZone:];
-[QSSLanguageDetected addObjectToBuffer:];
-[QSSLanguageDetected flatbuffData];
-[QSSLanguageDetected initAndVerifyWithFlatbuffData:];
-[QSSLanguageDetected initWithFlatbuffData:];
-[QSSLanguageDetected initWithFlatbuffData:root:];
-[QSSLanguageDetected initWithFlatbuffData:root:verify:];
-[QSSLanguageDetected detected_locale];
```
