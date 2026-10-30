# `PLProcessExitAggregatorHistogram`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
i _total;
i _duration_0_5;
i _duration_5_10;
i _duration_10_60;
i _duration_60_above;
i _duration_unknown;
```

## Properties

```
@property (Ti,V_total) total;
@property (Ti,V_duration_0_5) duration_0_5;
@property (Ti,V_duration_5_10) duration_5_10;
@property (Ti,V_duration_10_60) duration_10_60;
@property (Ti,V_duration_60_above) duration_60_above;
@property (Ti,V_duration_unknown) duration_unknown;
```

## Instance methods

```
-[PLProcessExitAggregatorHistogram total];
-[PLProcessExitAggregatorHistogram description];
-[PLProcessExitAggregatorHistogram setTotal:];
-[PLProcessExitAggregatorHistogram duration_0_5];
-[PLProcessExitAggregatorHistogram duration_10_60];
-[PLProcessExitAggregatorHistogram duration_5_10];
-[PLProcessExitAggregatorHistogram duration_60_above];
-[PLProcessExitAggregatorHistogram duration_unknown];
-[PLProcessExitAggregatorHistogram setDuration_0_5:];
-[PLProcessExitAggregatorHistogram setDuration_10_60:];
-[PLProcessExitAggregatorHistogram setDuration_5_10:];
-[PLProcessExitAggregatorHistogram setDuration_60_above:];
-[PLProcessExitAggregatorHistogram setDuration_unknown:];
```
