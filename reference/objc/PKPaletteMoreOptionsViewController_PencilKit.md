# `PKPaletteMoreOptionsViewController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `PKPaletteEdgeLocating`
- 28 instance variables, 32 properties, 83 instance methods, 0 class methods

## Instance variables

```
B _shouldShowAutoMinimizeOption;
B _shouldShowFingerDrawsOption;
B _shouldAlwaysShowAutoRefineControls;
B _autoHideOn;
B _isFingerDrawsOn;
B _shouldShowTapToRadarOption;
B _shouldShowResetHandwritingEducationPane;
B _shouldShowOpenPencilSettingsOption;
B _isAutoRefineOn;
B _isProofreadingOn;
Q _edgeLocation;
Q _cornerLocation;
@"<PKPaletteMoreOptionsViewControllerDelegate>" _delegate;
@"UITraitCollection" _externalTraitCollection;
@"NSArray" _stackViewPositioningConstraints;
@"UIScrollView" _scrollView;
@"UIStackView" _stackView;
@"UIStackView" _autoMinimizeAndFingerDrawsCellsContainer;
@"PKPaletteOptionSwitchCell" _autoMinimizeCell;
@"PKPaletteOptionSwitchCell" _shapesCell;
@"PKPaletteOptionSwitchCell" _fingerDrawsCell;
@"PKPaletteOptionTitleCell" _tapToRadarCell;
@"PKPaletteOptionTitleCell" _resetHandwritingEducationPaneCell;
@"PKPaletteOptionTitleCell" _resetImageWandOnboardingPaneCell;
@"PKPaletteOptionTitleCell" _openPencilSettingsCell;
@"PKPaletteOptionSwitchCell" _autoRefineCell;
@"PKPaletteOptionInfoCell" _autoRefineNotReadyCell;
@"PKPaletteOptionSwitchCell" _proofreadingCell;
```

## Properties

```
@property (T@"UITraitCollection",&,N,V_externalTraitCollection) externalTraitCollection;
@property (T@"NSArray",&,N,V_stackViewPositioningConstraints) stackViewPositioningConstraints;
@property (T@"UIScrollView",&,N,V_scrollView) scrollView;
@property (T@"UIStackView",&,N,V_stackView) stackView;
@property (T@"UIStackView",&,N,V_autoMinimizeAndFingerDrawsCellsContainer) autoMinimizeAndFingerDrawsCellsContainer;
@property (T@"PKPaletteOptionSwitchCell",&,N,V_autoMinimizeCell) autoMinimizeCell;
@property (T@"PKPaletteOptionSwitchCell",&,N,V_shapesCell) shapesCell;
@property (T@"PKPaletteOptionSwitchCell",&,N,V_fingerDrawsCell) fingerDrawsCell;
@property (T@"PKPaletteOptionTitleCell",&,N,V_tapToRadarCell) tapToRadarCell;
@property (T@"PKPaletteOptionTitleCell",&,N,V_resetHandwritingEducationPaneCell) resetHandwritingEducationPaneCell;
@property (T@"PKPaletteOptionTitleCell",&,N,V_resetImageWandOnboardingPaneCell) resetImageWandOnboardingPaneCell;
@property (T@"PKPaletteOptionTitleCell",&,N,V_openPencilSettingsCell) openPencilSettingsCell;
@property (T@"PKPaletteOptionSwitchCell",&,N,V_autoRefineCell) autoRefineCell;
@property (T@"PKPaletteOptionInfoCell",&,N,V_autoRefineNotReadyCell) autoRefineNotReadyCell;
@property (T@"PKPaletteOptionSwitchCell",&,N,V_proofreadingCell) proofreadingCell;
@property (T@"<PKPaletteMoreOptionsViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_shouldShowAutoMinimizeOption) shouldShowAutoMinimizeOption;
@property (TB,N,V_shouldShowFingerDrawsOption) shouldShowFingerDrawsOption;
@property (TB,N,V_shouldAlwaysShowAutoRefineControls) shouldAlwaysShowAutoRefineControls;
@property (TB,N,GisAutoHideOn,V_autoHideOn) autoHideOn;
@property (TB,N,V_isFingerDrawsOn) isFingerDrawsOn;
@property (TB,N,V_shouldShowTapToRadarOption) shouldShowTapToRadarOption;
@property (TB,N,V_shouldShowResetHandwritingEducationPane) shouldShowResetHandwritingEducationPane;
@property (TB,N,V_shouldShowOpenPencilSettingsOption) shouldShowOpenPencilSettingsOption;
@property (TB,N,V_isAutoRefineOn) isAutoRefineOn;
@property (TB,N,V_isProofreadingOn) isProofreadingOn;
@property (TQ,N,V_edgeLocation) edgeLocation;
@property (TQ,N,V_cornerLocation) cornerLocation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKPaletteMoreOptionsViewController scrollView];
-[PKPaletteMoreOptionsViewController viewDidLoad];
-[PKPaletteMoreOptionsViewController setScrollView:];
-[PKPaletteMoreOptionsViewController _canShowWhileLocked];
-[PKPaletteMoreOptionsViewController setDelegate:];
-[PKPaletteMoreOptionsViewController delegate];
-[PKPaletteMoreOptionsViewController stackView];
-[PKPaletteMoreOptionsViewController setStackView:];
-[PKPaletteMoreOptionsViewController preferredContentSize];
-[PKPaletteMoreOptionsViewController _updateContentSize];
-[PKPaletteMoreOptionsViewController _fingerDrawsCellDidChangeValue:];
-[PKPaletteMoreOptionsViewController fingerDrawsCell];
-[PKPaletteMoreOptionsViewController stackViewPositioningConstraints];
-[PKPaletteMoreOptionsViewController isFingerDrawsOn];
-[PKPaletteMoreOptionsViewController setShouldShowFingerDrawsOption:];
-[PKPaletteMoreOptionsViewController _autoMinimizeCellDidChangeValue:];
-[PKPaletteMoreOptionsViewController _autoRefineCellDidChangeValue:];
-[PKPaletteMoreOptionsViewController _contentSizeMinWidth];
-[PKPaletteMoreOptionsViewController _handleOpenPencilSettingsCellTapped];
-[PKPaletteMoreOptionsViewController _handleResetHandwritingEducationPaneCellTapped];
-[PKPaletteMoreOptionsViewController _handleResetImageWandOnboardingCellTapped:];
-[PKPaletteMoreOptionsViewController _handleTapToRadarCellTapped];
-[PKPaletteMoreOptionsViewController _isCellInstalled:];
-[PKPaletteMoreOptionsViewController _proofreadingCellDidChangeValue:];
-[PKPaletteMoreOptionsViewController _reloadItems];
-[PKPaletteMoreOptionsViewController _reloadResetImageWandOnboardingCell];
-[PKPaletteMoreOptionsViewController _shouldInstallOpenPencilSettingsCell];
-[PKPaletteMoreOptionsViewController _shouldInstallResetHandwritingEducationPanelCell];
-[PKPaletteMoreOptionsViewController _shouldInstallTapToRadarCell];
-[PKPaletteMoreOptionsViewController _shouldRemoveOpenPencilSettingsCell];
-[PKPaletteMoreOptionsViewController _shouldRemoveResetHandwritingEducationPanelCell];
-[PKPaletteMoreOptionsViewController _shouldRemoveTapToRadarCell];
-[PKPaletteMoreOptionsViewController _updateAutoMinimizeCell];
-[PKPaletteMoreOptionsViewController _updateAutoRefineCell];
-[PKPaletteMoreOptionsViewController _updateFingerDrawsCell];
-[PKPaletteMoreOptionsViewController _updateProofreadingCell];
-[PKPaletteMoreOptionsViewController autoMinimizeAndFingerDrawsCellsContainer];
-[PKPaletteMoreOptionsViewController autoMinimizeCell];
-[PKPaletteMoreOptionsViewController autoRefineCell];
-[PKPaletteMoreOptionsViewController autoRefineNotReadyCell];
-[PKPaletteMoreOptionsViewController cornerLocation];
-[PKPaletteMoreOptionsViewController edgeLocation];
-[PKPaletteMoreOptionsViewController externalTraitCollection];
-[PKPaletteMoreOptionsViewController isAutoHideOn];
-[PKPaletteMoreOptionsViewController isAutoRefineOn];
-[PKPaletteMoreOptionsViewController isProofreadingOn];
-[PKPaletteMoreOptionsViewController openPencilSettingsCell];
-[PKPaletteMoreOptionsViewController proofreadingCell];
-[PKPaletteMoreOptionsViewController resetHandwritingEducationPaneCell];
-[PKPaletteMoreOptionsViewController resetImageWandOnboardingPaneCell];
-[PKPaletteMoreOptionsViewController setAutoHideOn:];
-[PKPaletteMoreOptionsViewController setAutoMinimizeAndFingerDrawsCellsContainer:];
-[PKPaletteMoreOptionsViewController setAutoMinimizeCell:];
-[PKPaletteMoreOptionsViewController setAutoRefineCell:];
-[PKPaletteMoreOptionsViewController setAutoRefineNotReadyCell:];
-[PKPaletteMoreOptionsViewController setCornerLocation:];
-[PKPaletteMoreOptionsViewController setEdgeLocation:];
-[PKPaletteMoreOptionsViewController setExternalTraitCollection:];
-[PKPaletteMoreOptionsViewController setFingerDrawsCell:];
-[PKPaletteMoreOptionsViewController setIsAutoRefineOn:];
-[PKPaletteMoreOptionsViewController setIsFingerDrawsOn:];
-[PKPaletteMoreOptionsViewController setIsProofreadingOn:];
-[PKPaletteMoreOptionsViewController setOpenPencilSettingsCell:];
-[PKPaletteMoreOptionsViewController setProofreadingCell:];
-[PKPaletteMoreOptionsViewController setResetHandwritingEducationPaneCell:];
-[PKPaletteMoreOptionsViewController setResetImageWandOnboardingPaneCell:];
-[PKPaletteMoreOptionsViewController setShapesCell:];
-[PKPaletteMoreOptionsViewController setShouldAlwaysShowAutoRefineControls:];
-[PKPaletteMoreOptionsViewController setShouldShowAutoMinimizeOption:];
-[PKPaletteMoreOptionsViewController setShouldShowOpenPencilSettingsOption:];
-[PKPaletteMoreOptionsViewController setShouldShowResetHandwritingEducationPane:];
-[PKPaletteMoreOptionsViewController setShouldShowTapToRadarOption:];
-[PKPaletteMoreOptionsViewController setStackViewPositioningConstraints:];
-[PKPaletteMoreOptionsViewController setTapToRadarCell:];
-[PKPaletteMoreOptionsViewController shapesCell];
-[PKPaletteMoreOptionsViewController shouldAlwaysShowAutoRefineControls];
-[PKPaletteMoreOptionsViewController shouldShowAutoMinimizeOption];
-[PKPaletteMoreOptionsViewController shouldShowFingerDrawsOption];
-[PKPaletteMoreOptionsViewController shouldShowOpenPencilSettingsOption];
-[PKPaletteMoreOptionsViewController shouldShowResetHandwritingEducationPane];
-[PKPaletteMoreOptionsViewController shouldShowTapToRadarOption];
-[PKPaletteMoreOptionsViewController tapToRadarCell];
-[PKPaletteMoreOptionsViewController updateUIForTraitCollection:];
```
