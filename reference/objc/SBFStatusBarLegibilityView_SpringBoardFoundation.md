# `SBFStatusBarLegibilityView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `SBUILegibility`
- 5 instance variables, 10 properties, 16 instance methods, 2 class methods

## Instance variables

```
B _forceLegibilityGradientHidden;
@"_UILegibilitySettings" _legibilitySettings;
@"UIView" _statusBarGradientView;
@"UIImageView" _leftCornerView;
@"UIImageView" _rightCornerView;
```

## Properties

```
@property (T@"UIView",&,N,V_statusBarGradientView) statusBarGradientView;
@property (T@"UIImageView",&,N,V_leftCornerView) leftCornerView;
@property (T@"UIImageView",&,N,V_rightCornerView) rightCornerView;
@property (TB,N,V_forceLegibilityGradientHidden) forceLegibilityGradientHidden;
@property (Td,D,N) strength;
@property (T@"_UILegibilitySettings",&,N,V_legibilitySettings) legibilitySettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBFStatusBarLegibilityView statusBarGradientView];
+[SBFStatusBarLegibilityView gradientViewWithOpacities:locations:];
```

## Instance methods

```
-[SBFStatusBarLegibilityView setStatusBarGradientView:];
-[SBFStatusBarLegibilityView strength];
-[SBFStatusBarLegibilityView setStrength:];
-[SBFStatusBarLegibilityView layoutSubviews];
-[SBFStatusBarLegibilityView _configureWithLegibilitySettings:forceLegibilityGradientHidden:];
-[SBFStatusBarLegibilityView _configureAsPad];
-[SBFStatusBarLegibilityView setForceLegibilityGradientHidden:];
-[SBFStatusBarLegibilityView statusBarGradientView];
-[SBFStatusBarLegibilityView rightCornerView];
-[SBFStatusBarLegibilityView legibilitySettings];
-[SBFStatusBarLegibilityView setLeftCornerView:];
-[SBFStatusBarLegibilityView _configureAsPhone];
-[SBFStatusBarLegibilityView forceLegibilityGradientHidden];
-[SBFStatusBarLegibilityView setLegibilitySettings:];
-[SBFStatusBarLegibilityView leftCornerView];
-[SBFStatusBarLegibilityView setRightCornerView:];
```
