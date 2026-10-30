# `PLDuetServiceLpmSource`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"PLService" _duetService;
@"PLXPCListenerOperatorComposition" _lpmEnabledXPCListener;
@"PLXPCListenerOperatorComposition" _lpmDisabledXPCListener;
```

## Properties

```
@property (T@"PLService",W,V_duetService) duetService;
@property (T@"PLXPCListenerOperatorComposition",&,V_lpmEnabledXPCListener) lpmEnabledXPCListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_lpmDisabledXPCListener) lpmDisabledXPCListener;
```

## Class methods

```
+[PLDuetServiceLpmSource entryEventForwardDefinitionLpmSourceInformation];
```

## Instance methods

```
-[PLDuetServiceLpmSource init];
-[PLDuetServiceLpmSource stopService];
-[PLDuetServiceLpmSource setDuetService:];
-[PLDuetServiceLpmSource didReceiveLpmSourceInfoWithPayload:withFlag:];
-[PLDuetServiceLpmSource duetService];
-[PLDuetServiceLpmSource initOperatorDependanciesLpmSource:];
-[PLDuetServiceLpmSource lpmDisabledXPCListener];
-[PLDuetServiceLpmSource lpmEnabledXPCListener];
-[PLDuetServiceLpmSource setLpmDisabledXPCListener:];
-[PLDuetServiceLpmSource setLpmEnabledXPCListener:];
```
