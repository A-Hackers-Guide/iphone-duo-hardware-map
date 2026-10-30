# `_UIDisplayInfoProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIDisplayInfoProviding`
- 10 instance variables, 14 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"FBSDisplayConfiguration" displayConfiguration;
Q artworkSubtype;
d homeAffordanceOverlayAllowance;
d systemMinimumMargin;
@"<_UIDisplayInfoShape>" exclusionArea;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} peripheryInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} safeAreaInsetsPortrait;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} safeAreaInsetsLandscapeLeft;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} safeAreaInsetsLandscapeRight;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} safeAreaInsetsPortraitUpsideDown;
```

## Properties

```
@property (T@"FBSDisplayConfiguration",R,N,VdisplayConfiguration) displayConfiguration;
@property (TQ,R,N,VartworkSubtype) artworkSubtype;
@property (T{UIEdgeInsets=dddd},R,N,VperipheryInsets) peripheryInsets;
@property (Td,R,N,VsystemMinimumMargin) systemMinimumMargin;
@property (T{UIEdgeInsets=dddd},R,N,VsafeAreaInsetsPortrait) safeAreaInsetsPortrait;
@property (Td,R,N,VhomeAffordanceOverlayAllowance) homeAffordanceOverlayAllowance;
@property (T@"<_UIDisplayInfoShape>",R,N,VexclusionArea) exclusionArea;
@property (T{UIEdgeInsets=dddd},R,N,VsafeAreaInsetsLandscapeLeft) safeAreaInsetsLandscapeLeft;
@property (T{UIEdgeInsets=dddd},R,N,VsafeAreaInsetsPortraitUpsideDown) safeAreaInsetsPortraitUpsideDown;
@property (T{UIEdgeInsets=dddd},R,N,VsafeAreaInsetsLandscapeRight) safeAreaInsetsLandscapeRight;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDisplayInfoProvider peripheryInsets];
-[_UIDisplayInfoProvider displayConfiguration];
-[_UIDisplayInfoProvider artworkSubtype];
-[_UIDisplayInfoProvider exclusionArea];
-[_UIDisplayInfoProvider homeAffordanceOverlayAllowance];
-[_UIDisplayInfoProvider safeAreaInsetsLandscapeLeft];
-[_UIDisplayInfoProvider safeAreaInsetsLandscapeRight];
-[_UIDisplayInfoProvider safeAreaInsetsPortrait];
-[_UIDisplayInfoProvider safeAreaInsetsPortraitUpsideDown];
-[_UIDisplayInfoProvider systemMinimumMargin];
```
