# `SBSafeAreaResolverUtility`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 7 instance methods, 7 class methods

## Class methods

```
+[SBSafeAreaResolverUtility _bucketedSizeForSize:screenType:axis:includingStatusBar:];
+[SBSafeAreaResolverUtility _bucketingDetentsForScreenType:axis:statusBarHidden:];
+[SBSafeAreaResolverUtility _impliedInterfaceOrientationForOcclusionFrame:inReferenceBounds:screenType:];
+[SBSafeAreaResolverUtility _impliedStatusBarAxisForTopRightOcclusion:inReferenceBounds:screenType:requestedAxis:];
+[SBSafeAreaResolverUtility effectiveScreenTypeForApplication:windowScene:];
+[SBSafeAreaResolverUtility statusBarOcclusionRectForWindowScene:interfaceOrientation:screenType:statusBarHidden:statusBarAxis:inReferenceSpace:];
+[SBSafeAreaResolverUtility statusBarOcclusionSizeForWindowScene:interfaceOrientation:screenType:statusBarHidden:statusBarAxis:];
```

## Instance methods

```
-[SBSafeAreaResolverUtility _safeAreaInsetsForInterfaceOrientation:isPhone:portraitSafeAreaInsets:statusBarInsets:homeAffordanceOverlayAllowance:];
-[SBSafeAreaResolverUtility _windowControlsLayoutForApplicationFrame:screenBounds:application:switcherController:displayEdgeInfo:statusBarHidden:preferredWindowControlsPlacement:];
-[SBSafeAreaResolverUtility reevaluateSafeAreaSettingsForSettings:scene:windowScene:application:preferredWindowControlsPlacement:preferredSafeAreaSettings:displayEdgeInfo:suppressesStatusBarSafeArea:];
-[SBSafeAreaResolverUtility safeAreaCornerInsetResolverForApplicationFrame:screenBounds:isNonFullScreenWindowInFullScreenAppsMode:isFlexibleWindowingEnabled:windowControlsLayout:supportsSolariumSafeAreas:preferredSafeAreaSettings:isInSplitPIP:isClassic:];
-[SBSafeAreaResolverUtility safeAreaCornerInsetResolverWithBucketedAvoidanceDetentsForScreenType:windowScene:suppressesStatusBarSafeArea:suppressVerticalAxisWhereDisfavored:supportsVerticalBar:];
-[SBSafeAreaResolverUtility safeAreaEdgeInsetResolverForApplicationFrame:screenBounds:activationSettings:isNonFullScreenWindowInFullScreenAppsMode:displayEdgeInfo:screenType:isClassic:supportsSolariumSafeAreas:isFlexibleWindowingEnabled:windowControlsLayout:isInSplitPIP:suppressesStatusBarSafeArea:supportsVerticalBar:];
-[SBSafeAreaResolverUtility supportsSolariumSafeAreasRegardlessOfWindowingModeForApplication:switcherController:];
```
