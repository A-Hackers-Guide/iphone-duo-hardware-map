# `AUAudioUnitBus_XPC`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AUAudioUnitBus`
- Protocols: `NSSecureCoding`
- 7 instance variables, 0 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"AUAudioUnit_XPC" _audioUnit;
@"NSXPCConnection" _remoteAUXPCConnection;
I _scope;
I _element;
@"AVAudioFormat" _format;
@"NSArray" _supportedChannelLayoutTags;
B _removingObserverWithContext;
```

## Class methods

```
+[AUAudioUnitBus_XPC supportsSecureCoding];
+[AUAudioUnitBus_XPC automaticallyNotifiesObserversForKey:];
```

## Instance methods

```
-[AUAudioUnitBus_XPC addObserver:forKeyPath:options:context:];
-[AUAudioUnitBus_XPC removeObserver:forKeyPath:];
-[AUAudioUnitBus_XPC dealloc];
-[AUAudioUnitBus_XPC isEnabled];
-[AUAudioUnitBus_XPC setEnabled:];
-[AUAudioUnitBus_XPC encodeWithCoder:];
-[AUAudioUnitBus_XPC initWithCoder:];
-[AUAudioUnitBus_XPC removeObserver:forKeyPath:context:];
-[AUAudioUnitBus_XPC format];
-[AUAudioUnitBus_XPC propertyChanged:];
-[AUAudioUnitBus_XPC setFormat:error:];
```
