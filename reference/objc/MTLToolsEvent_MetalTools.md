# `MTLToolsEvent`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLEventSPI`
- 0 instance variables, 8 properties, 6 instance methods, 0 class methods

## Properties

```
@property (TB,N) enableBarrier;
@property (TB,R) supportsRollback;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsEvent device];
-[MTLToolsEvent label];
-[MTLToolsEvent setLabel:];
-[MTLToolsEvent supportsRollback];
-[MTLToolsEvent enableBarrier];
-[MTLToolsEvent setEnableBarrier:];
```
