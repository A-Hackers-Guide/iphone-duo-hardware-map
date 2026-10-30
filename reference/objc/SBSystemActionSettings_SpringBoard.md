# `SBSystemActionSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 4 instance variables, 4 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"SBSystemActionPreviewSettings" _previewSettings;
@"SBSystemActionCoachingSettings" _coachingSettings;
d _popScale;
d _inflateScale;
```

## Properties

```
@property (T@"SBSystemActionPreviewSettings",R,N,V_previewSettings) previewSettings;
@property (T@"SBSystemActionCoachingSettings",R,N,V_coachingSettings) coachingSettings;
@property (Td,N,V_popScale) popScale;
@property (Td,N,V_inflateScale) inflateScale;
```

## Class methods

```
+[SBSystemActionSettings settingsControllerModule];
```

## Instance methods

```
-[SBSystemActionSettings setDefaultValues];
-[SBSystemActionSettings previewSettings];
-[SBSystemActionSettings coachingSettings];
-[SBSystemActionSettings inflateScale];
-[SBSystemActionSettings popScale];
-[SBSystemActionSettings setInflateScale:];
-[SBSystemActionSettings setPopScale:];
```
