# `SBSAStatusBarAvoidanceDescription`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `SBSAInterfaceElementIdentifying`, `NSCopying`, `SBSABlockMutating`
- 4 instance variables, 8 properties, 15 instance methods, 3 class methods

## Instance variables

```
Q _avoidanceFrameUpdateOptions;
@"NSUUID" _interfaceElementIdentifier;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _avoidanceFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _occlusionFrame;
```

## Properties

```
@property (T@"NSUUID",C,N,S_setInterfaceElementIdentifier:,V_interfaceElementIdentifier) interfaceElementIdentifier;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setAvoidanceFrame:,V_avoidanceFrame) avoidanceFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setOcclusionFrame:,V_occlusionFrame) occlusionFrame;
@property (TQ,N,S_setAvoidanceFrameUpdateOptions:,V_avoidanceFrameUpdateOptions) avoidanceFrameUpdateOptions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSAStatusBarAvoidanceDescription initialize];
+[SBSAStatusBarAvoidanceDescription instanceWithBlock:];
+[SBSAStatusBarAvoidanceDescription mutatorClass];
```

## Instance methods

```
-[SBSAStatusBarAvoidanceDescription avoidanceFrame];
-[SBSAStatusBarAvoidanceDescription interfaceElementIdentifier];
-[SBSAStatusBarAvoidanceDescription hash];
-[SBSAStatusBarAvoidanceDescription description];
-[SBSAStatusBarAvoidanceDescription copyWithZone:];
-[SBSAStatusBarAvoidanceDescription isEqual:];
-[SBSAStatusBarAvoidanceDescription copyWithBlock:];
-[SBSAStatusBarAvoidanceDescription membersForCoder];
-[SBSAStatusBarAvoidanceDescription _setInterfaceElementIdentifier:];
-[SBSAStatusBarAvoidanceDescription _setAvoidanceFrame:];
-[SBSAStatusBarAvoidanceDescription _setAvoidanceFrameUpdateOptions:];
-[SBSAStatusBarAvoidanceDescription _setOcclusionFrame:];
-[SBSAStatusBarAvoidanceDescription avoidanceFrameUpdateOptions];
-[SBSAStatusBarAvoidanceDescription copyByPixelAligningGeometryWithScale:];
-[SBSAStatusBarAvoidanceDescription occlusionFrame];
```
