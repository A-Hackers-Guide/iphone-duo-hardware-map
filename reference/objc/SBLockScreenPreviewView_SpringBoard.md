# `SBLockScreenPreviewView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 14 instance variables, 0 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"UIView" _wallpaperView;
@"SBFLockScreenDateView" _dateView;
@"_UILegibilityLabel" _slideToUnlockLegibilityLabel;
@"UIStatusBar" _statusBar;
@"_UILegibilitySettings" _legibilitySettings;
@"SBWallpaperController" _wallpaperController;
@"SBUILegibilityView" _cameraView;
@"UILabel" _slideToUnlockView;
@"CSPageControl" _dashBoardPageControl;
@"SBUICallToActionLabel" _callToActionLabel;
@"SBUIProudLockIconView" _proudLockIconView;
@"CSQuickActionsView" _quickActionsView;
@"SBHomeGrabberView" _homeGrabberView;
@"SBFLockScreenDateViewController" _dateViewController;
```

## Instance methods

```
-[SBLockScreenPreviewView _setupPageControl];
-[SBLockScreenPreviewView _setupQuickActionView];
-[SBLockScreenPreviewView _statusBarReusePool];
-[SBLockScreenPreviewView _setupStatusBar];
-[SBLockScreenPreviewView dealloc];
-[SBLockScreenPreviewView _layoutQuickActionsView];
-[SBLockScreenPreviewView _layoutDateView];
-[SBLockScreenPreviewView layoutSubviews];
-[SBLockScreenPreviewView _setupCallToActionLabel];
-[SBLockScreenPreviewView _layoutStatusBar];
-[SBLockScreenPreviewView _layoutPageControl];
-[SBLockScreenPreviewView _layoutHomeGrabberView];
-[SBLockScreenPreviewView _setupWallpaperViewWithImage:];
-[SBLockScreenPreviewView _setupHomeGrabberView];
-[SBLockScreenPreviewView _setupDateViewWithOptions:];
-[SBLockScreenPreviewView _layoutProudLockIconView];
-[SBLockScreenPreviewView _layoutCallToActionLabel];
-[SBLockScreenPreviewView _layoutWallpaperView];
-[SBLockScreenPreviewView _setupProudLockIconView];
-[SBLockScreenPreviewView initWithFrame:wallpaperController:options:wallpaperImage:];
```
