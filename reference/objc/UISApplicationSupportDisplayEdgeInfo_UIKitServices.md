# `UISApplicationSupportDisplayEdgeInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`, `NSCopying`
- 8 instance variables, 11 properties, 20 instance methods, 2 class methods

## Instance variables

```
(?="asInt"Q"flags"{?="assertOnMutationAttempt"b1}) _infoFlags;
@"UISApplicationSupportDisplayEdgeInsetsWrapper" _peripheryInsets;
@"NSNumber" _systemMinimumMargin;
@"NSNumber" _homeAffordanceOverlayAllowance;
@"UISApplicationSupportDisplayEdgeInsetsWrapper" _safeAreaInsetsPortrait;
@"UISApplicationSupportDisplayEdgeInsetsWrapper" _safeAreaInsetsLandscapeLeft;
@"UISApplicationSupportDisplayEdgeInsetsWrapper" _safeAreaInsetsPortraitUpsideDown;
@"UISApplicationSupportDisplayEdgeInsetsWrapper" _safeAreaInsetsLandscapeRight;
```

## Properties

```
@property (T@"UISApplicationSupportDisplayEdgeInsetsWrapper",&,N,V_peripheryInsets) peripheryInsets;
@property (T@"NSNumber",&,N,V_systemMinimumMargin) systemMinimumMargin;
@property (T@"NSNumber",&,N,V_homeAffordanceOverlayAllowance) homeAffordanceOverlayAllowance;
@property (T@"UISApplicationSupportDisplayEdgeInsetsWrapper",&,N,V_safeAreaInsetsPortrait) safeAreaInsetsPortrait;
@property (T@"UISApplicationSupportDisplayEdgeInsetsWrapper",&,N,V_safeAreaInsetsLandscapeLeft) safeAreaInsetsLandscapeLeft;
@property (T@"UISApplicationSupportDisplayEdgeInsetsWrapper",&,N,V_safeAreaInsetsPortraitUpsideDown) safeAreaInsetsPortraitUpsideDown;
@property (T@"UISApplicationSupportDisplayEdgeInsetsWrapper",&,N,V_safeAreaInsetsLandscapeRight) safeAreaInsetsLandscapeRight;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISApplicationSupportDisplayEdgeInfo defaultDisplayEdgeInfoForceInsets:];
+[UISApplicationSupportDisplayEdgeInfo defaultDisplayEdgeInfo];
```

## Instance methods

```
-[UISApplicationSupportDisplayEdgeInfo peripheryInsets];
-[UISApplicationSupportDisplayEdgeInfo initWithXPCDictionary:];
-[UISApplicationSupportDisplayEdgeInfo encodeWithXPCDictionary:];
-[UISApplicationSupportDisplayEdgeInfo description];
-[UISApplicationSupportDisplayEdgeInfo copyWithZone:];
-[UISApplicationSupportDisplayEdgeInfo setSafeAreaInsetsLandscapeLeft:];
-[UISApplicationSupportDisplayEdgeInfo homeAffordanceOverlayAllowance];
-[UISApplicationSupportDisplayEdgeInfo safeAreaInsetsLandscapeLeft];
-[UISApplicationSupportDisplayEdgeInfo safeAreaInsetsLandscapeRight];
-[UISApplicationSupportDisplayEdgeInfo safeAreaInsetsPortrait];
-[UISApplicationSupportDisplayEdgeInfo safeAreaInsetsPortraitUpsideDown];
-[UISApplicationSupportDisplayEdgeInfo setHomeAffordanceOverlayAllowance:];
-[UISApplicationSupportDisplayEdgeInfo setPeripheryInsets:];
-[UISApplicationSupportDisplayEdgeInfo setSafeAreaInsetsLandscapeRight:];
-[UISApplicationSupportDisplayEdgeInfo setSafeAreaInsetsPortrait:];
-[UISApplicationSupportDisplayEdgeInfo setSafeAreaInsetsPortraitUpsideDown:];
-[UISApplicationSupportDisplayEdgeInfo setSystemMinimumMargin:];
-[UISApplicationSupportDisplayEdgeInfo systemMinimumMargin];
-[UISApplicationSupportDisplayEdgeInfo _copyFromOtherInfo:];
-[UISApplicationSupportDisplayEdgeInfo _performIvarUpdateIfAllowed:];
```
