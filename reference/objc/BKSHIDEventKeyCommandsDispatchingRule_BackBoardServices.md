# `BKSHIDEventKeyCommandsDispatchingRule`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `BSDescriptionProviding`, `NSCopying`
- 2 instance variables, 6 properties, 15 instance methods, 2 class methods

## Instance variables

```
@"BKSHIDEventKeyCommandsDispatchingPredicate" _predicate;
@"NSArray" _targets;
```

## Properties

```
@property (T@"BKSHIDEventKeyCommandsDispatchingPredicate",R,C,N,V_predicate) predicate;
@property (T@"NSArray",R,C,N,V_targets) targets;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventKeyCommandsDispatchingRule supportsSecureCoding];
+[BKSHIDEventKeyCommandsDispatchingRule ruleForDispatchingKeyCommandsMatchingPredicate:toTargets:];
```

## Instance methods

```
-[BKSHIDEventKeyCommandsDispatchingRule debugDescription];
-[BKSHIDEventKeyCommandsDispatchingRule succinctDescriptionBuilder];
-[BKSHIDEventKeyCommandsDispatchingRule init];
-[BKSHIDEventKeyCommandsDispatchingRule descriptionWithMultilinePrefix:];
-[BKSHIDEventKeyCommandsDispatchingRule succinctDescription];
-[BKSHIDEventKeyCommandsDispatchingRule encodeWithCoder:];
-[BKSHIDEventKeyCommandsDispatchingRule hash];
-[BKSHIDEventKeyCommandsDispatchingRule targets];
-[BKSHIDEventKeyCommandsDispatchingRule description];
-[BKSHIDEventKeyCommandsDispatchingRule initWithCoder:];
-[BKSHIDEventKeyCommandsDispatchingRule predicate];
-[BKSHIDEventKeyCommandsDispatchingRule copyWithZone:];
-[BKSHIDEventKeyCommandsDispatchingRule isEqual:];
-[BKSHIDEventKeyCommandsDispatchingRule descriptionBuilderWithMultilinePrefix:];
-[BKSHIDEventKeyCommandsDispatchingRule _initWithPredicate:targets:];
```
