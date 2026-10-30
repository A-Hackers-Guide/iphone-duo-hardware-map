# `BKSEventDeferringChainIdentity`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`, `NSSecureCoding`, `BSDescriptionStreamable`, `BSProtobufSerializable`
- 2 instance variables, 6 properties, 14 instance methods, 4 class methods

## Instance variables

```
@"BKSHIDEventDisplay" _display;
@"BKSHIDEventDeferringEnvironment" _environment;
```

## Properties

```
@property (T@"BKSHIDEventDisplay",R,N) display;
@property (T@"BKSHIDEventDeferringEnvironment",R,N) environment;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSEventDeferringChainIdentity build:];
+[BKSEventDeferringChainIdentity supportsSecureCoding];
+[BKSEventDeferringChainIdentity protobufSchema];
+[BKSEventDeferringChainIdentity new];
```

## Instance methods

```
-[BKSEventDeferringChainIdentity didFinishProtobufDecodingWithError:];
-[BKSEventDeferringChainIdentity display];
-[BKSEventDeferringChainIdentity mutableCopyWithZone:];
-[BKSEventDeferringChainIdentity initForProtobufDecoding];
-[BKSEventDeferringChainIdentity init];
-[BKSEventDeferringChainIdentity appendDescriptionToFormatter:];
-[BKSEventDeferringChainIdentity encodeWithCoder:];
-[BKSEventDeferringChainIdentity hash];
-[BKSEventDeferringChainIdentity description];
-[BKSEventDeferringChainIdentity initWithCoder:];
-[BKSEventDeferringChainIdentity copyWithZone:];
-[BKSEventDeferringChainIdentity isEqual:];
-[BKSEventDeferringChainIdentity environment];
-[BKSEventDeferringChainIdentity initWithDisplay:environment:];
```
