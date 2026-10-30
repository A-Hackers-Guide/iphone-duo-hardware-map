# `BKSHIDHapticFeedbackRequest`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `BSDescriptionStreamable`, `BSProtobufSerializable`, `NSCopying`, `NSMutableCopying`
- 5 instance variables, 9 properties, 15 instance methods, 4 class methods

## Instance variables

```
@"NSString" _pattern;
q _deviceType;
Q _senderID;
@"NSNumber" _powerSourceID;
Q _timestamp;
```

## Properties

```
@property (T@"NSString",R,C,N) pattern;
@property (Tq,R,N) deviceType;
@property (TQ,R,N) senderID;
@property (T@"NSNumber",R,N) powerSourceID;
@property (TQ,R,N) timestamp;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDHapticFeedbackRequest build:];
+[BKSHIDHapticFeedbackRequest supportsSecureCoding];
+[BKSHIDHapticFeedbackRequest protobufSchema];
+[BKSHIDHapticFeedbackRequest new];
```

## Instance methods

```
-[BKSHIDHapticFeedbackRequest pattern];
-[BKSHIDHapticFeedbackRequest mutableCopyWithZone:];
-[BKSHIDHapticFeedbackRequest initForProtobufDecoding];
-[BKSHIDHapticFeedbackRequest init];
-[BKSHIDHapticFeedbackRequest deviceType];
-[BKSHIDHapticFeedbackRequest appendDescriptionToFormatter:];
-[BKSHIDHapticFeedbackRequest timestamp];
-[BKSHIDHapticFeedbackRequest senderID];
-[BKSHIDHapticFeedbackRequest encodeWithCoder:];
-[BKSHIDHapticFeedbackRequest hash];
-[BKSHIDHapticFeedbackRequest description];
-[BKSHIDHapticFeedbackRequest initWithCoder:];
-[BKSHIDHapticFeedbackRequest copyWithZone:];
-[BKSHIDHapticFeedbackRequest isEqual:];
-[BKSHIDHapticFeedbackRequest powerSourceID];
```
