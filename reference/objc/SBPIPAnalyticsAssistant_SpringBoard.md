# `SBPIPAnalyticsAssistant`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 1 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSString" _bundleIdentifier;
q _contentType;
B _isAutoPIPEnabled;
d _activateDuration;
d _activationTimestamp;
@? _invalidationBlock;
@"NSString" _analyticsIdentifier;
```

## Properties

```
@property (T@"NSString",R,N,V_analyticsIdentifier) analyticsIdentifier;
```

## Instance methods

```
-[SBPIPAnalyticsAssistant invalidate];
-[SBPIPAnalyticsAssistant analyticsIdentifier];
-[SBPIPAnalyticsAssistant _generateMutableAnalyticsPayload];
-[SBPIPAnalyticsAssistant generateAnalyticsPayload];
-[SBPIPAnalyticsAssistant initWithBundleIdentifier:contentType:isAutoPIPEnabled:invalidationBlock:];
-[SBPIPAnalyticsAssistant noteBecameActiveAtTime:];
-[SBPIPAnalyticsAssistant noteBecameInactiveAtTime:];
```
