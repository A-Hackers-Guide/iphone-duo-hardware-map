# `AVSinkSubscriber`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVCancellable`
- 4 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"AVPublisher" _publisher;
@? _sink;
@"<AVCancellable>" _token;
^{OpaqueFigSimpleMutex=} _cancelMutex;
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
-[AVSinkSubscriber dealloc];
-[AVSinkSubscriber description];
-[AVSinkSubscriber cancel];
-[AVSinkSubscriber initWithPublisher:requestingInitialValue:sink:];
```
