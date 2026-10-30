# `NWAccumulatedValue`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSObject" _object;
@"NSString" _keyPath;
@"NWAccumulation" _accumulation;
@? _callback;
```

## Properties

```
@property (T@"NSObject",&,N,V_object) object;
@property (T@"NSString",&,N,V_keyPath) keyPath;
@property (T@"NWAccumulation",&,N,V_accumulation) accumulation;
@property (T@?,C,N,V_callback) callback;
```

## Instance methods

```
-[NWAccumulatedValue keyPath];
-[NWAccumulatedValue setKeyPath:];
-[NWAccumulatedValue callback];
-[NWAccumulatedValue setCallback:];
-[NWAccumulatedValue setAccumulation:];
-[NWAccumulatedValue snapshot];
-[NWAccumulatedValue setObject:];
-[NWAccumulatedValue description];
-[NWAccumulatedValue object];
-[NWAccumulatedValue accumulation];
```
