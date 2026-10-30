# `VTUIVoiceSelectionOptionsView`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UICollectionViewDelegate`, `UITableViewDelegate`, `UITableViewDelegatePrivate`, `SUICVoiceSelectionDisplaying`
- 5 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"UITableView" _voicesTableView;
@"SUICVoiceSelectionViewModel" _viewModel;
@"UITableViewDiffableDataSource" _tableViewDataSource;
@"<SUICVoiceSelectionViewModelProviding>" _voiceSelectionViewModelProvider;
@"<SUICVoiceSelectionEventHandling>" _voiceSelectionEventHandler;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SUICVoiceSelectionViewModelProviding>",W,N,V_voiceSelectionViewModelProvider) voiceSelectionViewModelProvider;
@property (T@"<SUICVoiceSelectionEventHandling>",W,N,V_voiceSelectionEventHandler) voiceSelectionEventHandler;
```

## Instance methods

```
-[VTUIVoiceSelectionOptionsView tableView:shouldDrawBottomSeparatorForSection:];
-[VTUIVoiceSelectionOptionsView init];
-[VTUIVoiceSelectionOptionsView setSemanticContentAttribute:];
-[VTUIVoiceSelectionOptionsView sizeThatFits:];
-[VTUIVoiceSelectionOptionsView tableView:shouldDrawTopSeparatorForSection:];
-[VTUIVoiceSelectionOptionsView tableView:didSelectRowAtIndexPath:];
-[VTUIVoiceSelectionOptionsView _tableCellForVoiceViewModel:indexPath:];
-[VTUIVoiceSelectionOptionsView setVoiceSelectionEventHandler:];
-[VTUIVoiceSelectionOptionsView setVoiceSelectionViewModelProvider:];
-[VTUIVoiceSelectionOptionsView voiceSelectionViewModelDidChange];
-[VTUIVoiceSelectionOptionsView voiceSelectionViewModelProvider];
-[VTUIVoiceSelectionOptionsView voiceSelectionEventHandler];
-[VTUIVoiceSelectionOptionsView _cellSizeForSize:];
-[VTUIVoiceSelectionOptionsView _createAndApplySnapshotForViewModel:];
-[VTUIVoiceSelectionOptionsView _diffableTableDataSource];
-[VTUIVoiceSelectionOptionsView _setupVoicesTableView];
```
