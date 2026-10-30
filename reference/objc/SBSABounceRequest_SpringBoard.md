# `SBSABounceRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSARequestRepresenting`
- 3 instance variables, 7 properties, 10 instance methods, 1 class methods

## Instance variables

```
q _style;
@? _triggeredBlock;
{CGPoint="x"d"y"d} _velocity;
```

## Properties

```
@property (Tq,R,N,V_style) style;
@property (T{CGPoint=dd},R,N,V_velocity) velocity;
@property (T@?,R,C,N,V_triggeredBlock) triggeredBlock;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSABounceRequest initialize];
```

## Instance methods

```
-[SBSABounceRequest velocity];
-[SBSABounceRequest style];
-[SBSABounceRequest encodeWithCoder:];
-[SBSABounceRequest hash];
-[SBSABounceRequest description];
-[SBSABounceRequest copyWithZone:];
-[SBSABounceRequest isEqual:];
-[SBSABounceRequest membersForCoder];
-[SBSABounceRequest initWithStyle:velocity:triggeredBlock:];
-[SBSABounceRequest triggeredBlock];
```
