# `BKSHIDUISensorCharacteristics`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCSecureCoding`, `NSSecureCoding`, `BSDescriptionStreamable`, `BSProtobufSerializable`, `NSCopying`
- 2 instance variables, 6 properties, 15 instance methods, 4 class methods

## Instance variables

```
q _suggestedSystemApertureGracePeriodForScreenOff;
B _hasDiscreteProximitySensor;
```

## Properties

```
@property (TB,R,N) hasDiscreteProximitySensor;
@property (Tq,R,N) suggestedSystemApertureGracePeriodForScreenOff;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDUISensorCharacteristics supportsBSXPCSecureCoding];
+[BKSHIDUISensorCharacteristics supportsSecureCoding];
+[BKSHIDUISensorCharacteristics protobufSchema];
+[BKSHIDUISensorCharacteristics new];
```

## Instance methods

```
-[BKSHIDUISensorCharacteristics initForProtobufDecoding];
-[BKSHIDUISensorCharacteristics init];
-[BKSHIDUISensorCharacteristics appendDescriptionToFormatter:];
-[BKSHIDUISensorCharacteristics _init];
-[BKSHIDUISensorCharacteristics encodeWithCoder:];
-[BKSHIDUISensorCharacteristics hash];
-[BKSHIDUISensorCharacteristics description];
-[BKSHIDUISensorCharacteristics initWithCoder:];
-[BKSHIDUISensorCharacteristics encodeWithBSXPCCoder:];
-[BKSHIDUISensorCharacteristics initWithBSXPCCoder:];
-[BKSHIDUISensorCharacteristics copyWithZone:];
-[BKSHIDUISensorCharacteristics isEqual:];
-[BKSHIDUISensorCharacteristics mutableCopy];
-[BKSHIDUISensorCharacteristics hasDiscreteProximitySensor];
-[BKSHIDUISensorCharacteristics suggestedSystemApertureGracePeriodForScreenOff];
```
