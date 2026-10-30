# `SBAppClipOverlayCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _overlayViewControllers;
@"NSMapTable" _participantForViewController;
```

## Instance methods

```
-[SBAppClipOverlayCoordinator init];
-[SBAppClipOverlayCoordinator _existingOverlayViewControllerForWebClipIdentifier:];
-[SBAppClipOverlayCoordinator overlayViewControllerForBundleIdentifier:webClipIdentifier:participant:];
-[SBAppClipOverlayCoordinator participant:didSurrenderViewController:];
```
