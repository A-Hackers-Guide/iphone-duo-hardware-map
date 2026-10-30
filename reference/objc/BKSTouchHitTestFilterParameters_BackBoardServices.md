# `BKSTouchHitTestFilterParameters`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSProtobufSerializable`, `NSSecureCoding`, `NSCopying`, `NSMutableCopying`, `BSDescriptionStreaming`
- 3 instance variables, 7 properties, 13 instance methods, 4 class methods

## Instance variables

```
@"NSArray" _senderDescriptors;
@"NSArray" _contextIDs;
Q _hitTestStimulus;
```

## Properties

```
@property (T@"NSArray",R,C,N) senderDescriptors;
@property (T@"NSArray",R,C,N) contextIDs;
@property (TQ,R,N) hitTestStimulus;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSTouchHitTestFilterParameters build:];
+[BKSTouchHitTestFilterParameters supportsSecureCoding];
+[BKSTouchHitTestFilterParameters protobufSchema];
+[BKSTouchHitTestFilterParameters new];
```

## Instance methods

```
-[BKSTouchHitTestFilterParameters mutableCopyWithZone:];
-[BKSTouchHitTestFilterParameters initForProtobufDecoding];
-[BKSTouchHitTestFilterParameters init];
-[BKSTouchHitTestFilterParameters encodeWithCoder:];
-[BKSTouchHitTestFilterParameters hash];
-[BKSTouchHitTestFilterParameters description];
-[BKSTouchHitTestFilterParameters initWithCoder:];
-[BKSTouchHitTestFilterParameters appendDescriptionToStream:];
-[BKSTouchHitTestFilterParameters copyWithZone:];
-[BKSTouchHitTestFilterParameters isEqual:];
-[BKSTouchHitTestFilterParameters hitTestStimulus];
-[BKSTouchHitTestFilterParameters contextIDs];
-[BKSTouchHitTestFilterParameters senderDescriptors];
```
