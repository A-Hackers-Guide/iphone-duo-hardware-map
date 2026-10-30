# `CAMFlashButton`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMExpandableMenuButton`
- Protocols: `CAMAccessibilityHUDImageProvider`
- 4 instance variables, 9 properties, 26 instance methods, 0 class methods

## Instance variables

```
B _allowsAutomaticFlash;
B _unavailable;
@"UIImageView" __glyphView;
@"UIImageView" __warningIndicatorView;
```

## Properties

```
@property (T@"UIImageView",R,N,V__glyphView) _glyphView;
@property (T@"UIImageView",R,N,V__warningIndicatorView) _warningIndicatorView;
@property (Tq,N) flashMode;
@property (TB,N,V_allowsAutomaticFlash) allowsAutomaticFlash;
@property (TB,N,GisUnavailable,V_unavailable) unavailable;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMFlashButton headerView];
-[CAMFlashButton initWithLayoutStyle:];
-[CAMFlashButton reloadData];
-[CAMFlashButton setFlashMode:];
-[CAMFlashButton flashMode];
-[CAMFlashButton initWithFrame:];
-[CAMFlashButton setUnavailable:];
-[CAMFlashButton isUnavailable];
-[CAMFlashButton modeForIndex:];
-[CAMFlashButton titleForMenuItemAtIndex:];
-[CAMFlashButton _commonCAMFlashButtonInitialization];
-[CAMFlashButton _currentGlyphImageForAccessibilityHUD:];
-[CAMFlashButton _glyphView];
-[CAMFlashButton _updateCurrentGlyphImage];
-[CAMFlashButton _warningIndicatorView];
-[CAMFlashButton allowsAutomaticFlash];
-[CAMFlashButton collapsedSelectedLabelHorizontalMargin];
-[CAMFlashButton imageForAccessibilityHUD];
-[CAMFlashButton indexForMode:];
-[CAMFlashButton numberOfMenuItems];
-[CAMFlashButton padHeaderViewContentInsetLeft];
-[CAMFlashButton prepareHeaderViewForExpanding:];
-[CAMFlashButton setAllowsAutomaticFlash:];
-[CAMFlashButton setAllowsAutomaticFlash:needsReloadData:];
-[CAMFlashButton shouldIgnoreMenuInteraction];
-[CAMFlashButton wantsSelectedItemToBeVisible];
```
