# `CAMBadgeTray`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CEKBadgeViewDelegate`
- 4 instance variables, 15 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _wantsLargerBadge;
@"<CAMBadgeTrayDelegate>" _delegate;
Q _visibleBadges;
@"NSMutableDictionary" __badgeMap;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V__badgeMap) _badgeMap;
@property (T@"<CAMBadgeTrayDelegate>",W,N,V_delegate) delegate;
@property (TQ,N,V_visibleBadges) visibleBadges;
@property (T@"CAMTextBadge",R,N) controlChangeBadge;
@property (T@"CAMFocusLockBadge",R,N) focusLockBadge;
@property (T@"CAMElapsedTimeView",R,N) elapsedTimeView;
@property (T@"CAMVideoStabilizationBadge",R,N) videoStabilizationBadge;
@property (T@"CAMVideoPausedBadge",R,N) videoPausedBadge;
@property (T@"CAMSpatialBadge",R,N) spatialBadge;
@property (T@"CAMTextBadge",R,N) batteryStressBadge;
@property (TB,N,V_wantsLargerBadge) wantsLargerBadge;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMBadgeTray videoStabilizationBadge];
-[CAMBadgeTray focusLockBadge];
-[CAMBadgeTray setVisibleBadges:animated:];
-[CAMBadgeTray badgeViewDidChangeIntrinsicContentSize:];
-[CAMBadgeTray elapsedTimeView];
-[CAMBadgeTray _createControlForType:];
-[CAMBadgeTray _forBadgeTypeInBadgeTypes:do:];
-[CAMBadgeTray layoutSubviews];
-[CAMBadgeTray hitTest:withEvent:];
-[CAMBadgeTray controlChangeBadge];
-[CAMBadgeTray _loadBadgesIfNeededForTypes:initialAlpha:];
-[CAMBadgeTray setDelegate:];
-[CAMBadgeTray spatialBadge];
-[CAMBadgeTray videoPausedBadge];
-[CAMBadgeTray visibleBadges];
-[CAMBadgeTray delegate];
-[CAMBadgeTray _updateBadgesVisibilityForVisibleBadges:];
-[CAMBadgeTray createBadgesIfNecessary:];
-[CAMBadgeTray wantsLargerBadge];
-[CAMBadgeTray _badgeMap];
-[CAMBadgeTray setWantsLargerBadge:];
-[CAMBadgeTray initWithFrame:];
-[CAMBadgeTray batteryStressBadge];
-[CAMBadgeTray _layoutBadges:withVisibleBadges:];
-[CAMBadgeTray setVisibleBadges:];
```
