# `UIUpdateInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 6 properties, 6 instance methods, 2 class methods

## Instance variables

```
Q _updateNumber;
B _immediatePresentationExpected;
B _lowLatencyEventDispatchConfirmed;
B _performingLowLatencyPhases;
d _modelTime;
d _completionDeadlineTime;
d _estimatedPresentationTime;
```

## Properties

```
@property (Td,R,N,V_modelTime) modelTime;
@property (Td,R,N,V_completionDeadlineTime) completionDeadlineTime;
@property (Td,R,N,V_estimatedPresentationTime) estimatedPresentationTime;
@property (TB,R,N,GisImmediatePresentationExpected,V_immediatePresentationExpected) immediatePresentationExpected;
@property (TB,R,N,GisLowLatencyEventDispatchConfirmed,V_lowLatencyEventDispatchConfirmed) lowLatencyEventDispatchConfirmed;
@property (TB,R,N,GisPerformingLowLatencyPhases,V_performingLowLatencyPhases) performingLowLatencyPhases;
```

## Class methods

```
+[UIUpdateInfo currentUpdateInfoForView:];
+[UIUpdateInfo currentUpdateInfoForWindowScene:];
```

## Instance methods

```
-[UIUpdateInfo isImmediatePresentationExpected];
-[UIUpdateInfo completionDeadlineTime];
-[UIUpdateInfo estimatedPresentationTime];
-[UIUpdateInfo isLowLatencyEventDispatchConfirmed];
-[UIUpdateInfo isPerformingLowLatencyPhases];
-[UIUpdateInfo modelTime];
```
