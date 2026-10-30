# `CAMHDRButton`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMExpandableMenuButton`
- Protocols: `CAMAccessibilityHUDImageProvider`
- 2 instance variables, 7 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"UIImageView" __glyphView;
@"NSArray" __allowedModes;
```

## Properties

```
@property (T@"UIImageView",R,N,V__glyphView) _glyphView;
@property (T@"NSArray",C,N,S_setAllowedModes:,V__allowedModes) _allowedModes;
@property (Tq,N) HDRMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMHDRButton headerView];
-[CAMHDRButton setHDRMode:];
-[CAMHDRButton initWithLayoutStyle:];
-[CAMHDRButton reloadData];
-[CAMHDRButton initWithFrame:];
-[CAMHDRButton HDRMode];
-[CAMHDRButton modeForIndex:];
-[CAMHDRButton titleForMenuItemAtIndex:];
-[CAMHDRButton _allowedModes];
-[CAMHDRButton _commonCAMHDRButtonInitialization];
-[CAMHDRButton _currentGlyphImageForAccessibilityHUD:];
-[CAMHDRButton _glyphView];
-[CAMHDRButton _setAllowedModes:];
-[CAMHDRButton _updateAllowedModes];
-[CAMHDRButton _updateCurrentGlyphImage];
-[CAMHDRButton imageForAccessibilityHUD];
-[CAMHDRButton indexForMode:];
-[CAMHDRButton numberOfMenuItems];
-[CAMHDRButton padHeaderViewContentInsetLeft];
-[CAMHDRButton prepareHeaderViewForExpanding:];
```
