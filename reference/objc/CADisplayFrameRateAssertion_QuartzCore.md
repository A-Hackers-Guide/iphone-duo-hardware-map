# `CADisplayFrameRateAssertion`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAInvalidatable`
- 7 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
I _display_id;
f _maximum_frame_rate;
@"NSString" _identifier;
I _server_port;
I _client_port;
B _active;
B _invalidated;
```

## Properties

```
@property (Tf,R,N) maximumFrameRate;
@property (T@"NSString",R,N) identifier;
@property (TB,R,N,GisActive) active;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CADisplayFrameRateAssertion acquire];
-[CADisplayFrameRateAssertion maximumFrameRate];
-[CADisplayFrameRateAssertion identifier];
-[CADisplayFrameRateAssertion dealloc];
-[CADisplayFrameRateAssertion invalidate];
-[CADisplayFrameRateAssertion description];
-[CADisplayFrameRateAssertion isActive];
-[CADisplayFrameRateAssertion cancel];
-[CADisplayFrameRateAssertion _ensureValid];
-[CADisplayFrameRateAssertion _initWithDisplayId:maximumFrameRate:identifier:];
-[CADisplayFrameRateAssertion initializeClientPort];
```
