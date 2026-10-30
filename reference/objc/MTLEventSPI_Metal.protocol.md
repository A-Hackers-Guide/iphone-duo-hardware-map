# `MTLEventSPI` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLEvent`
- 0 instance variables, 2 properties, 3 instance methods, 0 class methods

## Properties

```
@property (TB,N) enableBarrier;
@property (TB,R) supportsRollback;
```

## Instance methods

```
-[MTLEventSPI supportsRollback];
-[MTLEventSPI enableBarrier];
-[MTLEventSPI setEnableBarrier:];
```
