# `PKTextInputDebugRadarViewController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UICollectionViewDataSource`, `PKTextInputDebugRadarEntryCellDelegate`
- 10 instance variables, 14 properties, 48 instance methods, 0 class methods

## Instance variables

```
B __includeSysdiagnose;
@"PKTextInputDebugSharpenerLog" _sharpenerLog;
@"<PKTextInputDebugRadarViewControllerDelegate>" _delegate;
@"UISegmentedControl" __contextDetailControl;
@"UIBarButtonItem" __submitButton;
@"UICollectionView" __entriesCollectionView;
d __keyboardVerticalOverlap;
@"UIButton" __sysdiagnoseButton;
@"NSMutableArray" __intendedTexts;
@"NSMutableIndexSet" __includedEntryIndexes;
```

## Properties

```
@property (T@"UISegmentedControl",&,N,V__contextDetailControl) _contextDetailControl;
@property (T@"UIBarButtonItem",&,N,V__submitButton) _submitButton;
@property (T@"UICollectionView",&,N,V__entriesCollectionView) _entriesCollectionView;
@property (Td,N,S_setKeyboardVerticalOverlap:,V__keyboardVerticalOverlap) _keyboardVerticalOverlap;
@property (T@"UIButton",&,N,V__sysdiagnoseButton) _sysdiagnoseButton;
@property (T@"NSMutableArray",&,N,V__intendedTexts) _intendedTexts;
@property (T@"NSMutableIndexSet",&,N,V__includedEntryIndexes) _includedEntryIndexes;
@property (TB,N,V__includeSysdiagnose) _includeSysdiagnose;
@property (T@"PKTextInputDebugSharpenerLog",R,N,V_sharpenerLog) sharpenerLog;
@property (T@"<PKTextInputDebugRadarViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKTextInputDebugRadarViewController _dismiss];
-[PKTextInputDebugRadarViewController _setupViews];
-[PKTextInputDebugRadarViewController collectionView:numberOfItemsInSection:];
-[PKTextInputDebugRadarViewController collectionView:cellForItemAtIndexPath:];
-[PKTextInputDebugRadarViewController viewDidLoad];
-[PKTextInputDebugRadarViewController _canShowWhileLocked];
-[PKTextInputDebugRadarViewController setDelegate:];
-[PKTextInputDebugRadarViewController viewDidAppear:];
-[PKTextInputDebugRadarViewController delegate];
-[PKTextInputDebugRadarViewController _handleCancelButton:];
-[PKTextInputDebugRadarViewController _updateScrollView];
-[PKTextInputDebugRadarViewController entryCellIntendedTextDidChange:];
-[PKTextInputDebugRadarViewController _accumulatedLogEntryTextsForRadar];
-[PKTextInputDebugRadarViewController _buildString];
-[PKTextInputDebugRadarViewController _configureCell:atIndexPath:];
-[PKTextInputDebugRadarViewController _contextDetailControl];
-[PKTextInputDebugRadarViewController _deviceString];
-[PKTextInputDebugRadarViewController _entriesCollectionView];
-[PKTextInputDebugRadarViewController _generateLaunchURLWithLogFilename:];
-[PKTextInputDebugRadarViewController _handleDetailControlChanged:];
-[PKTextInputDebugRadarViewController _handleKeyboardWillHide:];
-[PKTextInputDebugRadarViewController _handleKeyboardWillShow:];
-[PKTextInputDebugRadarViewController _handleSubmitRadarButton:];
-[PKTextInputDebugRadarViewController _includeSysdiagnose];
-[PKTextInputDebugRadarViewController _includedEntryIndexes];
-[PKTextInputDebugRadarViewController _intendedTexts];
-[PKTextInputDebugRadarViewController _keyboardVerticalOverlap];
-[PKTextInputDebugRadarViewController _launchTTRAndDismiss];
-[PKTextInputDebugRadarViewController _loadIntendedTexts];
-[PKTextInputDebugRadarViewController _logEntryTextForRadarTitle];
-[PKTextInputDebugRadarViewController _loggedMainLocaleDescription];
-[PKTextInputDebugRadarViewController _selectedContentLevel];
-[PKTextInputDebugRadarViewController _setKeyboardVerticalOverlap:];
-[PKTextInputDebugRadarViewController _submitButton];
-[PKTextInputDebugRadarViewController _sysdiagnoseButton];
-[PKTextInputDebugRadarViewController _toggleSysdiagnoseButton];
-[PKTextInputDebugRadarViewController _updateSubmitButton];
-[PKTextInputDebugRadarViewController _updateSysdiagnoseButton];
-[PKTextInputDebugRadarViewController entryCellIncludedEntryDidChange:];
-[PKTextInputDebugRadarViewController initWithSharpenerLog:];
-[PKTextInputDebugRadarViewController set_contextDetailControl:];
-[PKTextInputDebugRadarViewController set_entriesCollectionView:];
-[PKTextInputDebugRadarViewController set_includeSysdiagnose:];
-[PKTextInputDebugRadarViewController set_includedEntryIndexes:];
-[PKTextInputDebugRadarViewController set_intendedTexts:];
-[PKTextInputDebugRadarViewController set_submitButton:];
-[PKTextInputDebugRadarViewController set_sysdiagnoseButton:];
-[PKTextInputDebugRadarViewController sharpenerLog];
```
