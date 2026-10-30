# `BKSHIDEventDiscreteDispatchingRule`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`, `NSSecureCoding`, `NSCopying`
- 3 instance variables, 7 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"BKSHIDEventDiscreteDispatchingPredicate" _predicate;
@"BKSHIDEventDispatchingTarget" _target;
Q _predicateEventTypeMask;
```

## Properties

```
@property (TQ,R,N,V_predicateEventTypeMask) predicateEventTypeMask;
@property (T@"BKSHIDEventDiscreteDispatchingPredicate",R,C,N,V_predicate) predicate;
@property (T@"BKSHIDEventDispatchingTarget",R,C,N,V_target) target;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventDiscreteDispatchingRule supportsSecureCoding];
+[BKSHIDEventDiscreteDispatchingRule ruleForDispatchingDiscreteEventsMatchingPredicate:toTarget:];
```

## Instance methods

```
-[BKSHIDEventDiscreteDispatchingRule init];
-[BKSHIDEventDiscreteDispatchingRule appendDescriptionToFormatter:];
-[BKSHIDEventDiscreteDispatchingRule encodeWithCoder:];
-[BKSHIDEventDiscreteDispatchingRule hash];
-[BKSHIDEventDiscreteDispatchingRule description];
-[BKSHIDEventDiscreteDispatchingRule initWithCoder:];
-[BKSHIDEventDiscreteDispatchingRule predicate];
-[BKSHIDEventDiscreteDispatchingRule target];
-[BKSHIDEventDiscreteDispatchingRule copyWithZone:];
-[BKSHIDEventDiscreteDispatchingRule isEqual:];
-[BKSHIDEventDiscreteDispatchingRule _initWithPredicate:target:];
-[BKSHIDEventDiscreteDispatchingRule predicateEventTypeMask];
```
