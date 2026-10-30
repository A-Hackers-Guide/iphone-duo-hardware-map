# `SBSystemApertureCaptureVisibilityShimViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFTouchPassThroughViewController`
- 8 instance variables, 3 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"SBSystemApertureSettings" _settings;
@"UIViewController" _contentViewController;
@"_UIPortalView" _displayPortalView;
@"_UIPortalView" _clonedDisplayPortalView;
@"CADisplay" _observedDisplay;
B _visibleOnClonedDisplay;
B _visibleInSnapshots;
B _contentsDifferOnClonedDisplay;
```

## Properties

```
@property (TB,N,GisVisibleOnClonedDisplay,V_visibleOnClonedDisplay) visibleOnClonedDisplay;
@property (TB,N,GisVisibleInSnapshots,V_visibleInSnapshots) visibleInSnapshots;
@property (TB,N,GdoContentsDifferOnClonedDisplay,V_contentsDifferOnClonedDisplay) contentsDifferOnClonedDisplay;
```

## Instance methods

```
-[SBSystemApertureCaptureVisibilityShimViewController setContentsDifferOnClonedDisplay:];
-[SBSystemApertureCaptureVisibilityShimViewController isVisibleInSnapshots];
-[SBSystemApertureCaptureVisibilityShimViewController _isOriginalContentCloned];
-[SBSystemApertureCaptureVisibilityShimViewController observeValueForKeyPath:ofObject:change:context:];
-[SBSystemApertureCaptureVisibilityShimViewController setVisibleOnClonedDisplay:];
-[SBSystemApertureCaptureVisibilityShimViewController supportedInterfaceOrientations];
-[SBSystemApertureCaptureVisibilityShimViewController dealloc];
-[SBSystemApertureCaptureVisibilityShimViewController _updateClonedVisibility];
-[SBSystemApertureCaptureVisibilityShimViewController doContentsDifferOnClonedDisplay];
-[SBSystemApertureCaptureVisibilityShimViewController setVisibleInSnapshots:];
-[SBSystemApertureCaptureVisibilityShimViewController viewDidLoad];
-[SBSystemApertureCaptureVisibilityShimViewController newDefaultVisibilityAnimator];
-[SBSystemApertureCaptureVisibilityShimViewController _canShowWhileLocked];
-[SBSystemApertureCaptureVisibilityShimViewController initWithContentViewController:];
-[SBSystemApertureCaptureVisibilityShimViewController isVisibleOnClonedDisplay];
-[SBSystemApertureCaptureVisibilityShimViewController _updatePortalVisibility];
-[SBSystemApertureCaptureVisibilityShimViewController _updateSnapshotVisibility];
```
