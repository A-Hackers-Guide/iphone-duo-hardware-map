# `CBRamp`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 20 properties, 30 instance methods, 2 class methods

## Instance variables

```
d _sMachTimebaseFactor;
@"NSObject<OS_os_log>" _logHandle;
B _isFinished;
f _length;
f _remainingLength;
f _frequency;
f _targetValue;
f _originalValue;
f _currentValue;
f _largestStep;
i _totalSteps;
f _largestTimeDelta;
@? _rampProgressCallback;
@? _rampFinishedCallback;
d _startTime;
d _currentTimestamp;
d _startAbsoluteTime;
d _currentAbsoluteTimestamp;
@"NSString" _identifier;
@"NSDictionary" _properties;
@"CBTrackedAnimation" _trackedAnimation;
```

## Properties

```
@property (T@?,C,V_rampProgressCallback) rampProgressCallback;
@property (T@?,C,V_rampFinishedCallback) rampFinishedCallback;
@property (Tf,R,V_length) length;
@property (Tf,R,V_remainingLength) remainingLength;
@property (Tf,R,V_frequency) frequency;
@property (Tf,R,V_targetValue) targetValue;
@property (Tf,R,V_originalValue) originalValue;
@property (Tf,R,V_currentValue) currentValue;
@property (Td,R,V_startTime) startTime;
@property (Td,R,V_currentTimestamp) currentTimestamp;
@property (Td,R,V_startAbsoluteTime) startAbsoluteTime;
@property (Td,R,V_currentAbsoluteTimestamp) currentAbsoluteTimestamp;
@property (TB,R,V_isFinished) isFinished;
@property (T@"NSString",R,V_identifier) identifier;
@property (T@"NSDictionary",R,V_properties) properties;
@property (T@"CBTrackedAnimation",&,V_trackedAnimation) trackedAnimation;
@property (Tf,R,V_largestStep) largestStep;
@property (Ti,R,V_totalSteps) totalSteps;
@property (Tf,R,V_largestTimeDelta) largestTimeDelta;
@property (TB,R,GisEternal) eternal;
```

## Class methods

```
+[CBRamp className];
+[CBRamp newLinearRampWithWithOrigin:target:length:frequency:identifier:];
```

## Instance methods

```
-[CBRamp isFinished];
-[CBRamp properties];
-[CBRamp frequency];
-[CBRamp identifier];
-[CBRamp currentTimestamp];
-[CBRamp startTime];
-[CBRamp dealloc];
-[CBRamp currentValue];
-[CBRamp length];
-[CBRamp targetValue];
-[CBRamp description];
-[CBRamp originalValue];
-[CBRamp totalSteps];
-[CBRamp remainingLength];
-[CBRamp clockRamp];
-[CBRamp clockRamp:];
-[CBRamp currentAbsoluteTimestamp];
-[CBRamp initWithOrigin:target:length:frequency:identifier:];
-[CBRamp initWithOrigin:target:length:frequency:identifier:properties:];
-[CBRamp isEternal];
-[CBRamp largestStep];
-[CBRamp largestTimeDelta];
-[CBRamp rampFinishedCallback];
-[CBRamp rampProgressCallback];
-[CBRamp setRampFinishedCallback:];
-[CBRamp setRampProgressCallback:];
-[CBRamp setTrackedAnimation:];
-[CBRamp startAbsoluteTime];
-[CBRamp trackedAnimation];
-[CBRamp updateTargetValue:];
```
