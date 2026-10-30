# `MTLToolsSharedEvent`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsEvent`
- Protocols: `MTLSharedEventSPI`
- 0 instance variables, 9 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"IOSurfaceSharedEvent",R,N) IOSurfaceSharedEvent;
@property (TB,R) supportsRollback;
@property (TQ) signaledValue;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsSharedEvent label];
-[MTLToolsSharedEvent setLabel:];
-[MTLToolsSharedEvent newSharedEventHandle];
-[MTLToolsSharedEvent notifyListener:atValue:block:];
-[MTLToolsSharedEvent setSignaledValue:];
-[MTLToolsSharedEvent signaledValue];
-[MTLToolsSharedEvent waitUntilSignaledValue:timeoutMS:];
-[MTLToolsSharedEvent IOSurfaceSharedEvent];
-[MTLToolsSharedEvent supportsRollback];
```
