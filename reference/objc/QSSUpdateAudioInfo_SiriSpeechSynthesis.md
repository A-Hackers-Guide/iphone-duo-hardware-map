# `QSSUpdateAudioInfo`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{UpdateAudioInfo=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) product_id;
@property (T@"NSString",R,N) vendor_id;
```

## Instance methods

```
-[QSSUpdateAudioInfo copyWithZone:];
-[QSSUpdateAudioInfo addObjectToBuffer:];
-[QSSUpdateAudioInfo flatbuffData];
-[QSSUpdateAudioInfo initAndVerifyWithFlatbuffData:];
-[QSSUpdateAudioInfo initWithFlatbuffData:];
-[QSSUpdateAudioInfo initWithFlatbuffData:root:];
-[QSSUpdateAudioInfo initWithFlatbuffData:root:verify:];
-[QSSUpdateAudioInfo product_id];
-[QSSUpdateAudioInfo vendor_id];
```
