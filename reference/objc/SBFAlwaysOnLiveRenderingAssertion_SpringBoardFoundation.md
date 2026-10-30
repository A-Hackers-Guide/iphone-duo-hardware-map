# `SBFAlwaysOnLiveRenderingAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 5 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@? _invalidationHandler;
@"NSString" _reason;
@"NSDate" _createdAt;
B _valid;
d _timeout;
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
-[SBFAlwaysOnLiveRenderingAssertion dealloc];
-[SBFAlwaysOnLiveRenderingAssertion invalidate];
-[SBFAlwaysOnLiveRenderingAssertion initWithReason:timeout:invalidationHandler:];
-[SBFAlwaysOnLiveRenderingAssertion isValid];
-[SBFAlwaysOnLiveRenderingAssertion description];
-[SBFAlwaysOnLiveRenderingAssertion initWithReason:invalidationHandler:];
-[SBFAlwaysOnLiveRenderingAssertion reason];
-[SBFAlwaysOnLiveRenderingAssertion _startAutoInvalidationTimer];
-[SBFAlwaysOnLiveRenderingAssertion createdAt];
```
