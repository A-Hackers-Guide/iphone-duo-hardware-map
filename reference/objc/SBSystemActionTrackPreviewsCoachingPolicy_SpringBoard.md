# `SBSystemActionTrackPreviewsCoachingPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemActionCoachingPolicy`
- 2 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"SBSystemActionTrackPreviewsCoachingPolicySettings" _settings;
@"NSMapTable" _trackedPreviewsByAction;
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
-[SBSystemActionTrackPreviewsCoachingPolicy init];
-[SBSystemActionTrackPreviewsCoachingPolicy noteDidBeginPreview:forAction:];
-[SBSystemActionTrackPreviewsCoachingPolicy noteDidEndPreview:forAction:];
-[SBSystemActionTrackPreviewsCoachingPolicy noteDidInvalidateExpansionOfPreview:forAction:withResult:];
-[SBSystemActionTrackPreviewsCoachingPolicy wantsCoachingDismissedForAction:];
-[SBSystemActionTrackPreviewsCoachingPolicy wantsCoachingPresentedForAction:];
```
