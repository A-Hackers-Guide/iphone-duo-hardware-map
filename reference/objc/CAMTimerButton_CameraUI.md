# `CAMTimerButton`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMExpandableMenuButton`
- Protocols: `CAMAccessibilityHUDImageProvider`
- 3 instance variables, 8 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _hideOffWhenCollapsed;
@"<CAMTimerButtonDelegate>" _delegate;
@"UIImageView" __glyphView;
```

## Properties

```
@property (T@"UIImageView",R,N,V__glyphView) _glyphView;
@property (T@"<CAMTimerButtonDelegate>",W,N,V_delegate) delegate;
@property (Tq,N) duration;
@property (TB,N,V_hideOffWhenCollapsed) hideOffWhenCollapsed;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMTimerButton headerView];
-[CAMTimerButton initWithLayoutStyle:];
-[CAMTimerButton duration];
-[CAMTimerButton reloadData];
-[CAMTimerButton setDelegate:];
-[CAMTimerButton delegate];
-[CAMTimerButton setDuration:];
-[CAMTimerButton initWithFrame:];
-[CAMTimerButton setDuration:animated:];
-[CAMTimerButton titleForMenuItemAtIndex:];
-[CAMTimerButton _commonCAMTimerButtonInitialization];
-[CAMTimerButton _currentGlyphImageForAccessibiliyHUD:];
-[CAMTimerButton _glyphView];
-[CAMTimerButton _updateCurrentGlyphImage];
-[CAMTimerButton hideOffWhenCollapsed];
-[CAMTimerButton imageForAccessibilityHUD];
-[CAMTimerButton numberOfMenuItems];
-[CAMTimerButton padHeaderViewContentInsetLeft];
-[CAMTimerButton setHideOffWhenCollapsed:];
-[CAMTimerButton setHideOffWhenCollapsed:needsReloadData:];
-[CAMTimerButton shownIndexesWhileCollapsed];
```
