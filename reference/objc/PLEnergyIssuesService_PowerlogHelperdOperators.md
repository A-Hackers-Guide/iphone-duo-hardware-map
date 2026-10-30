# `PLEnergyIssuesService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- 5 instance variables, 5 properties, 14 instance methods, 10 class methods

## Instance variables

```
@"PLXPCListenerOperatorComposition" _eventListener;
@"PLXPCListenerOperatorComposition" _xpcListenerEnergyIssueTrigger;
@"ComputeSafeguardsManagingClient" _safeguardsManagingClient;
@"PLEntryNotificationOperatorComposition" _coalitionCallback;
@"NSString" _entryKeyPLCoalitionAgentEventIntervalCoalition;
```

## Properties

```
@property (T@"PLXPCListenerOperatorComposition",&,V_eventListener) eventListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_xpcListenerEnergyIssueTrigger) xpcListenerEnergyIssueTrigger;
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
-[PLEnergyIssuesService safeguardsManagingClient];
-[PLEnergyIssuesService setAssertionThresholds];
-[PLEnergyIssuesService setCoalitionCallback:];
-[PLEnergyIssuesService setEventListener:];
-[PLEnergyIssuesService setSafeguardsManagingClient:];
-[PLEnergyIssuesService setXpcListenerEnergyIssueTrigger:];
-[PLEnergyIssuesService xpcListenerEnergyIssueTrigger];
```
