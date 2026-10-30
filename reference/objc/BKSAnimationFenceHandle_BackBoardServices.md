# `BKSAnimationFenceHandle`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`, `BSXPCSecureCoding`, `NSSecureCoding`, `NSCopying`, `BSInvalidatable`
- 1 instance variables, 6 properties, 16 instance methods, 4 class methods

## Instance variables

```
@"CAFenceHandle" _caFence;
```

## Properties

```
@property (TQ,R,N) fenceName;
@property (TB,R,N,GisUsable) usable;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSAnimationFenceHandle supportsBSXPCSecureCoding];
+[BKSAnimationFenceHandle supportsSecureCoding];
+[BKSAnimationFenceHandle newFenceHandleForCAFenceHandle:];
+[BKSAnimationFenceHandle newFenceHandleForContext:];
```

## Instance methods

```
-[BKSAnimationFenceHandle CAFenceHandle];
-[BKSAnimationFenceHandle _initWithCAFenceHandle:];
-[BKSAnimationFenceHandle init];
-[BKSAnimationFenceHandle initWithXPCDictionary:];
-[BKSAnimationFenceHandle dealloc];
-[BKSAnimationFenceHandle fenceName];
-[BKSAnimationFenceHandle invalidate];
-[BKSAnimationFenceHandle encodeWithXPCDictionary:];
-[BKSAnimationFenceHandle CAPort];
-[BKSAnimationFenceHandle encodeWithCoder:];
-[BKSAnimationFenceHandle description];
-[BKSAnimationFenceHandle initWithCoder:];
-[BKSAnimationFenceHandle encodeWithBSXPCCoder:];
-[BKSAnimationFenceHandle initWithBSXPCCoder:];
-[BKSAnimationFenceHandle copyWithZone:];
-[BKSAnimationFenceHandle isUsable];
```
