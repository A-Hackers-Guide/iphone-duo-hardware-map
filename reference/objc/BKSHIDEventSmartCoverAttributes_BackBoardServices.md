# `BKSHIDEventSmartCoverAttributes`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKSHIDEventBaseAttributes`
- 2 instance variables, 2 properties, 7 instance methods, 2 class methods

## Instance variables

```
i _smartCoverState;
i _wakeAnimationStyle;
```

## Properties

```
@property (Ti,N,V_smartCoverState) smartCoverState;
@property (Ti,N,V_wakeAnimationStyle) wakeAnimationStyle;
```

## Class methods

```
+[BKSHIDEventSmartCoverAttributes protobufSchema];
+[BKSHIDEventSmartCoverAttributes _eventAttributeType];
```

## Instance methods

```
-[BKSHIDEventSmartCoverAttributes setSmartCoverState:];
-[BKSHIDEventSmartCoverAttributes setWakeAnimationStyle:];
-[BKSHIDEventSmartCoverAttributes appendDescriptionToFormatter:];
-[BKSHIDEventSmartCoverAttributes wakeAnimationStyle];
-[BKSHIDEventSmartCoverAttributes smartCoverState];
-[BKSHIDEventSmartCoverAttributes copyWithZone:];
-[BKSHIDEventSmartCoverAttributes isEqual:];
```
