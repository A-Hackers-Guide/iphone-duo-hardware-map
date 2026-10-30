# `SBSAContainerViewDescription`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSAViewDescription`
- Protocols: `SBSAElementAssociating`, `SBSAContainerKeyLineDescribing`, `SBSAContainerShadowDescribing`
- 15 instance variables, 20 properties, 38 instance methods, 2 class methods

## Instance variables

```
B _contentClippingEnabled;
B _userInteractionEnabled;
q _elevationStyle;
d _resolutionTransitionStrength;
d _contentBorderWidth;
@"<SAElementIdentifying>" _associatedSystemApertureElementIdentity;
q _keyLineMode;
@"UIColor" _keyLineTintColor;
q _sampledBackgroundLuminanceLevel;
q _shadowStyle;
{CGSize="width"d"height"d} _contentScale;
{CGPoint="x"d"y"d} _contentCenter;
{SBSystemApertureContainerRenderingConfiguration="renderingStyle"q"cloningStyle"q"alwaysRenderInSnapshots"B} _renderingConfiguration;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _contentBounds;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _contentRotationTransform;
```

## Properties

```
@property (T@"<SAElementIdentifying>",C,N,S_setAssociatedSystemApertureElementIdentity:,V_associatedSystemApertureElementIdentity) associatedSystemApertureElementIdentity;
@property (T{CGSize=dd},N,S_setContentScale:,V_contentScale) contentScale;
@property (T{CGAffineTransform=dddddd},N,S_setContentRotationTransform:,V_contentRotationTransform) contentRotationTransform;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setContentBounds:,V_contentBounds) contentBounds;
@property (T{CGPoint=dd},N,S_setContentCenter:,V_contentCenter) contentCenter;
@property (Tq,N,S_setKeyLineMode:,V_keyLineMode) keyLineMode;
@property (T@"UIColor",C,N,S_setKeyLineTintColor:,V_keyLineTintColor) keyLineTintColor;
@property (Tq,N,S_setSampledBackgroundLuminanceLevel:,V_sampledBackgroundLuminanceLevel) sampledBackgroundLuminanceLevel;
@property (Tq,N,S_setShadowStyle:,V_shadowStyle) shadowStyle;
@property (T{SBSystemApertureContainerRenderingConfiguration=qqB},N,S_setRenderingConfiguration:,V_renderingConfiguration) renderingConfiguration;
@property (Tq,N,S_setElevationStyle:,V_elevationStyle) elevationStyle;
@property (TB,N,GisContentClippingEnabled,S_setContentClippingEnabled:,V_contentClippingEnabled) contentClippingEnabled;
@property (TB,N,GisUserInteractionEnabled,S_setUserInteractionEnabled:,V_userInteractionEnabled) userInteractionEnabled;
@property (Td,N,S_setResolutionTransitionStrength:,V_resolutionTransitionStrength) resolutionTransitionStrength;
@property (Td,N,S_setContentBorderWidth:,V_contentBorderWidth) contentBorderWidth;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSUUID",R,C,N) interfaceElementIdentifier;
```

## Class methods

```
+[SBSAContainerViewDescription initialize];
+[SBSAContainerViewDescription mutatorClass];
```

## Instance methods

```
-[SBSAContainerViewDescription shadowStyle];
-[SBSAContainerViewDescription contentBorderWidth];
-[SBSAContainerViewDescription associatedSystemApertureElementIdentity];
-[SBSAContainerViewDescription contentBounds];
-[SBSAContainerViewDescription resolutionTransitionStrength];
-[SBSAContainerViewDescription keyLineTintColor];
-[SBSAContainerViewDescription isContentClippingEnabled];
-[SBSAContainerViewDescription isUserInteractionEnabled];
-[SBSAContainerViewDescription sampledBackgroundLuminanceLevel];
-[SBSAContainerViewDescription init];
-[SBSAContainerViewDescription keyLineMode];
-[SBSAContainerViewDescription elevationStyle];
-[SBSAContainerViewDescription _setShadowStyle:];
-[SBSAContainerViewDescription _setContentBounds:];
-[SBSAContainerViewDescription _setContentScale:];
-[SBSAContainerViewDescription encodeWithCoder:];
-[SBSAContainerViewDescription contentScale];
-[SBSAContainerViewDescription renderingConfiguration];
-[SBSAContainerViewDescription hash];
-[SBSAContainerViewDescription description];
-[SBSAContainerViewDescription contentCenter];
-[SBSAContainerViewDescription copyWithZone:];
-[SBSAContainerViewDescription isEqual:];
-[SBSAContainerViewDescription contentRotationTransform];
-[SBSAContainerViewDescription membersForCoder];
-[SBSAContainerViewDescription _setContentCenter:];
-[SBSAContainerViewDescription _setUserInteractionEnabled:];
-[SBSAContainerViewDescription _setAssociatedSystemApertureElementIdentity:];
-[SBSAContainerViewDescription _setContentBorderWidth:];
-[SBSAContainerViewDescription _setContentClippingEnabled:];
-[SBSAContainerViewDescription _setContentRotationTransform:];
-[SBSAContainerViewDescription _setElevationStyle:];
-[SBSAContainerViewDescription _setKeyLineMode:];
-[SBSAContainerViewDescription _setKeyLineTintColor:];
-[SBSAContainerViewDescription _setRenderingConfiguration:];
-[SBSAContainerViewDescription _setResolutionTransitionStrength:];
-[SBSAContainerViewDescription _setSampledBackgroundLuminanceLevel:];
-[SBSAContainerViewDescription copyByPixelAligningGeometryWithScale:];
```
