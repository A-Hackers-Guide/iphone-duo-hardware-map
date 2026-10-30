# `CAMLivePhotoButton`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMExpandableMenuButton`
- Protocols: `CAMAccessibilityHUDImageProvider`
- 2 instance variables, 7 properties, 22 instance methods, 1 class methods

## Instance variables

```
B _allowsAutomaticMode;
@"CAMLivePhotoBloomView" __bloomView;
```

## Properties

```
@property (T@"CAMLivePhotoBloomView",R,N,V__bloomView) _bloomView;
@property (Tq,N) livePhotoMode;
@property (TB,N,V_allowsAutomaticMode) allowsAutomaticMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAMLivePhotoButton enablingAnimationDuration];
```

## Instance methods

```
-[CAMLivePhotoButton livePhotoMode];
-[CAMLivePhotoButton headerView];
-[CAMLivePhotoButton initWithLayoutStyle:];
-[CAMLivePhotoButton reloadData];
-[CAMLivePhotoButton setLivePhotoMode:];
-[CAMLivePhotoButton setSelectedIndex:];
-[CAMLivePhotoButton _updateBaseImage];
-[CAMLivePhotoButton modeForIndex:];
-[CAMLivePhotoButton titleForMenuItemAtIndex:];
-[CAMLivePhotoButton _availableModes];
-[CAMLivePhotoButton _bloomView];
-[CAMLivePhotoButton _currentBaseImage];
-[CAMLivePhotoButton allowsAutomaticMode];
-[CAMLivePhotoButton finishExpansionAnimated:];
-[CAMLivePhotoButton imageForAccessibilityHUD];
-[CAMLivePhotoButton indexForMode:];
-[CAMLivePhotoButton interruptEnablingAnimation];
-[CAMLivePhotoButton numberOfMenuItems];
-[CAMLivePhotoButton performEnablingAnimation];
-[CAMLivePhotoButton prepareHeaderViewForExpanding:];
-[CAMLivePhotoButton setAllowsAutomaticMode:];
-[CAMLivePhotoButton setAllowsAutomaticMode:needsReloadData:];
```
