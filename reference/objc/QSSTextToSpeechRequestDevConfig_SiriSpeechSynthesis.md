# `QSSTextToSpeechRequestDevConfig`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechRequestDevConfig=[1C]} _root;
```

## Properties

```
@property (TB,R,N) return_log;
@property (T@"NSString",R,N) voice_asset_path;
@property (T@"NSString",R,N) resource_asset_path;
@property (TB,R,N) return_server_info;
```

## Instance methods

```
-[QSSTextToSpeechRequestDevConfig copyWithZone:];
-[QSSTextToSpeechRequestDevConfig addObjectToBuffer:];
-[QSSTextToSpeechRequestDevConfig flatbuffData];
-[QSSTextToSpeechRequestDevConfig initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechRequestDevConfig initWithFlatbuffData:];
-[QSSTextToSpeechRequestDevConfig initWithFlatbuffData:root:];
-[QSSTextToSpeechRequestDevConfig initWithFlatbuffData:root:verify:];
-[QSSTextToSpeechRequestDevConfig resource_asset_path];
-[QSSTextToSpeechRequestDevConfig return_log];
-[QSSTextToSpeechRequestDevConfig return_server_info];
-[QSSTextToSpeechRequestDevConfig voice_asset_path];
```
