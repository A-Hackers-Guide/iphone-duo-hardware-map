# `PLProcessExitAggregator`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
C _exitReasonNamespace;
I _labelIdx;
I _lastTTR;
Q _exitReasonCode;
Q _jetsamPriority;
```

## Properties

```
@property (TI,V_labelIdx) labelIdx;
@property (TI,V_lastTTR) lastTTR;
@property (TC,V_exitReasonNamespace) exitReasonNamespace;
@property (TQ,V_exitReasonCode) exitReasonCode;
@property (TQ,V_jetsamPriority) jetsamPriority;
```

## Instance methods

```
-[PLProcessExitAggregator setJetsamPriority:];
-[PLProcessExitAggregator hash];
-[PLProcessExitAggregator description];
-[PLProcessExitAggregator jetsamPriority];
-[PLProcessExitAggregator copyWithZone:];
-[PLProcessExitAggregator isEqual:];
-[PLProcessExitAggregator lastTTR];
-[PLProcessExitAggregator exitReasonCode];
-[PLProcessExitAggregator exitReasonNamespace];
-[PLProcessExitAggregator labelIdx];
-[PLProcessExitAggregator setExitReasonCode:];
-[PLProcessExitAggregator setExitReasonNamespace:];
-[PLProcessExitAggregator setLabelIdx:];
-[PLProcessExitAggregator setLastTTR:];
```
