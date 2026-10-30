# `ReverseSiphonDelegate`

- Image: [`/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient`](../userland/System__Library__PrivateFrameworks__IsolatedCoreAudioClient.framework__IsolatedCoreAudioClient.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`, `IsolatedCoreAudioReverseSiphonProtocol`
- 6 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
^? mAvailabilityCallback;
^? mLapseCallback;
^v mAvailabilityData;
^v mLapseData;
@"NSXPCListener" _reverseListener;
@"NSXPCInterface" _reverseInterface;
```

## Properties

```
@property (T@"NSXPCListener",&,N,V_reverseListener) reverseListener;
@property (T@"NSXPCInterface",&,N,V_reverseInterface) reverseInterface;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ReverseSiphonDelegate listener:shouldAcceptNewConnection:];
-[ReverseSiphonDelegate init];
-[ReverseSiphonDelegate LapseCallback:with:];
-[ReverseSiphonDelegate AudioAvailabilityCallback:atSample:with:];
-[ReverseSiphonDelegate reverseListener];
-[ReverseSiphonDelegate reverseInterface];
-[ReverseSiphonDelegate setAvailabilityCallback:data:];
-[ReverseSiphonDelegate setLapseCallback:data:];
-[ReverseSiphonDelegate setReverseInterface:];
-[ReverseSiphonDelegate setReverseListener:];
```
