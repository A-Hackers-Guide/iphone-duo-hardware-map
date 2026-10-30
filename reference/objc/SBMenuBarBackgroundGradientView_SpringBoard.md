# `SBMenuBarBackgroundGradientView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFTouchPassThroughView`
- 2 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
B _menuBarContentIsLight;
@"SBMenuBarBackgroundGradientViewGradientLayerView" _gradientView;
```

## Properties

```
@property (T@"CABackdropLayer",R,D,N) layer;
@property (T@"SBMenuBarBackgroundGradientViewGradientLayerView",&,N,V_gradientView) gradientView;
@property (TB,N,GisMenuBarContentLight,V_menuBarContentIsLight) menuBarContentIsLight;
```

## Class methods

```
+[SBMenuBarBackgroundGradientView layerClass];
```

## Instance methods

```
-[SBMenuBarBackgroundGradientView gradientView];
-[SBMenuBarBackgroundGradientView setGradientView:];
-[SBMenuBarBackgroundGradientView layoutSubviews];
-[SBMenuBarBackgroundGradientView _shouldAnimatePropertyWithKey:];
-[SBMenuBarBackgroundGradientView _setupVariableLayerProperties];
-[SBMenuBarBackgroundGradientView initWithMenuBarContentIsLight:];
-[SBMenuBarBackgroundGradientView isMenuBarContentLight];
-[SBMenuBarBackgroundGradientView setMenuBarContentIsLight:];
```
