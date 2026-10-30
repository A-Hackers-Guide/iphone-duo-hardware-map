# `BKSContextRelativePoint`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCSecureCoding`
- 2 instance variables, 6 properties, 7 instance methods, 1 class methods

## Instance variables

```
I _contextID;
{CGPoint="x"d"y"d} _point;
```

## Properties

```
@property (T{CGPoint=dd},R,N,V_point) point;
@property (TI,R,N,V_contextID) contextID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSContextRelativePoint supportsBSXPCSecureCoding];
```

## Instance methods

```
-[BKSContextRelativePoint point];
-[BKSContextRelativePoint hash];
-[BKSContextRelativePoint encodeWithBSXPCCoder:];
-[BKSContextRelativePoint contextID];
-[BKSContextRelativePoint initWithBSXPCCoder:];
-[BKSContextRelativePoint isEqual:];
-[BKSContextRelativePoint initWithPoint:contextID:];
```
