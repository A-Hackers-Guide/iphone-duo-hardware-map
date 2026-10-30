# `SBModifierTimelineDetailViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UITableViewDelegate`, `UITableViewDataSource`
- 4 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"UITableView" _tableView;
@"SBModifierTimelineModifierDetailViewController" _modifierDetailViewController;
@"SBModifierTimelineTextDetailViewController" _textDetailViewController;
@"SBSwitcherModifierTimelineEntry" _entry;
```

## Properties

```
@property (T@"SBSwitcherModifierTimelineEntry",&,N,V_entry) entry;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBModifierTimelineDetailViewController tableView:numberOfRowsInSection:];
-[SBModifierTimelineDetailViewController numberOfSectionsInTableView:];
-[SBModifierTimelineDetailViewController tableView:cellForRowAtIndexPath:];
-[SBModifierTimelineDetailViewController tableView:titleForHeaderInSection:];
-[SBModifierTimelineDetailViewController viewDidLoad];
-[SBModifierTimelineDetailViewController tableView:didSelectRowAtIndexPath:];
-[SBModifierTimelineDetailViewController viewWillLayoutSubviews];
-[SBModifierTimelineDetailViewController entry];
-[SBModifierTimelineDetailViewController setEntry:];
-[SBModifierTimelineDetailViewController _done];
-[SBModifierTimelineDetailViewController _numberOfModifiersInStackSnapshot:];
-[SBModifierTimelineDetailViewController _prettyStringForEventPredicateDetails:];
-[SBModifierTimelineDetailViewController _stackSnapshotAtIndex:];
```
