# `_UIMotionAttitudeAnalyzer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIMotionAnalyzer`
- Protocols: `_UISettingsKeyObserver`
- 23 instance variables, 4 properties, 30 instance methods, 0 class methods

## Instance variables

```
d _smoothingDegree;
d _referenceShiftSpeed;
d _distanceMultiplier;
B _hasReferenceQuaternion;
(_GLKQuaternion=""{?="x"f"y"f"z"f"w"f}""{?="v"(_GLKVector3=""{?="x"f"y"f"z"f}""{?="r"f"g"f"b"f}""{?="s"f"t"f"p"f}"v"[3f])"s"f}"q"[4f]) _referenceQuaternion;
(_GLKQuaternion=""{?="x"f"y"f"z"f"w"f}""{?="v"(_GLKVector3=""{?="x"f"y"f"z"f}""{?="r"f"g"f"b"f}""{?="s"f"t"f"p"f}"v"[3f])"s"f}"q"[4f]) _absoluteQuaternion;
d _lastUpdate;
d _idleStartTime;
{UIOffset="horizontal"d"vertical"d} _idleStartOffset;
d _jumpThreshold;
d _idleLeeway;
d _secondsBeforeIdle;
d _lockValue;
d _lockStrength;
@"UIWindow" _diagnosticsWindow;
@"UILabel" _idleIndicator;
@"UIView" _horizontalLockIndicator;
@"UIView" _verticalLockIndicator;
B _hasHistory;
{UIOffset="horizontal"d"vertical"d} _lastAppliedViewerOffset;
(_GLKQuaternion=""{?="x"f"y"f"z"f"w"f}""{?="v"(_GLKVector3=""{?="x"f"y"f"z"f}""{?="r"f"g"f"b"f}""{?="s"f"t"f"p"f}"v"[3f])"s"f}"q"[4f]) _lastAppliedRelativeQuaternion;
B _isApplyingHysteresis;
(_GLKQuaternion=""{?="x"f"y"f"z"f"w"f}""{?="v"(_GLKVector3=""{?="x"f"y"f"z"f}""{?="r"f"g"f"b"f}""{?="s"f"t"f"p"f}"v"[3f])"s"f}"q"[4f]) _relativeQuaternionOnHysteresisEntry;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIMotionAttitudeAnalyzer _updateIdleStateForRawOffset:timestamp:];
-[_UIMotionAttitudeAnalyzer _updateSettings];
-[_UIMotionAttitudeAnalyzer _createDirectionLockIndicators];
-[_UIMotionAttitudeAnalyzer _shiftReferenceToYieldRelativeQuaternion:];
-[_UIMotionAttitudeAnalyzer _updateAcceleratedOutputRangeFixingOffset:];
-[_UIMotionAttitudeAnalyzer _referenceShiftRadiansPerSecondForAngle:];
-[_UIMotionAttitudeAnalyzer dealloc];
-[_UIMotionAttitudeAnalyzer reset];
-[_UIMotionAttitudeAnalyzer _directionLockStrength];
-[_UIMotionAttitudeAnalyzer settings:changedValueForKey:];
-[_UIMotionAttitudeAnalyzer _createDiagnosticsWindow];
-[_UIMotionAttitudeAnalyzer updateHistory];
-[_UIMotionAttitudeAnalyzer _tearDownDiagnosticsWindow];
-[_UIMotionAttitudeAnalyzer _updateSmoothedOffsetForRawOffset:];
-[_UIMotionAttitudeAnalyzer _isIdleGivenTimestamp:];
-[_UIMotionAttitudeAnalyzer _shouldSuspendApplicationForHysteresisGivenNewViewerOffset:wasSuspendingApplicationForHysteresis:];
-[_UIMotionAttitudeAnalyzer applyHysteresisWithReceivedEventTimestamp:timeSinceLastNewMotionEvent:slowUpdatesEnabled:returningShouldToggleSlowUpdates:logger:];
-[_UIMotionAttitudeAnalyzer _updateReferenceAttitude:timestamp:];
-[_UIMotionAttitudeAnalyzer updateWithEvent:];
-[_UIMotionAttitudeAnalyzer _resetDirectionalLockWithViewerOffset:];
-[_UIMotionAttitudeAnalyzer _currentRawOffset:];
-[_UIMotionAttitudeAnalyzer _relativeQuaternion];
-[_UIMotionAttitudeAnalyzer _updateDirectionalLockIndicators];
-[_UIMotionAttitudeAnalyzer resetHysteresis];
-[_UIMotionAttitudeAnalyzer _createIdleIndicator];
-[_UIMotionAttitudeAnalyzer _showIdleUI:];
-[_UIMotionAttitudeAnalyzer _tearDownDirectionLockIndicators];
-[_UIMotionAttitudeAnalyzer _tearDownIdleIndicator];
-[_UIMotionAttitudeAnalyzer initWithSettings:];
-[_UIMotionAttitudeAnalyzer _directionLockStatus];
```
