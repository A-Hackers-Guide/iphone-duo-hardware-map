# `SBBannerGestureRecognizerPriorityAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 5 instance variables, 7 properties, 8 instance methods, 1 class methods

## Instance variables

```
@? _invalidationHandler;
@? _enablementChangeHandler;
B _enabled;
q _priority;
@"NSString" _reason;
```

## Properties

```
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (Tq,R,N,V_priority) priority;
@property (T@"NSString",R,C,N,V_reason) reason;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBBannerGestureRecognizerPriorityAssertion isValidBannerGestureRecognizerPriority:];
```

## Instance methods

```
-[SBBannerGestureRecognizerPriorityAssertion priority];
-[SBBannerGestureRecognizerPriorityAssertion dealloc];
-[SBBannerGestureRecognizerPriorityAssertion isEnabled];
-[SBBannerGestureRecognizerPriorityAssertion invalidate];
-[SBBannerGestureRecognizerPriorityAssertion setEnabled:];
-[SBBannerGestureRecognizerPriorityAssertion description];
-[SBBannerGestureRecognizerPriorityAssertion reason];
-[SBBannerGestureRecognizerPriorityAssertion initWithPriority:reason:enablementChangeHandler:invalidationHandler:];
```
