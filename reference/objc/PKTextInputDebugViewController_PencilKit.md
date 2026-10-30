# `PKTextInputDebugViewController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UITableViewDataSource`, `UITableViewDelegate`, `PKTextInputDebugViewTableCellDelegate`, `PKTextInputDebugStateIntrospectorDelegate`
- 14 instance variables, 18 properties, 51 instance methods, 0 class methods

## Instance variables

```
B __visualizeTargets;
B __needsReloadData;
B __needsReloadTargetsVisualization;
@"PKTextInputDebugStateIntrospector" _introspectorDataSource;
@"<PKTextInputDebugViewControllerDelegate>" _delegate;
@"PKTextInputDebugLogController" _debugLogController;
@"PKTextInputElementsController" _elementsController;
Q _statusViewAnchorCorner;
@"UIView" __statusContainerView;
@"UITableView" __statusTableView;
@"UIToolbar" __statusViewToolbar;
@"PKTextInputDebugTargetsView" __targetsContainerView;
@"NSArray" __statusViewPositionConstraints;
@"NSTimer" __autoreloadTimer;
```

## Properties

```
@property (T@"UIView",&,N,V__statusContainerView) _statusContainerView;
@property (T@"UITableView",&,N,V__statusTableView) _statusTableView;
@property (T@"UIToolbar",&,N,V__statusViewToolbar) _statusViewToolbar;
@property (T@"PKTextInputDebugTargetsView",&,N,V__targetsContainerView) _targetsContainerView;
@property (T@"NSArray",&,N,V__statusViewPositionConstraints) _statusViewPositionConstraints;
@property (TB,N,S_setVisualizeTargets:,V__visualizeTargets) _visualizeTargets;
@property (TB,N,V__needsReloadData) _needsReloadData;
@property (TB,N,V__needsReloadTargetsVisualization) _needsReloadTargetsVisualization;
@property (T@"NSTimer",&,N,V__autoreloadTimer) _autoreloadTimer;
@property (T@"PKTextInputDebugStateIntrospector",&,N,V_introspectorDataSource) introspectorDataSource;
@property (T@"<PKTextInputDebugViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"PKTextInputDebugLogController",&,N,V_debugLogController) debugLogController;
@property (T@"PKTextInputElementsController",&,N,V_elementsController) elementsController;
@property (TQ,N,V_statusViewAnchorCorner) statusViewAnchorCorner;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKTextInputDebugViewController tableView:numberOfRowsInSection:];
-[PKTextInputDebugViewController numberOfSectionsInTableView:];
-[PKTextInputDebugViewController tableView:cellForRowAtIndexPath:];
-[PKTextInputDebugViewController viewDidLoad];
-[PKTextInputDebugViewController _canShowWhileLocked];
-[PKTextInputDebugViewController setDelegate:];
-[PKTextInputDebugViewController viewDidAppear:];
-[PKTextInputDebugViewController loadView];
-[PKTextInputDebugViewController delegate];
-[PKTextInputDebugViewController viewDidDisappear:];
-[PKTextInputDebugViewController _updateStatusView];
-[PKTextInputDebugViewController _handleCloseButton:];
-[PKTextInputDebugViewController _updateTargetsVisualizationView];
-[PKTextInputDebugViewController _autoreloadTimer];
-[PKTextInputDebugViewController _configureCell:forItemAtIndex:];
-[PKTextInputDebugViewController _handleAutoreloadTimerFired];
-[PKTextInputDebugViewController _handleLogButton:];
-[PKTextInputDebugViewController _handleRadarButton:];
-[PKTextInputDebugViewController _handleTargetsButton:];
-[PKTextInputDebugViewController _needsReloadData];
-[PKTextInputDebugViewController _needsReloadTargetsVisualization];
-[PKTextInputDebugViewController _reloadDebugStateData];
-[PKTextInputDebugViewController _reloadTargetsVisualization];
-[PKTextInputDebugViewController _setVisualizeTargets:];
-[PKTextInputDebugViewController _setupStatusView];
-[PKTextInputDebugViewController _statusContainerView];
-[PKTextInputDebugViewController _statusTableView];
-[PKTextInputDebugViewController _statusViewPositionConstraints];
-[PKTextInputDebugViewController _statusViewToolbar];
-[PKTextInputDebugViewController _targetsContainerView];
-[PKTextInputDebugViewController _visualizeTargets];
-[PKTextInputDebugViewController debugLogController];
-[PKTextInputDebugViewController debugStateIntrospectorContentDidChange:];
-[PKTextInputDebugViewController debugViewTableCellDidTapDetailsButton:];
-[PKTextInputDebugViewController elementsController];
-[PKTextInputDebugViewController introspectorDataSource];
-[PKTextInputDebugViewController setDebugLogController:];
-[PKTextInputDebugViewController setElementsController:];
-[PKTextInputDebugViewController setIntrospectorDataSource:];
-[PKTextInputDebugViewController setNeedsReloadDebugStateData];
-[PKTextInputDebugViewController setNeedsReloadTargetsVisualization];
-[PKTextInputDebugViewController setStatusViewAnchorCorner:];
-[PKTextInputDebugViewController set_autoreloadTimer:];
-[PKTextInputDebugViewController set_needsReloadData:];
-[PKTextInputDebugViewController set_needsReloadTargetsVisualization:];
-[PKTextInputDebugViewController set_statusContainerView:];
-[PKTextInputDebugViewController set_statusTableView:];
-[PKTextInputDebugViewController set_statusViewPositionConstraints:];
-[PKTextInputDebugViewController set_statusViewToolbar:];
-[PKTextInputDebugViewController set_targetsContainerView:];
-[PKTextInputDebugViewController statusViewAnchorCorner];
```
