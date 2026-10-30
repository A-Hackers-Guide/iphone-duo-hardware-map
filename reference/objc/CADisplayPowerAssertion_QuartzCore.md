# `CADisplayPowerAssertion`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 3 properties, 13 instance methods, 0 class methods

## Instance variables

```
I _display_id;
q _reason;
@"NSString" _identifier;
I _server_port;
I _client_port;
B _active;
B _invalidated;
```

## Properties

```
@property (Tq,R,N) reason;
@property (T@"NSString",R,N) identifier;
@property (TB,R,N,GisActive) active;
```

## Instance methods

```
-[CADisplayPowerAssertion acquire];
-[CADisplayPowerAssertion identifier];
-[CADisplayPowerAssertion dealloc];
-[CADisplayPowerAssertion invalidate];
-[CADisplayPowerAssertion description];
-[CADisplayPowerAssertion reason];
-[CADisplayPowerAssertion isActive];
-[CADisplayPowerAssertion cancel];
-[CADisplayPowerAssertion _acquireAndWait:];
-[CADisplayPowerAssertion _ensureValid];
-[CADisplayPowerAssertion _initWithDisplayId:reason:identifier:];
-[CADisplayPowerAssertion acquireAndWaitForPowerOn];
-[CADisplayPowerAssertion initializeClientPort];
```
