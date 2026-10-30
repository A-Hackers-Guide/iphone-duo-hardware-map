# `SBActivityCoverSheetObserver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBActivityModalPresentationControllerDelegate`, `SBActivityObserver`
- 3 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"SBActivityModalPresentationController" _modalPresentationController;
q _environment;
@"SBActivityAlert" _activeAlert;
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
-[SBActivityCoverSheetObserver activityDidEnd:];
-[SBActivityCoverSheetObserver init];
-[SBActivityCoverSheetObserver _activityManager];
-[SBActivityCoverSheetObserver activityDidDismiss:];
-[SBActivityCoverSheetObserver presentAlert:];
-[SBActivityCoverSheetObserver activityDidStart:];
-[SBActivityCoverSheetObserver dismissAlert:];
-[SBActivityCoverSheetObserver activityDidUpdate:];
-[SBActivityCoverSheetObserver activityEnvironmentChanged:];
-[SBActivityCoverSheetObserver shouldHandleActivityItem:];
-[SBActivityCoverSheetObserver _dismissAlertForItem:];
-[SBActivityCoverSheetObserver activityDidExceedReducedPushBudget:];
-[SBActivityCoverSheetObserver activityWasBlocked:];
-[SBActivityCoverSheetObserver activityWasUnblocked:];
-[SBActivityCoverSheetObserver presentationController:bestIconViewForActivityIdentifier:];
```
