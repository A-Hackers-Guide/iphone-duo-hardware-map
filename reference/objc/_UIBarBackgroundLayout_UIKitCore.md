# `_UIBarBackgroundLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 12 instance variables, 37 properties, 53 instance methods, 0 class methods

## Instance variables

```
d _backgroundAlpha;
d _shadowAlpha;
d _backgroundHeight1;
d _backgroundHeight2;
d _backgroundTransitionProgress;
q _interfaceIdiom;
q _interfaceStyle;
B _useExplicitGeometry;
B _disableTinting;
B _shadowHidden;
@"UIVibrancyEffect" _bg1ShadowEffect;
@"UIVibrancyEffect" _bg2ShadowEffect;
```

## Properties

```
@property (Td,R,N) bgInset;
@property (TB,R,N) shouldUseExplicitGeometry;
@property (Td,R,N) bg1Alpha;
@property (T@"NSArray",R,N) bg1Effects;
@property (T@"UIColor",R,N) bg1Color;
@property (T@"UIImage",R,N) bg1Image;
@property (Td,R,N) bg1ImageAlpha;
@property (Tq,R,N) bg1ImageMode;
@property (TB,R,N) bg1HasShadow;
@property (T@"UIColor",R,N) bg1ShadowColor;
@property (T@"UIImage",R,N) bg1ShadowImage;
@property (T@"UIVibrancyEffect",R,N,V_bg1ShadowEffect) bg1ShadowEffect;
@property (T@"UIColor",R,N) bg1ShadowTint;
@property (Td,R,N) bg1ShadowAlpha;
@property (TB,R,N) bg2Enabled;
@property (Td,R,N) bg2Alpha;
@property (T@"NSArray",R,N) bg2Effects;
@property (T@"UIColor",R,N) bg2Color;
@property (T@"UIImage",R,N) bg2Image;
@property (Tq,R,N) bg2ImageMode;
@property (TB,R,N) bg2HasShadow;
@property (T@"UIColor",R,N) bg2ShadowColor;
@property (T@"UIImage",R,N) bg2ShadowImage;
@property (T@"UIVibrancyEffect",R,N,V_bg2ShadowEffect) bg2ShadowEffect;
@property (T@"UIColor",R,N) bg2ShadowTint;
@property (Td,R,N) bg2ShadowAlpha;
@property (Tq,N,V_interfaceIdiom) interfaceIdiom;
@property (Tq,N,V_interfaceStyle) interfaceStyle;
@property (Td,N,V_backgroundAlpha) backgroundAlpha;
@property (Td,N,V_shadowAlpha) shadowAlpha;
@property (TB,N,V_shadowHidden) shadowHidden;
@property (TB,N,V_useExplicitGeometry) useExplicitGeometry;
@property (Td,N,V_backgroundHeight1) backgroundHeight1;
@property (Td,N,V_backgroundHeight2) backgroundHeight2;
@property (Td,N,V_backgroundTransitionProgress) backgroundTransitionProgress;
@property (Td,R,N) topInset;
@property (TB,N,V_disableTinting) disableTinting;
```

## Instance methods

```
-[_UIBarBackgroundLayout describeInto:];
-[_UIBarBackgroundLayout bg2Alpha];
-[_UIBarBackgroundLayout setShadowAlpha:];
-[_UIBarBackgroundLayout bg1Color];
-[_UIBarBackgroundLayout shadowAlpha];
-[_UIBarBackgroundLayout setShadowHidden:];
-[_UIBarBackgroundLayout setBackgroundTransitionProgress:];
-[_UIBarBackgroundLayout backgroundTransitionProgress];
-[_UIBarBackgroundLayout bg2Color];
-[_UIBarBackgroundLayout bg1ImageMode];
-[_UIBarBackgroundLayout bg2HasShadow];
-[_UIBarBackgroundLayout init];
-[_UIBarBackgroundLayout bg1ShadowTint];
-[_UIBarBackgroundLayout bg2ShadowEffect];
-[_UIBarBackgroundLayout bg2ShadowTint];
-[_UIBarBackgroundLayout setBackgroundAlpha:];
-[_UIBarBackgroundLayout interfaceIdiom];
-[_UIBarBackgroundLayout bg1HasShadow];
-[_UIBarBackgroundLayout bg2ShadowImage];
-[_UIBarBackgroundLayout bg2ImageMode];
-[_UIBarBackgroundLayout bg1Image];
-[_UIBarBackgroundLayout bg1Effects];
-[_UIBarBackgroundLayout bg1Alpha];
-[_UIBarBackgroundLayout bg1ShadowAlpha];
-[_UIBarBackgroundLayout bg2Image];
-[_UIBarBackgroundLayout shouldUseExplicitGeometry];
-[_UIBarBackgroundLayout bg2Effects];
-[_UIBarBackgroundLayout initWithLayout:];
-[_UIBarBackgroundLayout backgroundAlpha];
-[_UIBarBackgroundLayout bgInset];
-[_UIBarBackgroundLayout bg2Enabled];
-[_UIBarBackgroundLayout setInterfaceIdiom:];
-[_UIBarBackgroundLayout bg1ShadowColor];
-[_UIBarBackgroundLayout bg1ImageAlpha];
-[_UIBarBackgroundLayout description];
-[_UIBarBackgroundLayout bg1ShadowEffect];
-[_UIBarBackgroundLayout bg2ShadowAlpha];
-[_UIBarBackgroundLayout setUseExplicitGeometry:];
-[_UIBarBackgroundLayout copyWithZone:];
-[_UIBarBackgroundLayout bg2ShadowColor];
-[_UIBarBackgroundLayout topInset];
-[_UIBarBackgroundLayout bg1ShadowImage];
-[_UIBarBackgroundLayout backgroundHeight1];
-[_UIBarBackgroundLayout backgroundHeight2];
-[_UIBarBackgroundLayout bg2HasHeight];
-[_UIBarBackgroundLayout disableTinting];
-[_UIBarBackgroundLayout interfaceStyle];
-[_UIBarBackgroundLayout setBackgroundHeight1:];
-[_UIBarBackgroundLayout setBackgroundHeight2:];
-[_UIBarBackgroundLayout setDisableTinting:];
-[_UIBarBackgroundLayout setInterfaceStyle:];
-[_UIBarBackgroundLayout shadowHidden];
-[_UIBarBackgroundLayout useExplicitGeometry];
```
