# `SBProductivityGestureEducationController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBProductivityGestureEducationPillViewControllerDelegate`
- 4 instance variables, 4 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"<BNPosting>" _bannerPoster;
@"NSDictionary" _educationItemMap;
@"BSAbsoluteMachTimer" _bannerDismissTimer;
@"SBProductivityGestureEducationPillViewController" _educationPillViewController;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBProductivityGestureEducationController dealloc];
-[SBProductivityGestureEducationController _dismissBanner:];
-[SBProductivityGestureEducationController _itemMapUpdated];
-[SBProductivityGestureEducationController _dismissBannerTimerWithInterval:reason:];
-[SBProductivityGestureEducationController _invalidateBannerTimer];
-[SBProductivityGestureEducationController _itemTypeForType:];
-[SBProductivityGestureEducationController _loadItemMap];
-[SBProductivityGestureEducationController _presentBannerWithEducationItem:];
-[SBProductivityGestureEducationController _resetPillViewController:];
-[SBProductivityGestureEducationController gestureActivatedForType:];
-[SBProductivityGestureEducationController gestureEducationPillViewControllerDidDisappear:];
-[SBProductivityGestureEducationController gestureEducationPillViewControllerDidReceiveUserTap:];
-[SBProductivityGestureEducationController gestureEducationPillViewControllerFailsToAppear:];
-[SBProductivityGestureEducationController gestureEducationPillViewControllerMarqueeStarted:duration:];
-[SBProductivityGestureEducationController gestureEducationPillViewControllerWillAppear:];
-[SBProductivityGestureEducationController initWithBannerPoster:];
```
