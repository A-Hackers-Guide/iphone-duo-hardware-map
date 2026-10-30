# `QSSServiceDiscoveryResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{ServiceDiscoveryResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) session_id;
@property (Ti,R,N) error_code;
@property (T@"NSString",R,N) error_str;
@property (T@"NSArray",R,N) zk_node;
```

## Instance methods

```
-[QSSServiceDiscoveryResponse copyWithZone:];
-[QSSServiceDiscoveryResponse addObjectToBuffer:];
-[QSSServiceDiscoveryResponse error_code];
-[QSSServiceDiscoveryResponse error_str];
-[QSSServiceDiscoveryResponse flatbuffData];
-[QSSServiceDiscoveryResponse initAndVerifyWithFlatbuffData:];
-[QSSServiceDiscoveryResponse initWithFlatbuffData:];
-[QSSServiceDiscoveryResponse initWithFlatbuffData:root:];
-[QSSServiceDiscoveryResponse initWithFlatbuffData:root:verify:];
-[QSSServiceDiscoveryResponse session_id];
-[QSSServiceDiscoveryResponse zk_node];
```
