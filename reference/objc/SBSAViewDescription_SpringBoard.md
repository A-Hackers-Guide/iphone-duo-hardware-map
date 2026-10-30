# `SBSAViewDescription`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `SBSAInterfaceElementDescribing`, `NSCopying`, `SBSABlockMutating`
- 9 instance variables, 13 properties, 26 instance methods, 3 class methods

## Instance variables

```
@"UIColor" _backgroundColor;
d _blurRadius;
@"NSUUID" _interfaceElementIdentifier;
d _cornerRadius;
d _alpha;
{CGPoint="x"d"y"d} _center;
{CGSize="width"d"height"d} _scale;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _boundsVelocity;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _bounds;
```

## Properties

```
@property (T@"NSUUID",C,N,S_setInterfaceElementIdentifier:,V_interfaceElementIdentifier) interfaceElementIdentifier;
@property (T{CGPoint=dd},N,S_setCenter:,V_center) center;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setBounds:,V_bounds) bounds;
@property (Td,N,S_setCornerRadius:,V_cornerRadius) cornerRadius;
@property (Td,N,S_setAlpha:,V_alpha) alpha;
@property (T{CGSize=dd},N,S_setScale:,V_scale) scale;
@property (T@"UIColor",&,N,S_setBackgroundColor:,V_backgroundColor) backgroundColor;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setBoundsVelocity:,V_boundsVelocity) boundsVelocity;
@property (Td,N,S_setBlurRadius:,V_blurRadius) blurRadius;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSAViewDescription initialize];
+[SBSAViewDescription instanceWithBlock:];
+[SBSAViewDescription mutatorClass];
```

## Instance methods

```
-[SBSAViewDescription _setBounds:];
-[SBSAViewDescription _setCornerRadius:];
-[SBSAViewDescription scale];
-[SBSAViewDescription blurRadius];
-[SBSAViewDescription center];
-[SBSAViewDescription cornerRadius];
-[SBSAViewDescription interfaceElementIdentifier];
-[SBSAViewDescription hash];
-[SBSAViewDescription backgroundColor];
-[SBSAViewDescription bounds];
-[SBSAViewDescription description];
-[SBSAViewDescription alpha];
-[SBSAViewDescription copyWithZone:];
-[SBSAViewDescription isEqual:];
-[SBSAViewDescription copyWithBlock:];
-[SBSAViewDescription _setBackgroundColor:];
-[SBSAViewDescription _setScale:];
-[SBSAViewDescription membersForCoder];
-[SBSAViewDescription _setAlpha:];
-[SBSAViewDescription _setCenter:];
-[SBSAViewDescription _setBlurRadius:];
-[SBSAViewDescription _setInterfaceElementIdentifier:];
-[SBSAViewDescription _setBoundsVelocity:];
-[SBSAViewDescription boundsVelocity];
-[SBSAViewDescription copyByPixelAligningGeometryWithScale:];
-[SBSAViewDescription initWithViewDescription:];
```
