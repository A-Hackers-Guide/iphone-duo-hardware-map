# `SBPIPFadeInOutSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 7 instance variables, 9 properties, 17 instance methods, 2 class methods

## Instance variables

```
@"SBFAnimationSettings" _fadeInOutAnimationSettings;
d _fadeInInitialScale;
d _fadeInInitialOpacity;
d _fadeInInitialBlurRadius;
d _fadeOutFinalScale;
d _fadeOutFinalOpacity;
d _fadeOutFinalBlurRadius;
```

## Properties

```
@property (Td,N,V_fadeInInitialScale) fadeInInitialScale;
@property (Td,N,V_fadeInInitialOpacity) fadeInInitialOpacity;
@property (Td,N,V_fadeInInitialBlurRadius) fadeInInitialBlurRadius;
@property (Td,N,V_fadeOutFinalScale) fadeOutFinalScale;
@property (Td,N,V_fadeOutFinalOpacity) fadeOutFinalOpacity;
@property (Td,N,V_fadeOutFinalBlurRadius) fadeOutFinalBlurRadius;
@property (T@"SBFAnimationSettings",&,N,V_fadeInOutAnimationSettings) fadeInOutAnimationSettings;
@property (T{?=ddd},R,N) fadeInInitialValues;
@property (T{?=ddd},R,N) fadeOutFinalValues;
```

## Class methods

```
+[SBPIPFadeInOutSettings ignoresKey:];
+[SBPIPFadeInOutSettings settingsControllerModule];
```

## Instance methods

```
-[SBPIPFadeInOutSettings setDefaultValues];
-[SBPIPFadeInOutSettings fadeInInitialBlurRadius];
-[SBPIPFadeInOutSettings fadeInInitialOpacity];
-[SBPIPFadeInOutSettings fadeInInitialScale];
-[SBPIPFadeInOutSettings fadeInInitialValues];
-[SBPIPFadeInOutSettings fadeInOutAnimationSettings];
-[SBPIPFadeInOutSettings fadeOutFinalBlurRadius];
-[SBPIPFadeInOutSettings fadeOutFinalOpacity];
-[SBPIPFadeInOutSettings fadeOutFinalScale];
-[SBPIPFadeInOutSettings fadeOutFinalValues];
-[SBPIPFadeInOutSettings setFadeInInitialBlurRadius:];
-[SBPIPFadeInOutSettings setFadeInInitialOpacity:];
-[SBPIPFadeInOutSettings setFadeInInitialScale:];
-[SBPIPFadeInOutSettings setFadeInOutAnimationSettings:];
-[SBPIPFadeInOutSettings setFadeOutFinalBlurRadius:];
-[SBPIPFadeInOutSettings setFadeOutFinalOpacity:];
-[SBPIPFadeInOutSettings setFadeOutFinalScale:];
```
