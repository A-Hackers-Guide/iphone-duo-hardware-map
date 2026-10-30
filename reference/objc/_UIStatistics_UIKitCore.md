# `_UIStatistics`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 18 instance methods, 37 class methods

## Instance variables

```
@"NSString" _key;
d _sampleValue;
@"NSMutableSet" _children;
d _sampleRate;
```

## Properties

```
@property (Td,N,V_sampleRate) sampleRate;
```

## Class methods

```
+[_UIStatistics feedbackGeneratorPlayCountWithSuffix:];
+[_UIStatistics previewInteractionTapCount];
+[_UIStatistics scrollBounceCount];
+[_UIStatistics recentsInputViewItemSelectedCount];
+[_UIStatistics feedbackGeneratorActivationCountWithSuffix:];
+[_UIStatistics feedbackEngineOutOfChannelsCountWithSuffix:];
+[_UIStatistics currentTime];
+[_UIStatistics previewInteractionPeekCount];
+[_UIStatistics controlTapCountWithCategory:suffix:];
+[_UIStatistics previewInteractionPopForce];
+[_UIStatistics pinchGestureCount];
+[_UIStatistics previewInteractionPeekDuration];
+[_UIStatistics alertButtonTapCount];
+[_UIStatistics feedbackEnginePrewarmDurationWithSuffix:];
+[_UIStatistics feedbackEngineActivationCountWithSuffix:];
+[_UIStatistics scrubberUsageCount];
+[_UIStatistics maxForce];
+[_UIStatistics previewInteractionPopCount];
+[_UIStatistics zoomGestureCount];
+[_UIStatistics coverSheetButtonMaximumForceWithActivation:category:];
+[_UIStatistics feedbackEnginePrewarmCountWithSuffix:];
+[_UIStatistics coverSheetButtonFirstActivationDurationWithCategory:];
+[_UIStatistics previewInteractionPeekForce];
+[_UIStatistics coverSheetButtonInteractionCountWithActivation:category:];
+[_UIStatistics feedbackEngineActivationDurationWithSuffix:];
+[_UIStatistics feedbackGeneratorActivationTimeOutCountWithSuffix:];
+[_UIStatistics recentsInputViewNewEntryCount];
+[_UIStatistics _sharedStatisticWithDomain:statisticsClass:identifierReporting:];
+[_UIStatistics coverSheetButtonInteractionDurationWithCategory:];
+[_UIStatistics feedbackGeneratorActivationDurationWithSuffix:];
+[_UIStatistics previewInteractionAlertPresentationCount];
+[_UIStatistics recentsInputViewNumberOfItems];
+[_UIStatistics recentsInputViewPresentationCount];
+[_UIStatistics feedbackGeneratorPreparationCountWithSuffix:];
+[_UIStatistics controlInteractionDurationDistributionWithCategory:suffix:];
+[_UIStatistics scrubberUsageTime];
+[_UIStatistics controlValueChangeEmittedCountWithCategory:suffix:];
```

## Instance methods

```
-[_UIStatistics _setValue:];
-[_UIStatistics sampleRate];
-[_UIStatistics initWithDomain:];
-[_UIStatistics init];
-[_UIStatistics setSampleRate:];
-[_UIStatistics description];
-[_UIStatistics _addChildStatistic:];
-[_UIStatistics _incrementValueBy:];
-[_UIStatistics _key];
-[_UIStatistics _recordDistributionTime:];
-[_UIStatistics _recordDistributionValue:];
-[_UIStatistics _removeChildStatistic:];
-[_UIStatistics _resetDistribution];
-[_UIStatistics _resetDistributionToValue:];
-[_UIStatistics _resetValue];
-[_UIStatistics _shouldSample];
-[_UIStatistics initWithDomain:identifierReporting:];
-[_UIStatistics randomizeSampleValue];
```
