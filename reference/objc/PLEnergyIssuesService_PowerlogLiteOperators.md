# `PLEnergyIssuesService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- 16 instance variables, 16 properties, 75 instance methods, 18 class methods

## Instance variables

```
B _pushTopicLimitsUrsaEnabled;
@"PLXPCListenerOperatorComposition" _eventListener;
@"PLXPCListenerOperatorComposition" _xpcListenerEnergyIssueTrigger;
q _ursaStatus;
@"_TtC21PowerlogLiteOperators10UrsaClient" _ursaClient;
@"PLXPCResponderOperatorComposition" _ursaResponder;
@"PLXPCListenerOperatorComposition" _ursaInteractionListener;
@"PLEntryNotificationOperatorComposition" _powerExceptionListener;
@"PLEntryNotificationOperatorComposition" _awdlTimeoutListener;
@"PLEntryNotificationOperatorComposition" _pushTopicLimitsListener;
@"NSMutableDictionary" _pushLimitExceedanceTracking;
@"TRIClient" _pushTopicLimitsTrialClient;
@"<TRINotificationToken>" _pushTopicLimitsTrialUpdateToken;
@"ComputeSafeguardsManagingClient" _safeguardsManagingClient;
@"PLEntryNotificationOperatorComposition" _coalitionCallback;
@"NSString" _entryKeyPLCoalitionAgentEventIntervalCoalition;
```

## Properties

```
@property (T@"PLXPCListenerOperatorComposition",&,V_eventListener) eventListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_xpcListenerEnergyIssueTrigger) xpcListenerEnergyIssueTrigger;
@property (Tq,V_ursaStatus) ursaStatus;
@property (T@"_TtC21PowerlogLiteOperators10UrsaClient",&,V_ursaClient) ursaClient;
@property (T@"PLXPCResponderOperatorComposition",&,V_ursaResponder) ursaResponder;
@property (T@"PLXPCListenerOperatorComposition",&,V_ursaInteractionListener) ursaInteractionListener;
@property (T@"PLEntryNotificationOperatorComposition",&,V_powerExceptionListener) powerExceptionListener;
@property (T@"PLEntryNotificationOperatorComposition",&,V_awdlTimeoutListener) awdlTimeoutListener;
@property (T@"PLEntryNotificationOperatorComposition",&,V_pushTopicLimitsListener) pushTopicLimitsListener;
@property (T@"NSMutableDictionary",&,V_pushLimitExceedanceTracking) pushLimitExceedanceTracking;
@property (T@"TRIClient",&,N,V_pushTopicLimitsTrialClient) pushTopicLimitsTrialClient;
@property (T@"<TRINotificationToken>",&,N,V_pushTopicLimitsTrialUpdateToken) pushTopicLimitsTrialUpdateToken;
@property (TB,N,V_pushTopicLimitsUrsaEnabled) pushTopicLimitsUrsaEnabled;
@property (T@"ComputeSafeguardsManagingClient",&,V_safeguardsManagingClient) safeguardsManagingClient;
@property (T@"PLEntryNotificationOperatorComposition",&,V_coalitionCallback) coalitionCallback;
@property (T@"NSString",R,V_entryKeyPLCoalitionAgentEventIntervalCoalition) entryKeyPLCoalitionAgentEventIntervalCoalition;
```

## Class methods

```
+[PLEnergyIssuesService entryEventIntervalDefinitions];
+[PLEnergyIssuesService entryEventPointDefinitions];
+[PLEnergyIssuesService entryEventForwardDefinitions];
+[PLEnergyIssuesService load];
+[PLEnergyIssuesService supportsUrsa];
+[PLEnergyIssuesService entryEventForwardDefinitionHighPowerDetection];
+[PLEnergyIssuesService entryEventIntervalDefinitionsUrsaIssues];
+[PLEnergyIssuesService entryEventPointDefinitionEnergySignatures];
+[PLEnergyIssuesService entryEventPointDefinitionUrsaInteraction];
+[PLEnergyIssuesService entryEventPointDefinitionUrsaSummary];
+[PLEnergyIssuesService createIssueEntriesFrom:forKey:now:midnight:];
+[PLEnergyIssuesService findResponsibleProcessForAWDLServices:advertisingServices:serviceToClients:];
+[PLEnergyIssuesService isTestRackDevice:withExpGroup:internalKeyDetected:];
+[PLEnergyIssuesService parseAWDLRegisteredClients:];
+[PLEnergyIssuesService parseBootArgs:];
+[PLEnergyIssuesService shouldPopUpForPowerException];
+[PLEnergyIssuesService shouldPopUpForPowerExceptionForProcess:];
+[PLEnergyIssuesService shouldPopUpForPowerExceptionWithFatalCount:withNonFatalCount:withMitigationsEnabled:withIssueType:];
```

## Instance methods

```
-[PLEnergyIssuesService init];
-[PLEnergyIssuesService initOperatorDependancies];
-[PLEnergyIssuesService eventListener];
-[PLEnergyIssuesService coalitionCallback];
-[PLEnergyIssuesService createAssertionThreshold:withAggregateLimit:];
-[PLEnergyIssuesService entryKeyPLCoalitionAgentEventIntervalCoalition];
-[PLEnergyIssuesService handleAssertionNotifications];
-[PLEnergyIssuesService initializeSafeguardsSystem];
-[PLEnergyIssuesService safeguardsManagingClient];
-[PLEnergyIssuesService setAssertionThresholds];
-[PLEnergyIssuesService setCoalitionCallback:];
-[PLEnergyIssuesService setEventListener:];
-[PLEnergyIssuesService setSafeguardsManagingClient:];
-[PLEnergyIssuesService setXpcListenerEnergyIssueTrigger:];
-[PLEnergyIssuesService xpcListenerEnergyIssueTrigger];
-[PLEnergyIssuesService pushTopicLimitsTrialUpdateToken];
-[PLEnergyIssuesService handleUrsaTask:];
-[PLEnergyIssuesService registerPowerExceptionCallbacks];
-[PLEnergyIssuesService setPushLimitExceedanceTracking:];
-[PLEnergyIssuesService addUrsaResponders];
-[PLEnergyIssuesService awdlTimeoutListener];
-[PLEnergyIssuesService buildTableUpdateEntriesForPeriodicCall];
-[PLEnergyIssuesService buildVersionChanged];
-[PLEnergyIssuesService checkUrsaBootArgs];
-[PLEnergyIssuesService defaultFetchWindow];
-[PLEnergyIssuesService deregister:];
-[PLEnergyIssuesService deregisterUrsa];
-[PLEnergyIssuesService extractActionfromEntry:];
-[PLEnergyIssuesService extractProcessNameFromEntry:];
-[PLEnergyIssuesService getRepeatingTaskWith:needsSubmit:];
-[PLEnergyIssuesService getUrsaTask:];
-[PLEnergyIssuesService handleAWDLTimeout:];
-[PLEnergyIssuesService handlePeriodicCallback:withRequestUUID:withPayload:];
-[PLEnergyIssuesService handlePowerException:];
-[PLEnergyIssuesService handlePushTopicLimits:];
-[PLEnergyIssuesService handleUrsaCallback:withRequestUUID:withPayload:];
-[PLEnergyIssuesService initializePushTopicExceedanceCountsFromPowerlog];
-[PLEnergyIssuesService initializeUrsa];
-[PLEnergyIssuesService insertSystemTime:fromPLEntry:];
-[PLEnergyIssuesService isUrsaDevModeEnabled];
-[PLEnergyIssuesService isValidUrsaEntry:];
-[PLEnergyIssuesService logOnDeviceIssueTelemetry:withNotified:withRequestUUID:];
-[PLEnergyIssuesService postUrsaNotification:];
-[PLEnergyIssuesService powerExceptionListener];
-[PLEnergyIssuesService pushLimitExceedanceTracking];
-[PLEnergyIssuesService pushTopicLimitsListener];
-[PLEnergyIssuesService pushTopicLimitsTrialClient];
-[PLEnergyIssuesService pushTopicLimitsUrsaEnabled];
-[PLEnergyIssuesService queryExistingUrsaEntries:];
-[PLEnergyIssuesService registerAWDLTimeoutCallbacks];
-[PLEnergyIssuesService registerPushTopicLimitsCallbacks];
-[PLEnergyIssuesService registerTaskWith:inQueue:launchHandler:];
-[PLEnergyIssuesService registerUrsa];
-[PLEnergyIssuesService requestUrsaNotificationAndLog:];
-[PLEnergyIssuesService runPeriodic:withFlag:];
-[PLEnergyIssuesService setAwdlTimeoutListener:];
-[PLEnergyIssuesService setPowerExceptionListener:];
-[PLEnergyIssuesService setPushTopicLimitsListener:];
-[PLEnergyIssuesService setPushTopicLimitsTrialClient:];
-[PLEnergyIssuesService setPushTopicLimitsTrialUpdateToken:];
-[PLEnergyIssuesService setPushTopicLimitsUrsaEnabled:];
-[PLEnergyIssuesService setUrsaClient:];
-[PLEnergyIssuesService setUrsaInteractionListener:];
-[PLEnergyIssuesService setUrsaResponder:];
-[PLEnergyIssuesService setUrsaStatus:];
-[PLEnergyIssuesService shouldUpdateTableFrom:newPayload:];
-[PLEnergyIssuesService submitTask:];
-[PLEnergyIssuesService updateExistingTableEntry:withResponsePayload:];
-[PLEnergyIssuesService updateParamsForUrsaTask:];
-[PLEnergyIssuesService updateTask:];
-[PLEnergyIssuesService ursaClient];
-[PLEnergyIssuesService ursaInteractionListener];
-[PLEnergyIssuesService ursaResponder];
-[PLEnergyIssuesService ursaStatus];
-[PLEnergyIssuesService writeUrsaNotificationToTable:withIssueType:];
```
