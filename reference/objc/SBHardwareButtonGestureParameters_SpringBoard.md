# `SBHardwareButtonGestureParameters`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `NSCopying`, `NSMutableCopying`
- 3 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
q _maximumPressCount;
d _longPressTimeInterval;
d _multiplePressTimeInterval;
```

## Properties

```
@property (Tq,R,N,V_maximumPressCount) maximumPressCount;
@property (Td,R,N,V_longPressTimeInterval) longPressTimeInterval;
@property (Td,R,N,V_multiplePressTimeInterval) multiplePressTimeInterval;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBHardwareButtonGestureParameters mutableCopyWithZone:];
-[SBHardwareButtonGestureParameters succinctDescriptionBuilder];
-[SBHardwareButtonGestureParameters descriptionWithMultilinePrefix:];
-[SBHardwareButtonGestureParameters maximumPressCount];
-[SBHardwareButtonGestureParameters succinctDescription];
-[SBHardwareButtonGestureParameters description];
-[SBHardwareButtonGestureParameters multiplePressTimeInterval];
-[SBHardwareButtonGestureParameters longPressTimeInterval];
-[SBHardwareButtonGestureParameters copyWithZone:];
-[SBHardwareButtonGestureParameters descriptionBuilderWithMultilinePrefix:];
```
