# `PLApplicationAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- Protocols: `LSApplicationWorkspaceObserverProtocol`
- 21 instance variables, 25 properties, 93 instance methods, 42 class methods

## Instance variables

```
B _scheduledAppCleanup;
@"NSSet" _currentDisplayIdentifiers;
@"BKSApplicationStateMonitor" _appStateMonitor;
@"RBSProcessMonitor" _RBSAppStateMonitor;
@"PLXPCListenerOperatorComposition" _widgetStatsListener;
@"PLXPCListenerOperatorComposition" _widgetUpdatesListener;
@"PLXPCListenerOperatorComposition" _suggestedWidgetReloadListener;
@"PLXPCListenerOperatorComposition" _posterUpdatesListener;
@"PLXPCListenerOperatorComposition" _ambientModeListener;
@"PLXPCListenerOperatorComposition" _liveActivityStatsListener;
@"PLXPCListenerOperatorComposition" _liveActivityUpdatesListener;
@"PLXPCListenerOperatorComposition" _systemApertureListener;
@"PLXPCListenerOperatorComposition" _ambientModeActiveFaceListener;
@"PLXPCListenerOperatorComposition" _ambientModeLifetimeCounterListener;
@"PLXPCListenerOperatorComposition" _motionToWakeListener;
@"RBSProcessMonitor" _appStateMonitorRBS;
@"PLXPCListenerOperatorComposition" _appDockingListener;
@"PLXPCListenerOperatorComposition" _appPrewarmListener;
@"PLXPCListenerOperatorComposition" _controlCenterStatsListener;
@"PLXPCListenerOperatorComposition" _controlCenterUpdatesListener;
@"PLNSNotificationOperatorComposition" _dailyTaskNotification;
```

## Properties

```
@property (T@"NSSet",&,V_currentDisplayIdentifiers) currentDisplayIdentifiers;
@property (T@"BKSApplicationStateMonitor",&,V_appStateMonitor) appStateMonitor;
@property (T@"RBSProcessMonitor",&,V_RBSAppStateMonitor) RBSAppStateMonitor;
@property (T@"PLXPCListenerOperatorComposition",&,V_widgetStatsListener) widgetStatsListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_widgetUpdatesListener) widgetUpdatesListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_suggestedWidgetReloadListener) suggestedWidgetReloadListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_posterUpdatesListener) posterUpdatesListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_ambientModeListener) ambientModeListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_liveActivityStatsListener) liveActivityStatsListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_liveActivityUpdatesListener) liveActivityUpdatesListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_systemApertureListener) systemApertureListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_ambientModeActiveFaceListener) ambientModeActiveFaceListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_ambientModeLifetimeCounterListener) ambientModeLifetimeCounterListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_motionToWakeListener) motionToWakeListener;
@property (T@"RBSProcessMonitor",&,V_appStateMonitorRBS) appStateMonitorRBS;
@property (T@"PLXPCListenerOperatorComposition",&,V_appDockingListener) appDockingListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_appPrewarmListener) appPrewarmListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_controlCenterStatsListener) controlCenterStatsListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_controlCenterUpdatesListener) controlCenterUpdatesListener;
@property (T@"PLNSNotificationOperatorComposition",&,V_dailyTaskNotification) dailyTaskNotification;
@property (TB,V_scheduledAppCleanup) scheduledAppCleanup;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PLApplicationAgent entryEventPointDefinitions];
+[PLApplicationAgent entryEventForwardDefinitions];
+[PLApplicationAgent entryEventBackwardDefinitions];
+[PLApplicationAgent entryEventNoneDefinitions];
+[PLApplicationAgent load];
+[PLApplicationAgent defaults];
+[PLApplicationAgent isVisible:];
+[PLApplicationAgent entryEventForwardDefinitionAmbientMode];
+[PLApplicationAgent isEnabled];
+[PLApplicationAgent installedPlugins];
+[PLApplicationAgent entryAggregateDefinitions];
+[PLApplicationAgent addAppVersion:withVersion:];
+[PLApplicationAgent appVersionForBundle:];
+[PLApplicationAgent entryAggregateDefinitionApplicationReason];
+[PLApplicationAgent entryAggregateDefintionWidgetUpdates];
+[PLApplicationAgent entryEventBackwardDefinitionApplicationMemory];
+[PLApplicationAgent entryEventBackwardDefinitionControlCenterStats];
+[PLApplicationAgent entryEventBackwardDefinitionWidgetStats];
+[PLApplicationAgent entryEventForwardDefinitionAmbientActiveFace];
+[PLApplicationAgent entryEventForwardDefinitionAmbientModeLifetimeCounter];
+[PLApplicationAgent entryEventForwardDefinitionApplication];
+[PLApplicationAgent entryEventForwardDefinitionApplicationDidUninstall];
+[PLApplicationAgent entryEventForwardDefinitionHomeScreenConfiguration];
+[PLApplicationAgent entryEventForwardDefinitionHomeScreenPresentation];
+[PLApplicationAgent entryEventForwardDefinitionLiveActivityStats];
+[PLApplicationAgent entryEventForwardDefinitionMotionToWake];
+[PLApplicationAgent entryEventForwardDefinitionRBSApplication];
+[PLApplicationAgent entryEventForwardDefinitionSystemAperture];
+[PLApplicationAgent entryEventNoneAllApps];
+[PLApplicationAgent entryEventNoneAllPlugins];
+[PLApplicationAgent entryEventPointDefinitionAppDocking];
+[PLApplicationAgent entryEventPointDefinitionAppPrewarm];
+[PLApplicationAgent entryEventPointDefinitionApplicationExitReason];
+[PLApplicationAgent entryEventPointDefinitionControlCenterUpdates];
+[PLApplicationAgent entryEventPointDefinitionLiveActivityUpdates];
+[PLApplicationAgent entryEventPointDefinitionPosterUpdates];
+[PLApplicationAgent entryEventPointDefinitionSuggestedWidgetReload];
+[PLApplicationAgent entryEventPointDefinitionWidgetUpdates];
+[PLApplicationAgent getReasons:];
+[PLApplicationAgent hasScreenPresence:];
+[PLApplicationAgent pluginEntryFromRecord:];
+[PLApplicationAgent removeAppVersion:forVersion:];
```

## Instance methods

```
-[PLApplicationAgent applicationsDidUninstall:];
-[PLApplicationAgent applicationsDidInstall:];
-[PLApplicationAgent ambientModeListener];
-[PLApplicationAgent init];
-[PLApplicationAgent dealloc];
-[PLApplicationAgent initOperatorDependancies];
-[PLApplicationAgent setDailyTaskNotification:];
-[PLApplicationAgent appStateMonitor];
-[PLApplicationAgent log];
-[PLApplicationAgent trimConditionsForEntryKey:forTrimDate:];
-[PLApplicationAgent dailyTaskNotification];
-[PLApplicationAgent RBSStatetoPLState:state:];
-[PLApplicationAgent RBSAppStateMonitor];
-[PLApplicationAgent setLiveActivityUpdatesListener:];
-[PLApplicationAgent stateDidChange:state:prevState:];
-[PLApplicationAgent ambientModeActiveFaceListener];
-[PLApplicationAgent ambientModeLifetimeCounterListener];
-[PLApplicationAgent appDockingListener];
-[PLApplicationAgent appPrewarmListener];
-[PLApplicationAgent appReferenceCleanup];
-[PLApplicationAgent appStateMonitorRBS];
-[PLApplicationAgent buildAppVersionDictionary:];
-[PLApplicationAgent checkAppReferenceCleanupNeeded];
-[PLApplicationAgent controlCenterStatsListener];
-[PLApplicationAgent controlCenterUpdatesListener];
-[PLApplicationAgent createWidgetStatsAccountingEvents:];
-[PLApplicationAgent currentDisplayIdentifiers];
-[PLApplicationAgent displayIdentifiersDidChange];
-[PLApplicationAgent getApplicationRecordSet:];
-[PLApplicationAgent isAppClipWithBundleID:];
-[PLApplicationAgent isApplication:];
-[PLApplicationAgent liveActivityStatsListener];
-[PLApplicationAgent liveActivityUpdatesListener];
-[PLApplicationAgent logAllApps];
-[PLApplicationAgent logAllPlugins];
-[PLApplicationAgent logEventBackwardApplicationMemoryWithBundleId:withSuspendedMemory:withPeakMemory:];
-[PLApplicationAgent logEventBackwardControlCenterStats:];
-[PLApplicationAgent logEventBackwardWidgetStats:];
-[PLApplicationAgent logEventForwardAmbientMode:];
-[PLApplicationAgent logEventForwardAmbientModeActiveFace:];
-[PLApplicationAgent logEventForwardAmbientModeLifetimeCounter:];
-[PLApplicationAgent logEventForwardApplicationDidUninstall:withAppName:];
-[PLApplicationAgent logEventForwardHomeScreenConfiguration:];
-[PLApplicationAgent logEventForwardHomeScreenPresentation:];
-[PLApplicationAgent logEventForwardLiveActivityStats:];
-[PLApplicationAgent logEventForwardMotionToWake:];
-[PLApplicationAgent logEventForwardRBSApplicationForBundleID:withPid:withState:withReasons:withVisibility:];
-[PLApplicationAgent logEventForwardSystemAperture:];
-[PLApplicationAgent logEventPointApplication];
-[PLApplicationAgent logEventPointApplicationExitReason:];
-[PLApplicationAgent logEventPointApplicationForDisplayID:];
-[PLApplicationAgent logEventPointApplicationForDisplayID:withPid:withState:withReasons:];
-[PLApplicationAgent logEventPointControlCenterUpdates:];
-[PLApplicationAgent logEventPointDASAppDocking:];
-[PLApplicationAgent logEventPointDASAppPrewarm:];
-[PLApplicationAgent logEventPointLiveActivityUpdates:];
-[PLApplicationAgent logEventPointPosterUpdates:];
-[PLApplicationAgent logEventPointSuggestedWidgetReload:];
-[PLApplicationAgent logEventPointWidgetUpdates:];
-[PLApplicationAgent logInstalledAppWithRecord:withBundleID:shouldMaskTimestamp:];
-[PLApplicationAgent logInstalledPlugin:];
-[PLApplicationAgent logUninstalledApp:];
-[PLApplicationAgent logUninstalledAppVersion:];
-[PLApplicationAgent logUpdatedAppVersion:];
-[PLApplicationAgent motionToWakeListener];
-[PLApplicationAgent posterUpdatesListener];
-[PLApplicationAgent refreshAllAppsAndPlugins];
-[PLApplicationAgent resetScheduledAppCleanup];
-[PLApplicationAgent scheduledAppCleanup];
-[PLApplicationAgent sendApplicationMetadataToCA];
-[PLApplicationAgent setAmbientModeActiveFaceListener:];
-[PLApplicationAgent setAmbientModeLifetimeCounterListener:];
-[PLApplicationAgent setAmbientModeListener:];
-[PLApplicationAgent setAppDockingListener:];
-[PLApplicationAgent setAppPrewarmListener:];
-[PLApplicationAgent setAppStateMonitor:];
-[PLApplicationAgent setAppStateMonitorRBS:];
-[PLApplicationAgent setControlCenterStatsListener:];
-[PLApplicationAgent setControlCenterUpdatesListener:];
-[PLApplicationAgent setCurrentDisplayIdentifiers:];
-[PLApplicationAgent setLiveActivityStatsListener:];
-[PLApplicationAgent setMotionToWakeListener:];
-[PLApplicationAgent setPosterUpdatesListener:];
-[PLApplicationAgent setRBSAppStateMonitor:];
-[PLApplicationAgent setScheduledAppCleanup:];
-[PLApplicationAgent setSuggestedWidgetReloadListener:];
-[PLApplicationAgent setSystemApertureListener:];
-[PLApplicationAgent setWidgetStatsListener:];
-[PLApplicationAgent setWidgetUpdatesListener:];
-[PLApplicationAgent suggestedWidgetReloadListener];
-[PLApplicationAgent systemApertureListener];
-[PLApplicationAgent widgetStatsListener];
-[PLApplicationAgent widgetUpdatesListener];
```
