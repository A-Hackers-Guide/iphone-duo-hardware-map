# `QSSSetRequestOrigin`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{SetRequestOrigin=[1C]} _root;
```

## Properties

```
@property (Td,R,N) latitude;
@property (Td,R,N) longitude;
@property (TB,R,N) enable_geo_location_features;
```

## Instance methods

```
-[QSSSetRequestOrigin latitude];
-[QSSSetRequestOrigin longitude];
-[QSSSetRequestOrigin copyWithZone:];
-[QSSSetRequestOrigin addObjectToBuffer:];
-[QSSSetRequestOrigin flatbuffData];
-[QSSSetRequestOrigin initAndVerifyWithFlatbuffData:];
-[QSSSetRequestOrigin initWithFlatbuffData:];
-[QSSSetRequestOrigin initWithFlatbuffData:root:];
-[QSSSetRequestOrigin initWithFlatbuffData:root:verify:];
-[QSSSetRequestOrigin enable_geo_location_features];
```
