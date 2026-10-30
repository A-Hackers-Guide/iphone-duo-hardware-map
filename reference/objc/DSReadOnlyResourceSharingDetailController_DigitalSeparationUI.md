# `DSReadOnlyResourceSharingDetailController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSTableWelcomeController`
- Protocols: `DSController`
- 8 instance variables, 12 properties, 24 instance methods, 4 class methods

## Instance variables

```
B _isFinishedReviewing;
@"<DSNavigationDelegate>" _delegate;
@"DSSharingType" _sharingType;
@"DSSharingPerson" _sharingPerson;
@"<DSReadOnlyResourceSharingDetailDelegate>" _detailDelegate;
@"NSArray" _remainingSharingTypes;
@"NSArray" _remainingSharingPeople;
@"UIViewController" _startingViewController;
```

## Properties

```
@property (T@"DSSharingType",&,N,V_sharingType) sharingType;
@property (T@"DSSharingPerson",&,N,V_sharingPerson) sharingPerson;
@property (T@"<DSReadOnlyResourceSharingDetailDelegate>",&,N,V_detailDelegate) detailDelegate;
@property (T@"NSArray",&,N,V_remainingSharingTypes) remainingSharingTypes;
@property (T@"NSArray",&,N,V_remainingSharingPeople) remainingSharingPeople;
@property (T@"UIViewController",&,N,V_startingViewController) startingViewController;
@property (TB,N,V_isFinishedReviewing) isFinishedReviewing;
@property (T@"<DSNavigationDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DSReadOnlyResourceSharingDetailController initialize];
+[DSReadOnlyResourceSharingDetailController _removeDisplayedFromArray:];
+[DSReadOnlyResourceSharingDetailController initWithSharingPeople:startingViewController:delegate:];
+[DSReadOnlyResourceSharingDetailController initWithSharingTypes:startingViewController:delegate:];
```

## Instance methods

```
-[DSReadOnlyResourceSharingDetailController tableView:numberOfRowsInSection:];
-[DSReadOnlyResourceSharingDetailController tableView:editingStyleForRowAtIndexPath:];
-[DSReadOnlyResourceSharingDetailController tableView:cellForRowAtIndexPath:];
-[DSReadOnlyResourceSharingDetailController viewDidLoad];
-[DSReadOnlyResourceSharingDetailController setDelegate:];
-[DSReadOnlyResourceSharingDetailController _removeFromView];
-[DSReadOnlyResourceSharingDetailController delegate];
-[DSReadOnlyResourceSharingDetailController detailDelegate];
-[DSReadOnlyResourceSharingDetailController setDetailDelegate:];
-[DSReadOnlyResourceSharingDetailController setStartingViewController:];
-[DSReadOnlyResourceSharingDetailController startingViewController];
-[DSReadOnlyResourceSharingDetailController setSharingType:];
-[DSReadOnlyResourceSharingDetailController sharingType];
-[DSReadOnlyResourceSharingDetailController _finishReviewingReadOnlySharing];
-[DSReadOnlyResourceSharingDetailController _learnMorePressed];
-[DSReadOnlyResourceSharingDetailController _pushNextPane];
-[DSReadOnlyResourceSharingDetailController isFinishedReviewing];
-[DSReadOnlyResourceSharingDetailController remainingSharingPeople];
-[DSReadOnlyResourceSharingDetailController remainingSharingTypes];
-[DSReadOnlyResourceSharingDetailController setIsFinishedReviewing:];
-[DSReadOnlyResourceSharingDetailController setRemainingSharingPeople:];
-[DSReadOnlyResourceSharingDetailController setRemainingSharingTypes:];
-[DSReadOnlyResourceSharingDetailController setSharingPerson:];
-[DSReadOnlyResourceSharingDetailController sharingPerson];
```
