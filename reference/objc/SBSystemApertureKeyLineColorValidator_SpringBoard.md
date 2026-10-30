# `SBSystemApertureKeyLineColorValidator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PTSettingsKeyObserver`
- 5 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"SBSystemApertureSettings" _settings;
^{CGColorSpace=} _labColorSpace;
^{CGColorSpace=} _rgbColorSpace;
^{CGColorTransform=} _colorTransformToLAB;
^{CGColorTransform=} _colorTransformToRGB;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemApertureKeyLineColorValidator init];
-[SBSystemApertureKeyLineColorValidator dealloc];
-[SBSystemApertureKeyLineColorValidator settings:changedValueForKey:];
-[SBSystemApertureKeyLineColorValidator _applySettingsValues];
-[SBSystemApertureKeyLineColorValidator validateKeyLineColor:];
```
