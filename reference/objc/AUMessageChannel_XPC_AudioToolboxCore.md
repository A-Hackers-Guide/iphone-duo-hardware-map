# `AUMessageChannel_XPC`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AUMessageChannel`
- 2 instance variables, 1 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSXPCConnection" _xpcConnection;
@? _callHostBlock;
```

## Properties

```
@property (T@?,C,N,V_callHostBlock) callHostBlock;
```

## Instance methods

```
-[AUMessageChannel_XPC initWithListenerEndpoint:];
-[AUMessageChannel_XPC dealloc];
-[AUMessageChannel_XPC callAudioUnit:];
-[AUMessageChannel_XPC callHostBlock];
-[AUMessageChannel_XPC setCallHostBlock:];
```
