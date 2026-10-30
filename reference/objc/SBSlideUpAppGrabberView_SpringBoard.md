# `SBSlideUpAppGrabberView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_SBFVibrantView`, `SBUILegibility`
- 10 instance variables, 9 properties, 19 instance methods, 0 class methods

## Instance variables

```
d _strength;
@"_UILegibilitySettings" _legibilitySettings;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _hitTestEdgeInsets;
@"UIView" _tintView;
@"UIView" _backgroundView;
@"SBUILegibilityView" _legibilityView;
@"SBSaturatedIconView" _saturatedIconView;
@"UIImage" _grabberImage;
B _vibrancyAllowed;
@"_SBFVibrantSettings" _vibrantSettings;
```

## Properties

```
@property (T{UIEdgeInsets=dddd},R,N,V_hitTestEdgeInsets) hitTestEdgeInsets;
@property (TB,N,GisVibrancyAllowed,V_vibrancyAllowed) vibrancyAllowed;
@property (T@"_SBFVibrantSettings",&,N,V_vibrantSettings) vibrantSettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,N,V_strength) strength;
@property (T@"_UILegibilitySettings",&,N,V_legibilitySettings) legibilitySettings;
```

## Instance methods

```
-[SBSlideUpAppGrabberView strength];
-[SBSlideUpAppGrabberView setStrength:];
-[SBSlideUpAppGrabberView layoutSubviews];
-[SBSlideUpAppGrabberView setBackgroundColor:];
-[SBSlideUpAppGrabberView sizeThatFits:];
-[SBSlideUpAppGrabberView vibrantSettings];
-[SBSlideUpAppGrabberView hitTestEdgeInsets];
-[SBSlideUpAppGrabberView legibilitySettings];
-[SBSlideUpAppGrabberView pointInside:withEvent:];
-[SBSlideUpAppGrabberView setLegibilitySettings:];
-[SBSlideUpAppGrabberView setVibrantSettings:];
-[SBSlideUpAppGrabberView setBackgroundView:];
-[SBSlideUpAppGrabberView _shouldUseVibrancy];
-[SBSlideUpAppGrabberView isVibrancyAllowed];
-[SBSlideUpAppGrabberView setVibrancyAllowed:];
-[SBSlideUpAppGrabberView _lazyLegibilityView];
-[SBSlideUpAppGrabberView initWithAdditionalTopPadding:invertVerticalInsets:];
-[SBSlideUpAppGrabberView setAppStyleGrabberImage:];
-[SBSlideUpAppGrabberView setGrabberImageFromAppWithBundleIdentifier:];
```
