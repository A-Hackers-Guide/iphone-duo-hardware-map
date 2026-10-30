# `SBMutableStatusBarSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBStatusBarSettings`
- 0 instance variables, 8 properties, 12 instance methods, 0 class methods

## Properties

```
@property (Tq,D,N,G_uiPreferredAxis,S_setUIPreferredAxis:) uiPreferredAxis;
@property (T@"NSNumber",&,D,N) alpha;
@property (T@"NSDictionary",C,D,N) partAlphas;
@property (Tq,D,N) style;
@property (TQ,D,N) hiddenParts;
@property (Tq,D,N) preferredAxis;
@property (T@"_UILegibilitySettings",&,D,N) legibilitySettings;
@property (T@"NSSet",C,D,N) backgroundActivitiesToSuppress;
```

## Instance methods

```
-[SBMutableStatusBarSettings setPartAlphas:];
-[SBMutableStatusBarSettings init];
-[SBMutableStatusBarSettings setBackgroundActivitiesToSuppress:];
-[SBMutableStatusBarSettings _setUIPreferredAxis:];
-[SBMutableStatusBarSettings setStyle:];
-[SBMutableStatusBarSettings setAlpha:forParts:];
-[SBMutableStatusBarSettings setPreferredAxis:];
-[SBMutableStatusBarSettings setAlpha:];
-[SBMutableStatusBarSettings applySettings:];
-[SBMutableStatusBarSettings copyWithZone:];
-[SBMutableStatusBarSettings setLegibilitySettings:];
-[SBMutableStatusBarSettings setHiddenParts:];
```
