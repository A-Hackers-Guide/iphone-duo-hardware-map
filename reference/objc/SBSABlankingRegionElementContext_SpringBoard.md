# `SBSABlankingRegionElementContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `NSCopying`, `SAElementIdentifying`, `SBSABlockMutating`, `SBSATouchTransparency`
- 9 instance variables, 13 properties, 25 instance methods, 3 class methods

## Instance variables

```
B _transparentToTouches;
@"NSString" _clientIdentifier;
@"NSString" _elementIdentifier;
@"NSString" _regionIdentifier;
d _circleDiameter;
d _cornerRadius;
d _rrRegionDiameter;
{CGPoint="x"d"y"d} _sensorCenter;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _regionFrame;
```

## Properties

```
@property (T@"NSString",C,N,S_setClientIdentifier:,V_clientIdentifier) clientIdentifier;
@property (T@"NSString",C,N,S_setElementIdentifier:,V_elementIdentifier) elementIdentifier;
@property (T@"NSString",C,N,S_setRegionIdentifier:,V_regionIdentifier) regionIdentifier;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setRegionFrame:,V_regionFrame) regionFrame;
@property (T{CGPoint=dd},N,S_setSensorCenter:,V_sensorCenter) sensorCenter;
@property (Td,N,S_setCircleDiameter:,V_circleDiameter) circleDiameter;
@property (Td,N,S_setCornerRadius:,V_cornerRadius) cornerRadius;
@property (Td,N,S_setRRRegionDiameter:,V_rrRegionDiameter) rrRegionDiameter;
@property (TB,N,GisTransparentToTouches,S_setTransparentToTouches:,V_transparentToTouches) transparentToTouches;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSABlankingRegionElementContext initialize];
+[SBSABlankingRegionElementContext instanceWithBlock:];
+[SBSABlankingRegionElementContext mutatorClass];
```

## Instance methods

```
-[SBSABlankingRegionElementContext _setCornerRadius:];
-[SBSABlankingRegionElementContext clientIdentifier];
-[SBSABlankingRegionElementContext elementIdentifier];
-[SBSABlankingRegionElementContext isTransparentToTouches];
-[SBSABlankingRegionElementContext cornerRadius];
-[SBSABlankingRegionElementContext hash];
-[SBSABlankingRegionElementContext description];
-[SBSABlankingRegionElementContext copyWithZone:];
-[SBSABlankingRegionElementContext regionIdentifier];
-[SBSABlankingRegionElementContext isEqual:];
-[SBSABlankingRegionElementContext copyWithBlock:];
-[SBSABlankingRegionElementContext regionFrame];
-[SBSABlankingRegionElementContext membersForCoder];
-[SBSABlankingRegionElementContext circleDiameter];
-[SBSABlankingRegionElementContext _setCircleDiameter:];
-[SBSABlankingRegionElementContext _setClientIdentifier:];
-[SBSABlankingRegionElementContext _setElementIdentifier:];
-[SBSABlankingRegionElementContext _setRRRegionDiameter:];
-[SBSABlankingRegionElementContext _setRegionFrame:];
-[SBSABlankingRegionElementContext _setRegionIdentifier:];
-[SBSABlankingRegionElementContext _setSensorCenter:];
-[SBSABlankingRegionElementContext _setTransparentToTouches:];
-[SBSABlankingRegionElementContext initWithBlankingRegionElementContext:];
-[SBSABlankingRegionElementContext rrRegionDiameter];
-[SBSABlankingRegionElementContext sensorCenter];
```
