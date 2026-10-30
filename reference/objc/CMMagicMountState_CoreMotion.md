# `CMMagicMountState`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- 1 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
q _mountStatus;
```

## Properties

```
@property (TB,R,N,GisMounted) mounted;
@property (Tq,R,N,V_mountStatus) mountStatus;
```

## Class methods

```
+[CMMagicMountState supportsSecureCoding];
```

## Instance methods

```
-[CMMagicMountState isMounted];
-[CMMagicMountState encodeWithCoder:];
-[CMMagicMountState description];
-[CMMagicMountState initWithCoder:];
-[CMMagicMountState copyWithZone:];
-[CMMagicMountState initWithMountStatus:timestamp:];
-[CMMagicMountState mountStatus];
```
