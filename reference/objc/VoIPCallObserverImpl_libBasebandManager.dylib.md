# `VoIPCallObserverImpl`

- Image: [`/usr/lib/libBasebandManager.dylib`](../userland/usr__lib__libBasebandManager.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CXCallObserverDelegate`
- 4 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
{function<void (bool, bool, const char *)>="__f_"{__value_func<void (bool, bool, const char *)>="__buf_"(type="__data"[24C])"__f_"^v}} fCallback;
@"CXCallObserver" fCallObserver;
B fVoIPCallStarting;
B fVoIPCallActive;
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
-[VoIPCallObserverImpl callObserver:callChanged:];
-[VoIPCallObserverImpl initWithCallback:queue:];
```
