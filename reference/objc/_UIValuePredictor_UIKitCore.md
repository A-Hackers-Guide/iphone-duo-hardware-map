# `_UIValuePredictor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 21 instance variables, 11 properties, 49 instance methods, 0 class methods

## Instance variables

```
Q _capacity;
Q _arrayCapacity;
^d _values;
^d _valueWeights;
^d _predictions;
^d _confidenceFactorsForVelocity;
^d _confidenceFactorsForHistoricalAccuracy;
^d _confidenceFactorsForDerivativeStability;
^d _confidenceFactors;
^^d _derivatives;
d _minHistoricalAccuracyThreshold;
d _maxHistoricalAccuracyThreshold;
d _derivativeStabilityThreshold;
d _minVelocityThreshold;
d _maxVelocityThreshold;
d _minConstraint;
d _maxConstraint;
B _wrapConstraint;
Q _numValues;
Q _numPredictions;
Q _numDerivatives;
```

## Properties

```
@property (Td,N,V_minHistoricalAccuracyThreshold) minHistoricalAccuracyThreshold;
@property (Td,N,V_maxHistoricalAccuracyThreshold) maxHistoricalAccuracyThreshold;
@property (Td,N,V_derivativeStabilityThreshold) derivativeStabilityThreshold;
@property (Td,N,V_minVelocityThreshold) minVelocityThreshold;
@property (Td,N,V_maxVelocityThreshold) maxVelocityThreshold;
@property (Td,N,V_minConstraint) minConstraint;
@property (Td,N,V_maxConstraint) maxConstraint;
@property (TB,N,V_wrapConstraint) wrapConstraint;
@property (TQ,R,N,V_numValues) numValues;
@property (TQ,R,N,V_numPredictions) numPredictions;
@property (TQ,R,N,V_numDerivatives) numDerivatives;
```

## Instance methods

```
-[_UIValuePredictor minHistoricalAccuracyThreshold];
-[_UIValuePredictor initFromValuePredictor:];
-[_UIValuePredictor init];
-[_UIValuePredictor setMinConstraint:];
-[_UIValuePredictor setMaxVelocityThreshold:];
-[_UIValuePredictor addValue:weight:];
-[_UIValuePredictor predictions];
-[_UIValuePredictor _predictionsAtIndex:];
-[_UIValuePredictor dealloc];
-[_UIValuePredictor _derivatives];
-[_UIValuePredictor _updateConfidenceFactorsForHistoricalAccuracyAtIndex:];
-[_UIValuePredictor maxConstraint];
-[_UIValuePredictor _valuesAtIndex:];
-[_UIValuePredictor _slideDataWindow];
-[_UIValuePredictor _updateDerivatives:fromArray:weights:atIndex:wrap:];
-[_UIValuePredictor setMinVelocityThreshold:];
-[_UIValuePredictor numDerivatives];
-[_UIValuePredictor initWithNumPredictions:numDerivatives:];
-[_UIValuePredictor _getPriorPredictions:forValueAtIndex:];
-[_UIValuePredictor descriptionFromIndex:toIndex:includeHeader:includeDetailedConfidence:];
-[_UIValuePredictor numPredictions];
-[_UIValuePredictor _confidenceFactorsForDerivativeStabilityAtIndex:];
-[_UIValuePredictor _setupDefaults];
-[_UIValuePredictor minConstraint];
-[_UIValuePredictor setMaxHistoricalAccuracyThreshold:];
-[_UIValuePredictor _valueWeightsAtIndex:];
-[_UIValuePredictor derivativeStabilityThreshold];
-[_UIValuePredictor _updateConfidenceFactorsForVelocityAtIndex:];
-[_UIValuePredictor maxVelocityThreshold];
-[_UIValuePredictor _confidenceFactorsAtIndex:];
-[_UIValuePredictor _ensureCapacity:];
-[_UIValuePredictor wrapConstraint];
-[_UIValuePredictor setMinHistoricalAccuracyThreshold:];
-[_UIValuePredictor _updatePredictionsAtIndex:];
-[_UIValuePredictor numValues];
-[_UIValuePredictor description];
-[_UIValuePredictor _confidenceFactorsForVelocityAtIndex:];
-[_UIValuePredictor setMaxConstraint:];
-[_UIValuePredictor _updateConfidenceFactorsForDerivativeStabilityAtIndex:];
-[_UIValuePredictor minVelocityThreshold];
-[_UIValuePredictor confidenceFactors];
-[_UIValuePredictor copyWithZone:];
-[_UIValuePredictor _updateConfidenceFactorsAtIndex:];
-[_UIValuePredictor setWrapConstraint:];
-[_UIValuePredictor maxHistoricalAccuracyThreshold];
-[_UIValuePredictor setDerivativeStabilityThreshold:];
-[_UIValuePredictor _propagateDerivatives:fromHigherDerivatives:atIndex:];
-[_UIValuePredictor _constrainPrediction:];
-[_UIValuePredictor _confidenceFactorsForHistoricalAccuracyAtIndex:];
```
