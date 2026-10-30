# `PLScreenStateAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- Protocols: `FBSDisplayLayoutObserver`
- 29 instance variables, 33 properties, 89 instance methods, 18 class methods

## Instance variables

```
B _lastDisplayLayoutContainsLockScreenX;
B _lastDisplayLayoutContainsLockScreen;
i _displayStateX;
i _displayState;
@"FBSDisplayLayoutMonitor" _mainDisplayMonitor;
@"FBSDisplayLayoutMonitor" _airPlayDisplayMonitor;
@"FBSDisplayLayoutMonitor" _carPlayDisplayMonitor;
@"NSString" _primaryDisplayHWID;
@"NSString" _secondaryDisplayHWID;
@"PLXPCListenerOperatorComposition" _windowModeListener;
@"NSMutableDictionary" _lastScreenStateEntries;
@"NSMutableDictionary" _lastLayoutMonitorEntries;
@"NSMutableDictionary" _lastScreenStateEntriesX;
@"NSMutableDictionary" _lastLayoutMonitorEntriesX;
@"FBSDisplayLayout" _lastDisplayLayoutX;
@"NSArray" _lastMainLayoutEntries;
@"NSArray" _lastDisplayXLayoutEntries;
@"PLXPCListenerOperatorComposition" _iconDraggingListner;
@"PLXPCListenerOperatorComposition" _widgetAdditionAnimationListener;
@"PLXPCListenerOperatorComposition" _widgetFlipAnimationListener;
@"PLXPCListenerOperatorComposition" _springBoardAlwaysOnEnableStateListener;
@"PLXPCListenerOperatorComposition" _springBoardBacklightStateChangeListener;
@"PLXPCListenerOperatorComposition" _springBoardFlipbookStatisticsListener;
@"PLXPCResponderOperatorComposition" _springBoardAlwaysOnEnableStateResponder;
@"PLXPCResponderOperatorComposition" _springBoardBacklightStateChangeResponder;
@"PLXPCResponderOperatorComposition" _springBoardFlipbookStatisticsResponder;
@"PLEntryNotificationOperatorComposition" _displayCallback;
@"PLEntryNotificationOperatorComposition" _displayCallbackX;
@"FBSDisplayLayout" _lastDisplayLayout;
```

## Properties

```
@property (T@"FBSDisplayLayoutMonitor",&,V_mainDisplayMonitor) mainDisplayMonitor;
@property (T@"FBSDisplayLayoutMonitor",&,V_airPlayDisplayMonitor) airPlayDisplayMonitor;
@property (T@"FBSDisplayLayoutMonitor",&,V_carPlayDisplayMonitor) carPlayDisplayMonitor;
@property (T@"NSString",C,N,V_primaryDisplayHWID) primaryDisplayHWID;
@property (T@"NSString",C,N,V_secondaryDisplayHWID) secondaryDisplayHWID;
@property (T@"PLXPCListenerOperatorComposition",&,V_windowModeListener) windowModeListener;
@property (T@"NSMutableDictionary",&,V_lastScreenStateEntries) lastScreenStateEntries;
@property (T@"NSMutableDictionary",&,V_lastLayoutMonitorEntries) lastLayoutMonitorEntries;
@property (T@"NSMutableDictionary",&,V_lastScreenStateEntriesX) lastScreenStateEntriesX;
@property (T@"NSMutableDictionary",&,V_lastLayoutMonitorEntriesX) lastLayoutMonitorEntriesX;
@property (Ti,N,V_displayStateX) displayStateX;
@property (T@"FBSDisplayLayout",&,N,V_lastDisplayLayoutX) lastDisplayLayoutX;
@property (TB,N,V_lastDisplayLayoutContainsLockScreenX) lastDisplayLayoutContainsLockScreenX;
@property (T@"NSArray",C,N,V_lastMainLayoutEntries) lastMainLayoutEntries;
@property (T@"NSArray",C,N,V_lastDisplayXLayoutEntries) lastDisplayXLayoutEntries;
@property (T@"PLXPCListenerOperatorComposition",&,V_iconDraggingListner) iconDraggingListner;
@property (T@"PLXPCListenerOperatorComposition",&,V_widgetAdditionAnimationListener) widgetAdditionAnimationListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_widgetFlipAnimationListener) widgetFlipAnimationListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_springBoardAlwaysOnEnableStateListener) springBoardAlwaysOnEnableStateListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_springBoardBacklightStateChangeListener) springBoardBacklightStateChangeListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_springBoardFlipbookStatisticsListener) springBoardFlipbookStatisticsListener;
@property (T@"PLXPCResponderOperatorComposition",&,V_springBoardAlwaysOnEnableStateResponder) springBoardAlwaysOnEnableStateResponder;
@property (T@"PLXPCResponderOperatorComposition",&,V_springBoardBacklightStateChangeResponder) springBoardBacklightStateChangeResponder;
@property (T@"PLXPCResponderOperatorComposition",&,V_springBoardFlipbookStatisticsResponder) springBoardFlipbookStatisticsResponder;
@property (T@"PLEntryNotificationOperatorComposition",&,V_displayCallback) displayCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_displayCallbackX) displayCallbackX;
@property (Ti,V_displayState) displayState;
@property (T@"FBSDisplayLayout",&,V_lastDisplayLayout) lastDisplayLayout;
@property (TB,V_lastDisplayLayoutContainsLockScreen) lastDisplayLayoutContainsLockScreen;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PLScreenStateAgent entryEventPointDefinitions];
+[PLScreenStateAgent entryEventForwardDefinitions];
+[PLScreenStateAgent entryEventBackwardDefinitions];
+[PLScreenStateAgent entryEventNoneDefinitions];
+[PLScreenStateAgent load];
+[PLScreenStateAgent entryAggregateDefinitions];
+[PLScreenStateAgent entryAggregateDefinitionForeground];
+[PLScreenStateAgent entryAggregateDefinitionWidgetAdditionAnimation];
+[PLScreenStateAgent entryAggregateDefinitionWidgetFlipAnimation];
+[PLScreenStateAgent entryEventBackwardDefinitionAlwaysOnEnableState];
+[PLScreenStateAgent entryEventBackwardDefinitionBacklightStateChange];
+[PLScreenStateAgent entryEventBackwardDefinitionBacklightStateChangeX];
+[PLScreenStateAgent entryEventBackwardDefinitionFlipbookStatistics];
+[PLScreenStateAgent entryEventBackwardDefinitionIconDragging];
+[PLScreenStateAgent entryEventForwardScreenState];
+[PLScreenStateAgent entryEventForwardScreenStateX];
+[PLScreenStateAgent entryEventForwardWindowMode];
+[PLScreenStateAgent entryEventPointBacklightEvent];
```

## Instance methods

```
-[PLScreenStateAgent setMainDisplayMonitor:];
-[PLScreenStateAgent setDisplayState:];
-[PLScreenStateAgent init];
-[PLScreenStateAgent dealloc];
-[PLScreenStateAgent initOperatorDependancies];
-[PLScreenStateAgent mainDisplayMonitor];
-[PLScreenStateAgent displayState];
-[PLScreenStateAgent createCarPlayAccountingEvents:];
-[PLScreenStateAgent layoutMonitor:didUpdateDisplayLayout:withContext:];
-[PLScreenStateAgent log];
-[PLScreenStateAgent setDisplayCallback:];
-[PLScreenStateAgent GetBacklightState:];
-[PLScreenStateAgent displayCallback];
-[PLScreenStateAgent logEventForwardMainScreenState:];
-[PLScreenStateAgent setWidgetFlipAnimationListener:];
-[PLScreenStateAgent widgetAdditionAnimationListener];
-[PLScreenStateAgent accountForegroundWithMainPrecedence];
-[PLScreenStateAgent accountWithLayoutEntries:];
-[PLScreenStateAgent airPlayDisplayMonitor];
-[PLScreenStateAgent carPlayDisplayMonitor];
-[PLScreenStateAgent convertWindowingMode:];
-[PLScreenStateAgent convertZoomLevel:];
-[PLScreenStateAgent createAirPlayWiFiAccountingEvent:];
-[PLScreenStateAgent displayCallbackX];
-[PLScreenStateAgent displayStateX];
-[PLScreenStateAgent displayValueForLayout:];
-[PLScreenStateAgent handleDisplayCallback:];
-[PLScreenStateAgent handleDisplayCallbackX:];
-[PLScreenStateAgent iconDraggingListner];
-[PLScreenStateAgent isSecondaryDisplay:];
-[PLScreenStateAgent lastDisplayLayout];
-[PLScreenStateAgent lastDisplayLayoutContainsLockScreen];
-[PLScreenStateAgent lastDisplayLayoutContainsLockScreenX];
-[PLScreenStateAgent lastDisplayLayoutX];
-[PLScreenStateAgent lastDisplayXLayoutEntries];
-[PLScreenStateAgent lastLayoutMonitorEntries];
-[PLScreenStateAgent lastLayoutMonitorEntriesX];
-[PLScreenStateAgent lastMainLayoutEntries];
-[PLScreenStateAgent lastScreenStateEntries];
-[PLScreenStateAgent lastScreenStateEntriesX];
-[PLScreenStateAgent logAggregateWidgetAdditionAnimation:];
-[PLScreenStateAgent logAggregateWidgetFlipAnimation:];
-[PLScreenStateAgent logEventBackwardAlwaysOnEnableState:];
-[PLScreenStateAgent logEventBackwardBacklightStateChange:];
-[PLScreenStateAgent logEventBackwardBacklightStateChangeX:];
-[PLScreenStateAgent logEventBackwardFlipbookStatistics:];
-[PLScreenStateAgent logEventBackwardIconDragging:];
-[PLScreenStateAgent logEventForwardAirPlayScreenState:];
-[PLScreenStateAgent logEventForwardCarScreenState:];
-[PLScreenStateAgent logEventForwardScreenStateX:];
-[PLScreenStateAgent logEventForwardWindowMode:];
-[PLScreenStateAgent logEventPointMainBacklightEvent:withContext:];
-[PLScreenStateAgent postEnhancedScreenStateNotification:currentLayout:];
-[PLScreenStateAgent primaryDisplayHWID];
-[PLScreenStateAgent processQuery:withEntryKey:];
-[PLScreenStateAgent secondaryDisplayHWID];
-[PLScreenStateAgent setAirPlayDisplayMonitor:];
-[PLScreenStateAgent setCarPlayDisplayMonitor:];
-[PLScreenStateAgent setDisplayCallbackX:];
-[PLScreenStateAgent setDisplayStateX:];
-[PLScreenStateAgent setIconDraggingListner:];
-[PLScreenStateAgent setLastDisplayLayout:];
-[PLScreenStateAgent setLastDisplayLayoutContainsLockScreen:];
-[PLScreenStateAgent setLastDisplayLayoutContainsLockScreenX:];
-[PLScreenStateAgent setLastDisplayLayoutX:];
-[PLScreenStateAgent setLastDisplayXLayoutEntries:];
-[PLScreenStateAgent setLastLayoutMonitorEntries:];
-[PLScreenStateAgent setLastLayoutMonitorEntriesX:];
-[PLScreenStateAgent setLastMainLayoutEntries:];
-[PLScreenStateAgent setLastScreenStateEntries:];
-[PLScreenStateAgent setLastScreenStateEntriesX:];
-[PLScreenStateAgent setPrimaryDisplayHWID:];
-[PLScreenStateAgent setSecondaryDisplayHWID:];
-[PLScreenStateAgent setSpringBoardAlwaysOnEnableStateListener:];
-[PLScreenStateAgent setSpringBoardAlwaysOnEnableStateResponder:];
-[PLScreenStateAgent setSpringBoardBacklightStateChangeListener:];
-[PLScreenStateAgent setSpringBoardBacklightStateChangeResponder:];
-[PLScreenStateAgent setSpringBoardFlipbookStatisticsListener:];
-[PLScreenStateAgent setSpringBoardFlipbookStatisticsResponder:];
-[PLScreenStateAgent setWidgetAdditionAnimationListener:];
-[PLScreenStateAgent setWindowModeListener:];
-[PLScreenStateAgent springBoardAlwaysOnEnableStateListener];
-[PLScreenStateAgent springBoardAlwaysOnEnableStateResponder];
-[PLScreenStateAgent springBoardBacklightStateChangeListener];
-[PLScreenStateAgent springBoardBacklightStateChangeResponder];
-[PLScreenStateAgent springBoardFlipbookStatisticsListener];
-[PLScreenStateAgent springBoardFlipbookStatisticsResponder];
-[PLScreenStateAgent widgetFlipAnimationListener];
-[PLScreenStateAgent windowModeListener];
```
