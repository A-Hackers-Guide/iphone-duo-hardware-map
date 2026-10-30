# `MTLResourceViewPool` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 5 instance methods, 0 class methods

## Properties

```
@property (T{MTLResourceID=Q},R,N) baseResourceID;
@property (TQ,R,N) resourceViewCount;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",R,N) label;
```

## Instance methods

```
-[MTLResourceViewPool device];
-[MTLResourceViewPool label];
-[MTLResourceViewPool baseResourceID];
-[MTLResourceViewPool copyResourceViewsFromPool:sourceRange:destinationIndex:];
-[MTLResourceViewPool resourceViewCount];
```
