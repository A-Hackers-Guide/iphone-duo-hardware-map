# `SBFullScreenSessionMetric`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAnalyticsStateMachineEventHandler`
- 4 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
d _startTimestamp;
@"NSString" _startReason;
@"NSString" _primaryBundleIdentifier;
@"NSString" _sideBundleIdentifier;
```

## Properties

```
@property (Td,N,V_startTimestamp) startTimestamp;
@property (T@"NSString",C,N,V_startReason) startReason;
@property (T@"NSString",C,N,V_primaryBundleIdentifier) primaryBundleIdentifier;
@property (T@"NSString",C,N,V_sideBundleIdentifier) sideBundleIdentifier;
```

## Instance methods

```
-[SBFullScreenSessionMetric setStartTimestamp:];
-[SBFullScreenSessionMetric init];
-[SBFullScreenSessionMetric startTimestamp];
-[SBFullScreenSessionMetric startReason];
-[SBFullScreenSessionMetric setStartReason:];
-[SBFullScreenSessionMetric _bundleIdentifierForElementWithLayoutRole:fromContext:];
-[SBFullScreenSessionMetric _sendCoreAnalyticsEventWithStartReason:endReason:duration:primaryBundleIdentifier:doNotDisturbActive:hardwareKeyboardAttached:];
-[SBFullScreenSessionMetric primaryBundleIdentifier];
-[SBFullScreenSessionMetric sendCoreAnalyticsEventWithName:payload:];
-[SBFullScreenSessionMetric setPrimaryBundleIdentifier:];
-[SBFullScreenSessionMetric setSideBundleIdentifier:];
-[SBFullScreenSessionMetric sideBundleIdentifier];
```
