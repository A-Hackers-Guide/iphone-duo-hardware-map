# `BKSHIDEventDiscreteDispatchingPredicate`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSSecureCoding`, `NSCopying`, `NSMutableCopying`
- 3 instance variables, 7 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSSet" _senderDescriptors;
@"NSSet" _descriptors;
@"NSSet" _fuzzyDescriptors;
```

## Properties

```
@property (T@"NSSet",R,C,N,V_senderDescriptors) senderDescriptors;
@property (T@"NSSet",R,C,N,V_descriptors) descriptors;
@property (T@"NSSet",R,C,D,N) displays;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventDiscreteDispatchingPredicate supportsSecureCoding];
```

## Instance methods

```
-[BKSHIDEventDiscreteDispatchingPredicate mutableCopyWithZone:];
-[BKSHIDEventDiscreteDispatchingPredicate init];
-[BKSHIDEventDiscreteDispatchingPredicate descriptors];
-[BKSHIDEventDiscreteDispatchingPredicate displays];
-[BKSHIDEventDiscreteDispatchingPredicate encodeWithCoder:];
-[BKSHIDEventDiscreteDispatchingPredicate hash];
-[BKSHIDEventDiscreteDispatchingPredicate description];
-[BKSHIDEventDiscreteDispatchingPredicate initWithCoder:];
-[BKSHIDEventDiscreteDispatchingPredicate appendDescriptionToStream:];
-[BKSHIDEventDiscreteDispatchingPredicate copyWithZone:];
-[BKSHIDEventDiscreteDispatchingPredicate isEqual:];
-[BKSHIDEventDiscreteDispatchingPredicate _initWithSourceDescriptors:descriptors:];
-[BKSHIDEventDiscreteDispatchingPredicate containsDescriptor:];
-[BKSHIDEventDiscreteDispatchingPredicate senderDescriptors];
-[BKSHIDEventDiscreteDispatchingPredicate specifiesDescriptor:];
```
