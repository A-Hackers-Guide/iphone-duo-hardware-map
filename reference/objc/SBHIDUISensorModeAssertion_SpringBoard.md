# `SBHIDUISensorModeAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 8 instance variables, 12 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _pocketTouchesExpected;
@"SBHIDUISensorModeController" _sensorModeController;
@"NSString" _reason;
q _source;
q _displayState;
q _digitizerMode;
q _proximitySuspensionMode;
Q _wakeSwipeEdges;
```

## Properties

```
@property (T@"SBHIDUISensorModeController",W,N,V_sensorModeController) sensorModeController;
@property (T@"NSString",C,N,V_reason) reason;
@property (Tq,N,V_source) source;
@property (Tq,N,V_displayState) displayState;
@property (Tq,N,V_digitizerMode) digitizerMode;
@property (Tq,N,V_proximitySuspensionMode) proximitySuspensionMode;
@property (TB,N,V_pocketTouchesExpected) pocketTouchesExpected;
@property (TQ,N,V_wakeSwipeEdges) wakeSwipeEdges;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBHIDUISensorModeAssertion setDisplayState:];
-[SBHIDUISensorModeAssertion setSensorModeController:];
-[SBHIDUISensorModeAssertion setPocketTouchesExpected:];
-[SBHIDUISensorModeAssertion succinctDescriptionBuilder];
-[SBHIDUISensorModeAssertion digitizerMode];
-[SBHIDUISensorModeAssertion displayState];
-[SBHIDUISensorModeAssertion setReason:];
-[SBHIDUISensorModeAssertion descriptionWithMultilinePrefix:];
-[SBHIDUISensorModeAssertion setSource:];
-[SBHIDUISensorModeAssertion wakeSwipeEdges];
-[SBHIDUISensorModeAssertion succinctDescription];
-[SBHIDUISensorModeAssertion setDigitizerMode:];
-[SBHIDUISensorModeAssertion invalidate];
-[SBHIDUISensorModeAssertion setWakeSwipeEdges:];
-[SBHIDUISensorModeAssertion setProximitySuspensionMode:];
-[SBHIDUISensorModeAssertion description];
-[SBHIDUISensorModeAssertion reason];
-[SBHIDUISensorModeAssertion pocketTouchesExpected];
-[SBHIDUISensorModeAssertion proximitySuspensionMode];
-[SBHIDUISensorModeAssertion sensorModeController];
-[SBHIDUISensorModeAssertion source];
-[SBHIDUISensorModeAssertion descriptionBuilderWithMultilinePrefix:];
```
