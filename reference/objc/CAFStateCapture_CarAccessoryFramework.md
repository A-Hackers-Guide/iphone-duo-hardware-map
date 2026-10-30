# `CAFStateCapture`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
@? _capture;
@"NSObject<OS_dispatch_queue>" _queue;
Q _handler;
```

## Properties

```
@property (T@?,C,N,V_capture) capture;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (TQ,N,V_handler) handler;
@property (T@"NSString",R,N,V_identifier) identifier;
```

## Instance methods

```
-[CAFStateCapture identifier];
-[CAFStateCapture dealloc];
-[CAFStateCapture setHandler:];
-[CAFStateCapture queue];
-[CAFStateCapture handler];
-[CAFStateCapture stateCapture];
-[CAFStateCapture description];
-[CAFStateCapture capture];
-[CAFStateCapture setQueue:];
-[CAFStateCapture setCapture:];
-[CAFStateCapture initWithIdentifier:capture:];
```
