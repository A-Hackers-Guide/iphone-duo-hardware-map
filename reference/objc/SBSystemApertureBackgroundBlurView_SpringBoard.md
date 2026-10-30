# `SBSystemApertureBackgroundBlurView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 4 instance variables, 2 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"SBSDFView" _sdfView;
@"SBSDFElementView" _sdfElementView;
d _elementCornerRadius;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _elementFrame;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_elementFrame) elementFrame;
@property (Td,N,V_elementCornerRadius) elementCornerRadius;
```

## Class methods

```
+[SBSystemApertureBackgroundBlurView layerClass];
+[SBSystemApertureBackgroundBlurView haloExtent];
```

## Instance methods

```
-[SBSystemApertureBackgroundBlurView backdropLayer];
-[SBSystemApertureBackgroundBlurView initWithFrame:];
-[SBSystemApertureBackgroundBlurView elementFrame];
-[SBSystemApertureBackgroundBlurView _configureSDFHierarchy];
-[SBSystemApertureBackgroundBlurView _configureVariableBlurFilter];
-[SBSystemApertureBackgroundBlurView _newGradientEffect];
-[SBSystemApertureBackgroundBlurView elementCornerRadius];
-[SBSystemApertureBackgroundBlurView setElementCornerRadius:];
-[SBSystemApertureBackgroundBlurView setElementFrame:];
```
