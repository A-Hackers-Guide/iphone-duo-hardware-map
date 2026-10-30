# `SBHardwareButtonDropletAnimationEvent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifierEvent`
- 2 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"<SBHardwareButtonLaunchPreludeAnimationToken>" _preludeToken;
@"<SBHardwareButtonLaunchZoomUpAnimationToken>" _zoomUpToken;
```

## Properties

```
@property (TQ,R,N) eventSubtype;
@property (T@"<SBHardwareButtonLaunchPreludeAnimationToken>",R,N,V_preludeToken) preludeToken;
@property (T@"<SBHardwareButtonLaunchZoomUpAnimationToken>",R,N,V_zoomUpToken) zoomUpToken;
```

## Instance methods

```
-[SBHardwareButtonDropletAnimationEvent type];
-[SBHardwareButtonDropletAnimationEvent copyWithZone:];
-[SBHardwareButtonDropletAnimationEvent descriptionBuilderWithMultilinePrefix:];
-[SBHardwareButtonDropletAnimationEvent eventSubtype];
-[SBHardwareButtonDropletAnimationEvent initWithPreludeToken:zoomUpToken:];
-[SBHardwareButtonDropletAnimationEvent preludeToken];
-[SBHardwareButtonDropletAnimationEvent zoomUpToken];
```
