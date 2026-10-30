# `SBSystemActionPressWithinTimeIntervalCoachingPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemActionCoachingPolicy`
- 4 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"SBSystemActionPressWithinTimeIntervalCoachingPolicySettings" _settings;
@"NSCountedSet" _countedActions;
@"NSMapTable" _latestPreviewsByAction;
@"NSTimer" _resetTimer;
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
-[SBSystemActionPressWithinTimeIntervalCoachingPolicy init];
-[SBSystemActionPressWithinTimeIntervalCoachingPolicy noteDidBeginPreview:forAction:];
-[SBSystemActionPressWithinTimeIntervalCoachingPolicy noteDidEndPreview:forAction:];
-[SBSystemActionPressWithinTimeIntervalCoachingPolicy noteDidInvalidateExpansionOfPreview:forAction:withResult:];
-[SBSystemActionPressWithinTimeIntervalCoachingPolicy wantsCoachingDismissedForAction:];
-[SBSystemActionPressWithinTimeIntervalCoachingPolicy wantsCoachingPresentedForAction:];
```
