# `BKSHIDEventKeyCommandDispatchingRoot`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKSHIDEventDeliveryRuleWrapper`
- 0 instance variables, 3 properties, 3 instance methods, 1 class methods

## Properties

```
@property (T@"NSString",R,C,D,N) reason;
@property (TI,R,D,N) seed;
@property (T@"BKSHIDEventKeyCommandsDispatchingRule",R,C,N) rule;
```

## Class methods

```
+[BKSHIDEventKeyCommandDispatchingRoot supportsSecureCoding];
```

## Instance methods

```
-[BKSHIDEventKeyCommandDispatchingRoot rule];
-[BKSHIDEventKeyCommandDispatchingRoot decodePayload:];
-[BKSHIDEventKeyCommandDispatchingRoot initWithReason:seed:rule:];
```
