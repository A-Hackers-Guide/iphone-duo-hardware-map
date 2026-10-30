# `BKSHIDEventGenericGestureDescriptor`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKSHIDEventDescriptor`
- 2 instance variables, 1 properties, 10 instance methods, 3 class methods

## Instance variables

```
B _isWildcard;
I _genericGestureType;
```

## Properties

```
@property (TI,R,N,V_genericGestureType) genericGestureType;
```

## Class methods

```
+[BKSHIDEventGenericGestureDescriptor supportsSecureCoding];
+[BKSHIDEventGenericGestureDescriptor descriptorForAnyGenericGestureType];
+[BKSHIDEventGenericGestureDescriptor descriptorWithGenericGestureType:];
```

## Instance methods

```
-[BKSHIDEventGenericGestureDescriptor init];
-[BKSHIDEventGenericGestureDescriptor initWithGenericGestureType:];
-[BKSHIDEventGenericGestureDescriptor describes:];
-[BKSHIDEventGenericGestureDescriptor encodeWithCoder:];
-[BKSHIDEventGenericGestureDescriptor genericGestureType];
-[BKSHIDEventGenericGestureDescriptor hash];
-[BKSHIDEventGenericGestureDescriptor requiresFuzzyMatching];
-[BKSHIDEventGenericGestureDescriptor initWithCoder:];
-[BKSHIDEventGenericGestureDescriptor appendDescriptionToStream:];
-[BKSHIDEventGenericGestureDescriptor isEqual:];
```
