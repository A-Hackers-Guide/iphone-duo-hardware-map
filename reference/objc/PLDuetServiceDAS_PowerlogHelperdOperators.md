# `PLDuetServiceDAS`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 33 instance methods, 11 class methods

## Instance variables

```
@"PLService" _duetService;
@"PLXPCListenerOperatorComposition" _dasActivityEventListener;
@"PLXPCListenerOperatorComposition" _dasActivityLifecycleEventListener;
@"PLXPCListenerOperatorComposition" _dasInfoEventListener;
@"PLXPCListenerOperatorComposition" _dasPredictionEventListener;
@"PLXPCListenerOperatorComposition" _dasBudgetEventListener;
@"PLXPCListenerOperatorComposition" _dasDataBudgetEventListener;
@"PLXPCListenerOperatorComposition" _dasEnergyReportEventListener;
@"PLXPCListenerOperatorComposition" _dasPoliciesBlockingCriteriaEventListener;
@"PLXPCListenerOperatorComposition" _dasTrialEventListener;
```

## Properties

```
@property (T@"PLService",W,V_duetService) duetService;
@property (T@"PLXPCListenerOperatorComposition",&,V_dasActivityEventListener) dasActivityEventListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_dasActivityLifecycleEventListener) dasActivityLifecycleEventListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_dasInfoEventListener) dasInfoEventListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_dasPredictionEventListener) dasPredictionEventListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_dasBudgetEventListener) dasBudgetEventListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_dasDataBudgetEventListener) dasDataBudgetEventListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_dasEnergyReportEventListener) dasEnergyReportEventListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_dasPoliciesBlockingCriteriaEventListener) dasPoliciesBlockingCriteriaEventListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_dasTrialEventListener) dasTrialEventListener;
```

## Class methods

```
+[PLDuetServiceDAS entryEventBackwardDefinitionsDASEnergyBudgetReport];
+[PLDuetServiceDAS entryEventForwardDefinitionsDASApplicationPrediction];
+[PLDuetServiceDAS entryEventForwardDefinitionsDASDataBudgetAvailable];
+[PLDuetServiceDAS entryEventForwardDefinitionsDASEnergyBudgetAvailable];
+[PLDuetServiceDAS entryEventForwardDefinitionsDASPrediction];
+[PLDuetServiceDAS entryEventForwardDefinitionsDASTrial];
+[PLDuetServiceDAS entryEventNoneDefinitionsDASActivity];
+[PLDuetServiceDAS entryEventNoneDefinitionsDASActivityDropCount];
+[PLDuetServiceDAS entryEventNoneDefinitionsDASActivityLifecycle];
+[PLDuetServiceDAS entryEventNoneDefinitionsDASInfo];
+[PLDuetServiceDAS entryEventNoneDefinitionsDASPoliciesBlockingCriteria];
```

## Instance methods

```
-[PLDuetServiceDAS init];
-[PLDuetServiceDAS stopService];
-[PLDuetServiceDAS fileProtectionTypeStringToEnum:];
-[PLDuetServiceDAS setDuetService:];
-[PLDuetServiceDAS dasActivityEventListener];
-[PLDuetServiceDAS dasActivityLifecycleEventListener];
-[PLDuetServiceDAS dasBudgetEventListener];
-[PLDuetServiceDAS dasDataBudgetEventListener];
-[PLDuetServiceDAS dasEnergyReportEventListener];
-[PLDuetServiceDAS dasInfoEventListener];
-[PLDuetServiceDAS dasPoliciesBlockingCriteriaEventListener];
-[PLDuetServiceDAS dasPredictionEventListener];
-[PLDuetServiceDAS dasTrialEventListener];
-[PLDuetServiceDAS didReceiveDASActivityEventWithPayload:];
-[PLDuetServiceDAS didReceiveDASActivityLifecycleEventWithPayload:];
-[PLDuetServiceDAS didReceiveDASBudgetEventWithPayload:];
-[PLDuetServiceDAS didReceiveDASDataBudgetEventWithPayload:];
-[PLDuetServiceDAS didReceiveDASInfoEventWithPayload:];
-[PLDuetServiceDAS didReceiveDASPoliciesBlockingCriteriaEventWithPayload:];
-[PLDuetServiceDAS didReceiveDASPredictionEventWithPayload:];
-[PLDuetServiceDAS didReceiveDASReportEventWithPayload:];
-[PLDuetServiceDAS didReceiveDASTrialEventWithPayload:];
-[PLDuetServiceDAS duetService];
-[PLDuetServiceDAS initOperatorDependanciesDAS:];
-[PLDuetServiceDAS setDasActivityEventListener:];
-[PLDuetServiceDAS setDasActivityLifecycleEventListener:];
-[PLDuetServiceDAS setDasBudgetEventListener:];
-[PLDuetServiceDAS setDasDataBudgetEventListener:];
-[PLDuetServiceDAS setDasEnergyReportEventListener:];
-[PLDuetServiceDAS setDasInfoEventListener:];
-[PLDuetServiceDAS setDasPoliciesBlockingCriteriaEventListener:];
-[PLDuetServiceDAS setDasPredictionEventListener:];
-[PLDuetServiceDAS setDasTrialEventListener:];
```
