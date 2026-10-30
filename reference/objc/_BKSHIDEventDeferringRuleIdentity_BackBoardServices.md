# `_BKSHIDEventDeferringRuleIdentity`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`, `NSCopying`, `NSSecureCoding`
- 2 instance variables, 6 properties, 10 instance methods, 1 class methods

## Instance variables

```
I _seed;
i _pid;
```

## Properties

```
@property (TI,R,N,V_seed) seed;
@property (Ti,R,N,V_pid) pid;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_BKSHIDEventDeferringRuleIdentity supportsSecureCoding];
```

## Instance methods

```
-[_BKSHIDEventDeferringRuleIdentity seed];
-[_BKSHIDEventDeferringRuleIdentity initWithSeed:pid:];
-[_BKSHIDEventDeferringRuleIdentity appendDescriptionToFormatter:];
-[_BKSHIDEventDeferringRuleIdentity pid];
-[_BKSHIDEventDeferringRuleIdentity encodeWithCoder:];
-[_BKSHIDEventDeferringRuleIdentity hash];
-[_BKSHIDEventDeferringRuleIdentity description];
-[_BKSHIDEventDeferringRuleIdentity initWithCoder:];
-[_BKSHIDEventDeferringRuleIdentity copyWithZone:];
-[_BKSHIDEventDeferringRuleIdentity isEqual:];
```
