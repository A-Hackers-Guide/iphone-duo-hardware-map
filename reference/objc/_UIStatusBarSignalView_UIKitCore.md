# `_UIStatusBarSignalView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarPersistentAnimationView`
- Protocols: `_UIStatusBarDisplayable`
- 8 instance variables, 17 properties, 22 instance methods, 1 class methods

## Instance variables

```
B _smallSize;
B _rounded;
q _numberOfBars;
q _numberOfActiveBars;
q _signalMode;
@"UIColor" _inactiveColor;
@"UIColor" _activeColor;
q _iconSize;
```

## Properties

```
@property (TB,N,V_rounded) rounded;
@property (Tq,N,V_iconSize) iconSize;
@property (Tq,N,V_numberOfBars) numberOfBars;
@property (Tq,N,V_numberOfActiveBars) numberOfActiveBars;
@property (Tq,N,V_signalMode) signalMode;
@property (T@"UIColor",C,N,V_inactiveColor) inactiveColor;
@property (T@"UIColor",C,N,V_activeColor) activeColor;
@property (TB,N,V_smallSize) smallSize;
@property (TB,?,R,N) wantsCrossfade;
@property (TB,?,R,N) prefersBaselineAlignment;
@property (TB,?,R,N) prefersCenterVerticalAlignment;
@property (Tq,?,R,N) overriddenVerticalAlignment;
@property (T@"UIAccessibilityHUDItem",?,R,N) accessibilityHUDRepresentation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIStatusBarSignalView _intrinsicContentSizeForNumberOfBars:iconSize:];
```

## Instance methods

```
-[_UIStatusBarSignalView setIconSize:];
-[_UIStatusBarSignalView _iconSizeDidChange];
-[_UIStatusBarSignalView iconSize];
-[_UIStatusBarSignalView activeColor];
-[_UIStatusBarSignalView applyStyleAttributes:];
-[_UIStatusBarSignalView setInactiveColor:];
-[_UIStatusBarSignalView _updateActiveBars];
-[_UIStatusBarSignalView inactiveColor];
-[_UIStatusBarSignalView _colorsDidChange];
-[_UIStatusBarSignalView _updateBars];
-[_UIStatusBarSignalView rounded];
-[_UIStatusBarSignalView _updateFromMode:];
-[_UIStatusBarSignalView setRounded:];
-[_UIStatusBarSignalView setActiveColor:];
-[_UIStatusBarSignalView numberOfActiveBars];
-[_UIStatusBarSignalView numberOfBars];
-[_UIStatusBarSignalView setNumberOfActiveBars:];
-[_UIStatusBarSignalView setNumberOfBars:];
-[_UIStatusBarSignalView setSignalMode:];
-[_UIStatusBarSignalView setSmallSize:];
-[_UIStatusBarSignalView signalMode];
-[_UIStatusBarSignalView smallSize];
```
