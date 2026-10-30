# `QSSServiceDiscoveryRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{ServiceDiscoveryRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) session_id;
@property (T@"NSString",R,N) app_id;
@property (T@"NSString",R,N) zk_path;
```

## Instance methods

```
-[QSSServiceDiscoveryRequest copyWithZone:];
-[QSSServiceDiscoveryRequest addObjectToBuffer:];
-[QSSServiceDiscoveryRequest app_id];
-[QSSServiceDiscoveryRequest flatbuffData];
-[QSSServiceDiscoveryRequest initAndVerifyWithFlatbuffData:];
-[QSSServiceDiscoveryRequest initWithFlatbuffData:];
-[QSSServiceDiscoveryRequest initWithFlatbuffData:root:];
-[QSSServiceDiscoveryRequest initWithFlatbuffData:root:verify:];
-[QSSServiceDiscoveryRequest session_id];
-[QSSServiceDiscoveryRequest zk_path];
```
