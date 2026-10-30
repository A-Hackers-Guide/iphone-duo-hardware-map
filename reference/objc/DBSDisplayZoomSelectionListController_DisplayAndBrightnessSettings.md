# `DBSDisplayZoomSelectionListController`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSListController`
- Protocols: `DBSDisplayZoomTableViewCellDelegate`
- 2 instance variables, 6 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"<DBSDisplayZoomSelectionControllerDelegate>" _delegate;
Q _selectedDisplayZoomOption;
```

## Properties

```
@property (TQ,N,V_selectedDisplayZoomOption) selectedDisplayZoomOption;
@property (T@"<DBSDisplayZoomSelectionControllerDelegate>",&,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DBSDisplayZoomSelectionListController tableView:cellForRowAtIndexPath:];
-[DBSDisplayZoomSelectionListController tableView:didEndDisplayingCell:forRowAtIndexPath:];
-[DBSDisplayZoomSelectionListController viewDidLoad];
-[DBSDisplayZoomSelectionListController tableView:willDisplayCell:forRowAtIndexPath:];
-[DBSDisplayZoomSelectionListController setDelegate:];
-[DBSDisplayZoomSelectionListController viewDidAppear:];
-[DBSDisplayZoomSelectionListController delegate];
-[DBSDisplayZoomSelectionListController preferredContentSize];
-[DBSDisplayZoomSelectionListController specifiers];
-[DBSDisplayZoomSelectionListController userDidTapDone:];
-[DBSDisplayZoomSelectionListController _updateNavigationButtonStateWithNewOption:];
-[DBSDisplayZoomSelectionListController _userDidConfirmDisplayZoomModeWithSpecifier:];
-[DBSDisplayZoomSelectionListController confirmationDictForCurrentSelectedScale];
-[DBSDisplayZoomSelectionListController displayZoomTableViewCell:userDidTapOnDisplayZoomOption:];
-[DBSDisplayZoomSelectionListController displayZoomTableViewCellCurrentlySelectedDisplayZoomOption:];
-[DBSDisplayZoomSelectionListController selectedDisplayZoomOption];
-[DBSDisplayZoomSelectionListController setSelectedDisplayZoomOption:];
-[DBSDisplayZoomSelectionListController supportedDisplayZoomOptions];
-[DBSDisplayZoomSelectionListController updateNavigationButtonStateWithCurrentState];
-[DBSDisplayZoomSelectionListController userDidTapCancel:];
```
